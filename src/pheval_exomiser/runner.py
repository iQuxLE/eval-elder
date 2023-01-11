"""Exomiser Runner"""
from dataclasses import dataclass
from pathlib import Path
from pheval.runners.runner import PhEvalRunner

from pheval_exomiser.post_process.post_process import post_process_exomiser_results
from pheval_exomiser.prepare.prepare import (
    prepare_scrambled_phenopackets,
    prepare_spiked_vcfs,
    prepare_updated_phenopackets,
)
from pheval_exomiser.run.run import prepare_batch_files, run_exomiser
from pheval_exomiser.config_parser import parse_exomiser_config


@dataclass
class ExomiserPhEvalRunner(PhEvalRunner):
    """_summary_"""

    input_dir: Path
    testdata_dir: Path
    tmp_dir: Path
    output_dir: Path
    config_file: Path

    def prepare(self):
        """prepare"""
        print("preparing")
        config = parse_exomiser_config(self.config_file)
        prepare_updated_phenopackets(
            testdata_dir=Path(self.testdata_dir), config=config
        )
        prepare_scrambled_phenopackets(
            testdata_dir=Path(self.testdata_dir), config=config
        )
        prepare_spiked_vcfs(testdata_dir=Path(self.testdata_dir), config=config)

    def run(self):
        """run"""
        print("running with exomiser")
        config = parse_exomiser_config(self.config_file)
        prepare_batch_files(input_dir=Path(self.input_dir), output_dir=Path(self.output_dir), config=config)
        run_exomiser(output_dir=self.output_dir, config=config)

    def post_process(self):
        """post_process"""
        print("post processing")
        config = parse_exomiser_config(self.config_file)
        post_process_exomiser_results(output_dir=self.output_dir, config=config)
