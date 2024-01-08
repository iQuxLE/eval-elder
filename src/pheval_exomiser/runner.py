"""Exomiser Runner"""
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Any

from pheval.post_processing.post_processing import generate_pheval_result, PhEvalDiseaseResult
from pheval.utils.file_utils import all_files

from pheval_exomiser.prepare.simple_service import SimpleService
from pheval.runners.runner import PhEvalRunner
from pheval_exomiser.prepare.utils.similarity_measures import SimilarityMeasures
from pheval_exomiser.prepare.core.elder import ElderRunner
from pheval_exomiser.prepare.tool_specific_configuration_options import ElderPostProcessingConfig
from pheval.utils.phenopacket_utils import phenopacket_reader
from pheval.utils.phenopacket_utils import PhenopacketUtil


@dataclass
class ExomiserPhEvalRunner(PhEvalRunner):
    """_summary_"""

    input_dir: Path
    testdata_dir: Path
    tmp_dir: Path
    output_dir: Path
    config_file: Path
    version: str
    results: List[Any] = field(default_factory=list)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.simple_service = SimpleService()
        self.config = ElderPostProcessingConfig.parse_obj(self.input_dir_config.tool_specific_configuration_options)
        self.simple_runner = ElderRunner(
            similarity_measure=SimilarityMeasures.COSINE)
        self.current_file_name = None

    def prepare(self):
        """prepare"""
        print("preparing and working")
        self.simple_service.greet()
        start_init = time.time()
        self.simple_runner.initialize_data()
        init_time = time.time() - start_init
        print("initialized simple runner")
        print(init_time)
        start_setup = time.time()
        self.simple_runner.setup_collections()
        print("set up collections")
        setup_time = time.time() - start_setup
        print(setup_time)


    def run(self):
        """run"""
        print("running with exomiser")
        path = Path("/Users/carlo/Carlo/pheval/pheval/corpora/lirical/default/phenopackets")
        for i in all_files(path):
            self.current_file_name = i.stem
            phenopacket = phenopacket_reader(i)
            phenopacket_util = PhenopacketUtil(phenopacket)
            observed_phenotypes = phenopacket_util.observed_phenotypic_features()
            observed_phenotypes_hpo_ids = [
                observed_phenotype.type.id for observed_phenotype in observed_phenotypes
            ]

            if self.simple_runner is not None:
                self.results = self.simple_runner.run_analysis(observed_phenotypes_hpo_ids)
                print("Running with custom pheval runner")
                self.post_process()
            else:
                print("Main system is not initialized")


    def post_process(self):
        """post_process"""
        print("post processing")
        if self.input_dir_config.disease_analysis and self.results:
            disease_results = self.create_disease_results(self.results)
            output_file_name = f"{self.current_file_name}_disease_results.tsv"  # Create a unique output file name
            generate_pheval_result(
                pheval_result=disease_results,
                sort_order_str=self.config.post_process.sort_order,
                output_dir=self.pheval_disease_results_dir,
                tool_result_path=Path(output_file_name),
            )
        else:
            print("No results to process")

    @staticmethod
    def create_disease_results(query_results):
        return [
            PhEvalDiseaseResult(disease_name=disease_id, disease_identifier=disease_id, score=distance)
            for disease_id, distance in query_results
        ]

