import time

import numpy as np
from chromadb.types import Collection

from pheval_exomiser.prepare.core.base_service import BaseService
from pheval_exomiser.prepare.core.data_processor import DataProcessor


class DiseaseAvgEmbeddingService(BaseService):
    """
    upsert averaged embeddings from hp_embeddings (cached dict from ont_hp collection) that are connected to the
    relevant disease from disease_to_hps (cached dict from hpoa) into the disease_avg_embeddings_collection that
    contains disease and the average embeddings of the correlating hp terms
    """

    def __init__(self, data_processor: DataProcessor):
        super().__init__(data_processor)
        self.precomputed_embeddings = {}

    def process_data(self) -> Collection:
        if not self.disease_to_hps_from_omim:
            raise ValueError("disease to hps data is not initialized")
        if not self.disease_avg_embeddings_collection:
            raise ValueError("disease_new_avg_embeddings collection is not initialized")

        if self.disease_new_avg_embeddings_collection:
            print("Disease Avg Embeddings collection early return, cause already initialized!")
            return self.disease_new_avg_embeddings_collection

        batch_size = 25
        batch = []
        embedding_calc_time = 0
        upsert_time = 0

        for disease, hps in self.disease_to_hps_from_omim.items():
            start = time.time()
            average_embedding = self.data_processor.calculate_average_embedding(hps, self.hp_embeddings)
            embedding_calc_time += time.time() - start
            batch.append((disease, average_embedding.tolist()))

            if len(batch) >= batch_size:
                start = time.time()
                self.upsert_batch(batch)
                upsert_time += time.time() - start
                batch = []

        if batch:
            start = time.time()
            self.upsert_batch(batch)
            upsert_time += time.time() - start

        print(f"Total time for embedding calculations (avg): {embedding_calc_time}s")
        print(f"Total time for upsert operations (avg): {upsert_time}s")

        return self.disease_avg_embeddings_collection

    def upsert_batch(self, batch):
        ids = [item[0] for item in batch]
        embeddings = [item[1] for item in batch]
        metadatas = [{"type": "disease"}] * len(batch)
        self.disease_avg_embeddings_collection.upsert(ids=ids, embeddings=embeddings, metadatas=metadatas)

    # def compute_clustered_embeddings(self, hpo_terms, hpo_clustering):
    #     all_clusters = sorted(hpo_clustering.all_clusters)  # consistent sorted order of clusters
    #     embedding_size = 1536
    #     cluster_embeddings = {cluster: [] for cluster in all_clusters} # init embeddings for all clusters
    #
    #     for hpo_term in hpo_terms:
    #         cluster = hpo_clustering.find_highest_parent(hpo_term) # get cluster
    #         cluster_embeddings[cluster].append(self.hp_embeddings.get(hpo_term, np.zeros(embedding_size)))
    #     # concatenate embeddings in consistent order of clusters
    #     concatenated_embedding = []
    #     for cluster in all_clusters:
    #         if cluster_embeddings[cluster]:
    #             concatenated_embedding.append(np.mean(cluster_embeddings[cluster], axis=0))
    #         else:
    #             concatenated_embedding.append(-1 * np.ones(embedding_size)) # -1 vector for missing clusters
    #
    #     return np.concatenate(concatenated_embedding)






























    # def compute_and_store_clustered_embeddings(self, hpo_clustering):
    #     for disease, hpo_terms in self.disease_to_hps.items():
    #         cluster_embeddings = {}
    #         for hpo_term in hpo_terms:
    #             cluster = hpo_clustering.find_highest_parent(hpo_term)
    #             if cluster in cluster_embeddings:
    #                 cluster_embeddings[cluster].append(self.hp_embeddings[hpo_term])
    #             else:
    #                 cluster_embeddings[cluster] = [self.hp_embeddings[hpo_term]]
    #
    #         concatenated_embedding = np.concatenate(
    #             [np.mean(embeddings, axis=0) for embeddings in cluster_embeddings.values() if embeddings])
    #         self.precomputed_embeddings[disease] = concatenated_embedding



    # def compute_and_store_clustered_embeddings(self, hpo_clustering):
    #     all_clusters = sorted(hpo_clustering.all_clusters)  # consistent sorted order of clusters
    #     embedding_size = 1536
    #     computed_embeddings = {}
    #
    #     for disease, hpo_terms in self.disease_to_hps.items():
    #         cluster_embeddings = {cluster: [] for cluster in all_clusters}  # init embeddings for all clusters
    #
    #         # cluster the HPO terms
    #         for hpo_term in hpo_terms:
    #             cluster = hpo_clustering.find_highest_parent(hpo_term)
    #             if cluster in cluster_embeddings:
    #                 cluster_embeddings[cluster].append(self.hp_embeddings[hpo_term])
    #
    #         # concatenate embeddings in consistent order of clusters
    #         concatenated_embedding = []
    #         for cluster in all_clusters:
    #             if cluster_embeddings[cluster]:
    #                 concatenated_embedding.append(np.mean(cluster_embeddings[cluster], axis=0))
    #             else:
    #                 concatenated_embedding.append(-1 * np.ones(embedding_size))  # -1 vector for missing clusters
    #
    #         concatenated_embedding = np.concatenate(concatenated_embedding)
    #         self.precomputed_embeddings[disease] = concatenated_embedding
    #         computed_embeddings[disease] = concatenated_embedding
    #
    #     return computed_embeddings