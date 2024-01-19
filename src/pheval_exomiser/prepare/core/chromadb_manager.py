import logging
from typing import Optional
import chromadb
from pheval_exomiser.prepare.utils.similarity_measures import SimilarityMeasures
from pheval_exomiser.prepare.config import config_loader

logger = logging.getLogger(__name__)


class ChromaDBManager:
    def __init__(self, similarity: Optional[SimilarityMeasures] = SimilarityMeasures.COSINE):
        config = config_loader.load_config()
        path = config["chroma_db_path"] # change between stagedb and stagedb_new
        self.client = chromadb.PersistentClient(path=path)
        self.ont_hp = self.get_collection("ont_hp")
        self.hpoa = self.get_collection("hpoa3233")
        self.hp_embeddings_collection = self.get_collection("hpo") or self.create_collection(
            "hpo", similarity
        )
        self.disease_avg_embeddings_collection = self.get_collection("average") or self.create_collection(
            "average", similarity
        )
        self.clustered_embeddings_collection = self.get_collection("DiseaseOrganEmbeddings") or self.create_collection(
            "DiseaseOrganEmbeddings", similarity
        )
        # THIS 2 NEW ONES CREATED FOR USING THE OMIM DICT FROM phenotype.hpoa instead hpoa collection
        self.disease_new_avg_embeddings_collection = self.get_collection(
            "DiseaseNewAvgEmbeddingsNew") or self.create_collection(
            "DiseaseNewAvgEmbeddingsNew", similarity
        )
        self.clustered_new_embeddings_collection = self.get_collection(
            "DiseaseNewOrganEmbeddings") or self.create_collection(
            "DiseaseNewOrganEmbeddings", similarity
        )

    def create_collection(self, name: str, similarity: Optional[SimilarityMeasures] = SimilarityMeasures.COSINE):
        try:
            similarity_str_value = similarity.value if similarity else SimilarityMeasures.COSINE.value
            collection = self.client.create_collection(name=name, metadata={"hnsw:space": similarity_str_value})
            return collection
        except chromadb.db.base.UniqueConstraintError:
            logger.info(f"Collection {name} already exists")
            return None

    def get_collection(self, name: str):
        try:
            return self.client.get_collection(name)
        except Exception as e:
            logger.info(f"Error getting collection {name}: {str(e)}")
            return None

    def list_collections(self):
        return self.client.list_collections()
