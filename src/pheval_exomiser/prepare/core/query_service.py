from typing import Any, List

from pheval_exomiser.prepare.core.chromadb_manager import ChromaDBManager
from pheval_exomiser.prepare.core.data_processor import DataProcessor
from pheval_exomiser.prepare.core.disease_avg_embedding_service import DiseaseAvgEmbeddingService


class QueryService:
    def __init__(
            self,
            data_processor: DataProcessor,
            db_manager: ChromaDBManager,
            disease_service: DiseaseAvgEmbeddingService,
            similarity_strategy=None,
    ):
        self.db_manager = db_manager
        self.data_processor = data_processor
        self.similarity_strategy = similarity_strategy
        self.hp_embeddings = data_processor.hp_embeddings  # Dict
        self.disease_service = disease_service

    # def query_diseases_by_hpo_terms_using_inbuild_distance_functions(
    #     self, hpo_ids: List[str], n_results: int
    # ) -> list[Any]:  # str just for early return
    #     """
    #     Queries the 'DiseaseAvgEmbeddings' collection for diseases closest to the average embeddings of given HPO terms.
    #
    #     :param n_results: number of results for query
    #     :param hpo_ids: List of HPO term IDs.
    #     :return: List of diseases sorted by closeness to the average HPO embeddings.
    #     """
    #     # need to check that self contains the collection needed here and the dicts !!!!
    #     avg_embedding = self.data_processor.calculate_average_embedding(
    #         hpo_ids, self.hp_embeddings
    #     )  # self.data_processor
    #     if avg_embedding is None:
    #         raise ValueError("No valid embeddings found for provided HPO terms.")
    #         # return [{"error": "No valid embeddings found for provided HPO terms."}]
    #
    #     query_results = self.disease_service.disease_avg_embeddings_collection.query(  # self.data_processor?
    #         query_embeddings=[avg_embedding.tolist()],
    #         n_results=n_results,  # optional, should be all for
    #         include=["embeddings", "distances"],  # just distances should also work
    #     )
    #
    #     disease_ids = query_results["ids"][0] if "ids" in query_results and query_results["ids"] else []
    #     distances = query_results["distances"][0] if "distances" in query_results and query_results["distances"] else []
    #     sorted_results = sorted(zip(disease_ids, distances, strict=False), key=lambda x: x[1])
    #
    #     return sorted_results

    def query_diseases_by_hpo_terms_using_inbuild_distance_functions(self, hpo_ids: List[str], n_results: int = None) -> \
    list[Any]:
        """
        Queries the 'DiseaseAvgEmbeddings' collection for diseases closest to the average embeddings of given HPO terms.

        :param hpo_ids: List of HPO term IDs.
        :param n_results: Optional number of results to return. Returns all if None.
        :return: List of diseases sorted by closeness to the average HPO embeddings.
        """
        print("n_results at default  = :" + f"{n_results}")
        avg_embedding = self.data_processor.calculate_average_embedding(hpo_ids, self.hp_embeddings)
        if avg_embedding is None:
            raise ValueError("No valid embeddings found for provided HPO terms.")

        query_params = {
            "query_embeddings": [avg_embedding.tolist()],
            "include": ["embeddings", "distances"]
        }

        # Determine the number of results to query for if not provided
        if n_results is None:
            # Perform a binary search to find the maximum safe value for n_results
            estimated_total = self.disease_service.disease_avg_embeddings_collection.get(include=['metadatas'])
            estimated_length = len(estimated_total["metadatas"]) #12468 - 1
            print(f"Estimated length (n_results) == {estimated_length}")
            max_n_results = self.binary_search_max_results(query_params, 11700, estimated_length)
            query_params["n_results"] = max_n_results
            print(f"Using max safe n_results: {max_n_results}")
        else:
            query_params["n_results"] = n_results

        print("1")
        query_results = self.disease_service.disease_avg_embeddings_collection.query(**query_params)
        print("2")
        disease_ids = query_results['ids'][0] if 'ids' in query_results and query_results['ids'] else []
        distances = query_results['distances'][0] if 'distances' in query_results and query_results['distances'] else []
        # labels = query_results['labels'][0] if 'labels' in query_results and query_results[
        #     'labels'] else []  # Fetching labels
        sorted_results = sorted(zip(disease_ids, distances), key=lambda x: x[1]) # remember to add label
        print("Returning result from query service")
        return sorted_results

    def binary_search_max_results(self, query_params, lower_bound, upper_bound):
        max_safe_value = lower_bound

        while lower_bound < upper_bound - 1:
            mid_point = (lower_bound + upper_bound) // 2
            query_params['n_results'] = mid_point

            try:
                query_results = self.disease_service.disease_avg_embeddings_collection.query(**query_params)
                max_safe_value = mid_point
                lower_bound = mid_point
            except RuntimeError as e:
                upper_bound = mid_point

        # Verification step: test values around max_safe_value to ensure it's the highest safe value.
        for test_value in range(max_safe_value - 1, max_safe_value + 2):
            if test_value <= 0:
                continue  # Skip non-positive values
            query_params['n_results'] = test_value
            try:
                self.disease_service.disease_avg_embeddings_collection.query(**query_params)
                max_safe_value = test_value  # Update max_safe_value if this higher value is also safe
            except RuntimeError as e:
                break  # Stop testing if this value causes an error

        return max_safe_value

    def query_with_custom_similarity_function(self, data1, data2):
        if self.similarity_strategy:
            return self.similarity_strategy.calculate_similarity(data1, data2)
        else:
            raise ValueError("No similarity strategy provided")
