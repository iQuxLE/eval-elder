"""Exomiser Runner"""
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Any

from pheval.post_processing.post_processing import generate_pheval_result, PhEvalDiseaseResult

from pheval_exomiser.prepare.simple_service import SimpleService
from pheval.runners.runner import PhEvalRunner
from pheval_exomiser.prepare.utils.similarity_measures import SimilarityMeasures
from pheval_exomiser.prepare.core.elder import ElderRunner
from pheval_exomiser.constants import allfromomim619340
# from pheval_exomiser.post_process.post_process import post_process_result_format
from pheval_exomiser.prepare.tool_specific_configuration_options import ElderPostProcessingConfig
# from pheval_exomiser.prepare.write_application_properties import ExomiserConfigurationFileWriter
# from pheval_exomiser.run.run import prepare_batch_files, run_exomiser


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

    def prepare(self):
        """prepare"""
        # print("preparing")
        # self.simple_service.greet()
        # self.simple_runner.initialize_data()
        # self.simple_runner.setup_collections()

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
        # ExomiserConfigurationFileWriter(
        #     input_dir=self.input_dir,
        #     configurations=ExomiserConfigurations.parse_obj(
        #         self.input_dir_config.tool_specific_configuration_options
        #     ),
        # ).write_application_properties()

    def run(self):
        """run"""
        print("running with exomiser")
        if self.simple_runner is not None:
            self.results = self.simple_runner.run_analysis(allfromomim619340)
            print("Running with custom pheval runner")
        else:
            print("Main system is not initialized")
        # config = ExomiserConfigurations.parse_obj(
        #     self.input_dir_config.tool_specific_configuration_options
        # )
        # prepare_batch_files(
        #     input_dir=self.input_dir,
        #     config=config,
        #     testdata_dir=self.testdata_dir,
        #     tool_input_commands_dir=self.tool_input_commands_dir,
        #     raw_results_dir=self.raw_results_dir,
        #     variant_analysis=self.input_dir_config.variant_analysis,
        # )
        # run_exomiser(
        #     input_dir=self.input_dir,
        #     testdata_dir=self.testdata_dir,
        #     config=config,
        #     output_dir=self.output_dir,
        #     tool_input_commands_dir=self.tool_input_commands_dir,
        #     raw_results_dir=self.raw_results_dir,
        #     exomiser_version=self.version,
        #     variant_analysis=self.input_dir_config.variant_analysis,
        # )

    def post_process(self):
        """post_process"""
        print("post processing")
        if self.input_dir_config.disease_analysis and self.results:
            disease_results = self.create_disease_results(self.results)
            generate_pheval_result(
                pheval_result=disease_results,
                sort_order_str=self.config.post_process.sort_order,  # Access sort_order from config
                output_dir=self.pheval_disease_results_dir,  # Use base class property
                tool_result_path=Path("disease_results.tsv"),
            )
        else:
            print("No results to process")
        # config = ExomiserConfigurations.parse_obj(
        #     self.input_dir_config.tool_specific_configuration_options
        # )
        # post_process_result_format(
        #     config=config,
        #     raw_results_dir=self.raw_results_dir,
        #     output_dir=self.output_dir,
        #     variant_analysis=self.input_dir_config.variant_analysis,
        #     gene_analysis=self.input_dir_config.gene_analysis,
        #     disease_analysis=self.input_dir_config.disease_analysis,
        # )

    @staticmethod
    def create_disease_results(query_results):
        # Convert query results to PhEvalDiseaseResult instances
        return [
            PhEvalDiseaseResult(disease_name=disease_id, disease_identifier=disease_id, score=distance)
            for disease_id, distance in query_results
        ]

    # @staticmethod
    # def load_config(config_file: Path) -> ElderPostProcessingConfig:
    #     with open(config_file, "r") as file:
    #         return ElderPostProcessingConfig.model_validate(yaml.safe_load(file))

















"""
(1)
You've re-declared the attributes from the parent class (input_dir, testdata_dir, etc.). 
While this isn't inherently wrong and can help with readability and understanding what attributes are used, 
it's not necessary due to inheritance. In Python's data classes, the fields are inherited,
so you don't need to redeclare them unless you are changing their type or default values.

(2)
You're parsing configurations multiple times in different methods (prepare, run, and post_process). 
Consider parsing the configuration once in the __init__ or prepare method and storing it as an instance
attribute to be used throughout the class. This can improve performance and maintainability.

(3)
def __init__(self, ...):
    super().__init__(...)
    self.config = ExomiserConfigurations.parse_obj(self.input_dir_config.tool_specific_configuration_options)

"""