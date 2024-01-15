import time
from typing import List

import numpy as np
from chromadb.types import Collection

from pheval_exomiser.prepare.core.base_service import BaseService
from pheval_exomiser.prepare.core.data_processor import DataProcessor


class DiseaseClusteredEmbeddingService(BaseService):
    """
    Handles the computation and upserting of clustered embeddings for diseases. These embeddings are created
    by clustering HPO terms associated with each disease and then concatenating the average embeddings of each cluster.
    """

    def __init__(self, data_processor: DataProcessor, hpo_clustering):
        super().__init__(data_processor)
        self.hpo_clustering = hpo_clustering
        self.clustered_embeddings_collection = self.data_processor.db_manager.clustered_embeddings_collection

    def process_data(self) -> Collection:
        if not self.disease_to_hps:
            raise ValueError("Disease to HPO data is not initialized")
        if not self.clustered_embeddings_collection:
            raise ValueError("Clustered embeddings collection is not initialized")
        # if self.clustered_embeddings_collection:
        #     print("Clustered Embeddings collection early return, cause already initialized!")
        #     return self.clustered_embeddings_collection

        batch_size = 25
        batch = []
        embedding_calc_time = 0
        upsert_time = 0

        for disease, hpo_terms in self.disease_to_hps.items():
            start = time.time()
            clustered_embedding = self.compute_organ_embeddings()
            embedding_calc_time += time.time() - start
            batch.append((disease, clustered_embedding.tolist()))

            if len(batch) >= batch_size:
                start = time.time()
                self.upsert_batch(batch)
                upsert_time += time.time() - start
                batch = []

        if batch:
            start = time.time()
            self.upsert_batch(batch)
            upsert_time += time.time() - start

        print(f"Total time for embedding calculations: {embedding_calc_time}s")
        print(f"Total time for upsert operations: {upsert_time}s")

        return self.clustered_embeddings_collection

    def upsert_batch(self, batch):
        ids = [item[0] for item in batch]
        embeddings = [item[1] for item in batch]
        metadatas = [{"type": "disease"}] * len(batch)
        self.clustered_embeddings_collection.upsert(ids=ids, embeddings=embeddings, metadatas=metadatas)

    def compute_clustered_embeddings_per_hp_term(self, hpo_terms):
        all_clusters = sorted(self.hpo_clustering.all_clusters)
        embedding_size = 1536
        cluster_embeddings = {cluster: [] for cluster in all_clusters}
        terms_with_no_cluster = []

        for hpo_term in hpo_terms:
            cluster = self.hpo_clustering.find_highest_parent(hpo_term)
            embedding = self.hp_embeddings.get(hpo_term)
            if cluster is None:
                terms_with_no_cluster.append(hpo_term)
                continue

            if isinstance(embedding, np.ndarray):
                cluster_embeddings[cluster].append(embedding)
            else:
                cluster_embeddings[cluster].append(np.zeros(embedding_size))

        concatenated_embedding = []
        for cluster in all_clusters:
            if isinstance(cluster_embeddings[cluster], list) and cluster_embeddings[cluster]:
                concatenated_embedding.append(np.mean(cluster_embeddings[cluster], axis=0))
            else:
                concatenated_embedding.append(-1 * np.ones(embedding_size))

        with open('terms_with_no_cluster.txt', 'w') as f:
            for term in terms_with_no_cluster:
                f.write(f"{term}\n")

        return np.concatenate([emb for emb in concatenated_embedding if isinstance(emb, np.ndarray)])

    def compute_organ_embeddings(self, hpo_terms: List[str] = None):
        concatenated_embeddings = []
        if hpo_terms is not None:
            hpo_terms_source = [('Patient', hpo_terms)]
        else:
            hpo_terms_source = self.disease_to_hps.items()

        for disease, hpo_terms in hpo_terms_source:
            organ_system_embeddings = {}

            for hpo_term in hpo_terms:
                organ_system = self.hpo_clustering.get_organ_system(hpo_term)
                if organ_system not in organ_system_embeddings:
                    organ_system_embeddings[organ_system] = []

                embedding = self.hp_embeddings.get(hpo_term, -1 * np.ones(1536))
                organ_system_embeddings[organ_system].append(embedding)

            organ_system_embeddings.pop(None, [])
            sorted_organ_systems = sorted(organ_system_embeddings.keys())

            for organ_system in sorted_organ_systems:
                embeddings = organ_system_embeddings[organ_system]
                if any(isinstance(e, np.ndarray) for e in embeddings):
                    average_embedding = np.mean([e for e in embeddings if isinstance(e, np.ndarray)], axis=0)
                    concatenated_embeddings.append(average_embedding)
                else:
                    concatenated_embeddings.append(-1 * np.ones(1536))

        return np.concatenate(concatenated_embeddings)

