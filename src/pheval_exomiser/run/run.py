import os
import subprocess
from dataclasses import dataclass
from pathlib import Path
# import yaml
from pheval.utils.file_utils import all_files

from pheval_exomiser.config_parser import ExomiserConfig, ExomiserConfigSingleRun
from pheval_exomiser.prepare.create_batch_commands import create_batch_file


@dataclass
class BasicDockerMountsForExomiser:
    phenopacket_test_data: str
    vcf_test_data: str
    exomiser_yaml: str
    batch_file_path: str
    exomiser_data_dir: str


@dataclass
class ExomiserConfigParameters:
    application_properties_path: Path = None
    exomiser_phenotype_version: str = None
    exomiser_hg19_version: str = None
    exomiser_hg38_version: str = None


# def write_output_options(input_dir: Path, output_dir: Path, run: ExomiserConfigSingleRun):
#     try:
#         Path(input_dir.joinpath("output_options")).mkdir()
#     except FileExistsError:
#         pass
#     with open(Path(input_dir).joinpath("output_options/output_options.yaml"), "w") as output_options:
#         yaml.dump({'outputPrefix': f'{output_dir.absolute().joinpath(run.run_identifier)}_results/'}, output_options)
#     output_options.close()
#     return Path(input_dir).joinpath("output_options/output_options.yaml")

def edit_application_properties_data_path_for_exomiser(run: ExomiserConfigSingleRun):
    with open(run.exomiser_configurations.path_to_application_properties_config) as exomiser_config:
        exomiser_config_lines = exomiser_config.readlines()
    exomiser_config.close()
    exomiser_config_lines = [line.replace(line, "exomiser.data-directory=/exomiser-data") if line.startswith(
        "exomiser.data-directory=") else line for line in exomiser_config_lines]
    with open(run.exomiser_configurations.path_to_application_properties_config, "w") as exomiser_config:
        exomiser_config.writelines(exomiser_config_lines)
    exomiser_config.close()


def prepare_batch_files(input_dir: Path, output_dir: Path, config: ExomiserConfig):
    """Prepares the exomiser batch files"""
    try:
        Path(output_dir).mkdir()
        print("...created output directory...")
    except FileExistsError:
        pass
    print("...preparing batch files...")
    for run in config.run.runs:
        # output_options_file = write_output_options(input_dir, output_dir,
        #                                            run) if run.path_to_output_option_file is None and
        #                                            run.path_to_output_option_directory is None else None
        create_batch_file(
            config.run.environment,
            run.path_to_analysis_yaml,
            run.path_to_input_phenopacket_data,
            run.path_to_input_vcf,
            output_dir,
            run.run_identifier,
            run.prepare_batch.max_jobs,
            run.path_to_output_option_directory,
            run.path_to_output_option_file  # if output_options_file is None else output_options_file
        )


def mount_docker(output_dir: Path, run: ExomiserConfigSingleRun) -> BasicDockerMountsForExomiser:
    phenopacket_test_data = f'"{run.path_to_input_phenopacket_data}{os.sep}:/exomiser-testdata-phenopacket"'
    vcf_test_data = (
        f'"{run.path_to_input_vcf}{os.sep}:/exomiser-testdata-vcf"'
    )
    exomiser_yaml = f'"{run.path_to_analysis_yaml.parents[0]}{os.sep}:/exomiser-yaml-template"'
    batch_file_path = f'"{Path(output_dir).joinpath("exomiser_batch_files").absolute()}{os.sep}:/exomiser-batch-file"'
    exomiser_data_dir = f'"{run.exomiser_configurations.exomiser_data_directory}{os.sep}:/exomiser-data"'
    # TODO add mount for results directory to be specified in the output-options
    return BasicDockerMountsForExomiser(
        phenopacket_test_data=phenopacket_test_data,
        vcf_test_data=vcf_test_data,
        exomiser_yaml=exomiser_yaml,
        batch_file_path=batch_file_path,
        exomiser_data_dir=exomiser_data_dir,
    )


def add_exomiser_config_file_for_docker(run: ExomiserConfigSingleRun) -> ExomiserConfigParameters:
    return ExomiserConfigParameters(
        application_properties_path=run.exomiser_configurations.path_to_application_properties_config.parents[0]
    )


def add_exomiser_config_parameters_for_docker(run: ExomiserConfigSingleRun) -> ExomiserConfigParameters:
    return ExomiserConfigParameters(
        exomiser_hg19_version=run.exomiser_configurations.application_properties_arguments.exomiser_hg19_version,
        exomiser_hg38_version=run.exomiser_configurations.application_properties_arguments.exomiser_hg38_version,
        exomiser_phenotype_version=run.exomiser_configurations.application_properties_arguments.exomiser_phenotype_version)


def exomiser_config_parameters(run: ExomiserConfigSingleRun) -> ExomiserConfigParameters:
    return (
        add_exomiser_config_file_for_docker(run)
        if run.exomiser_configurations.path_to_application_properties_config is not None
        else add_exomiser_config_parameters_for_docker(run)
    )


def run_exomiser_local(output_dir: Path, config: ExomiserConfig):
    print("...running exomiser...")
    os.chdir(output_dir)
    for run in config.run.runs:
        # try:
        #     os.mkdir(Path(output_dir).joinpath(Path(run.run_identifier + "_results")))
        # except FileExistsError:
        #     pass
        prefixed_batch_files = [
            filename
            for filename in all_files(Path(output_dir).joinpath("exomiser_batch_files"))
            if filename.name.startswith(run.run_identifier)
        ]
        exomiser_config_path = run.path_to_exomiser_software_directory.joinpath("application.properties")
        exomiser_jar_file = [
            filename
            for filename in all_files(run.path_to_exomiser_software_directory)
            if filename.name.endswith(".jar")
        ][0]
        exomiser_jar_file_path = run.path_to_exomiser_software_directory.joinpath(exomiser_jar_file)
        for file in prefixed_batch_files:
            subprocess.run(
                [
                    "/usr/bin/java",
                    "-Xmx4g",
                    "-jar",
                    exomiser_jar_file_path,
                    "--batch",
                    file,
                    f"--spring.config.location={exomiser_config_path}",
                ],
                shell=False,
            )
        os.rename(Path(output_dir).joinpath("results"), Path(output_dir).joinpath(run.run_identifier + "_results"))


def create_docker_run_command(output_dir: Path, run: ExomiserConfigSingleRun, batch_file: Path):
    docker_mounts = mount_docker(output_dir, run)
    exomiser_config_params = exomiser_config_parameters(run)
    if exomiser_config_params.application_properties_path is None:
        return [
            "docker",
            "run",
            "-v",
            docker_mounts.exomiser_data_dir,
            "-v",
            docker_mounts.phenopacket_test_data,
            "-v",
            docker_mounts.vcf_test_data,
            "-v",
            docker_mounts.batch_file_path,
            "-v",
            docker_mounts.exomiser_yaml,
            f"exomiser/exomiser-cli:{run.exomiser_configurations.exomiser_version}"
            "--batch",
            "/exomiser-batch-file/" + batch_file.name,
            f"--exomiser.data-directory=/exomiser-data"
            f"--exomiser.hg19.data-version={exomiser_config_params.exomiser_hg19_version}",
            f"--exomiser.hg38.data-version={exomiser_config_params.exomiser_hg38_version}",
            f"--exomiser.phenotype.data-version={exomiser_config_params.exomiser_phenotype_version}",
        ]
    else:
        return [
            "docker",
            "run",
            "-v",
            docker_mounts.exomiser_data_dir,
            "-v",
            f'"{exomiser_config_params.application_properties_path}{os.sep}:/exomiser-config"',
            "-v",
            docker_mounts.phenopacket_test_data,
            "-v",
            docker_mounts.vcf_test_data,
            "-v",
            docker_mounts.batch_file_path,
            "-v",
            docker_mounts.exomiser_yaml,
            f"exomiser/exomiser-cli:{run.exomiser_configurations.exomiser_version}",
            "--batch",
            "/exomiser-batch-file/" + batch_file.name,
            f"--spring.config.location=/exomiser-config/application.properties",
        ]


def run_exomiser_docker(output_dir: Path, config: ExomiserConfig):
    print("...running exomiser...")
    os.chdir(output_dir)
    for run in config.run.runs:
        edit_application_properties_data_path_for_exomiser(run)
        prefixed_batch_files = [
            filename
            for filename in all_files(Path(output_dir).joinpath("exomiser_batch_files"))
            if filename.name.startswith(run.run_identifier)
        ]
        for file in prefixed_batch_files:
            docker_command = create_docker_run_command(output_dir, run, file)
            subprocess.run(
                " ".join(docker_command),
                shell=True,
            )
        os.rename(Path(output_dir).joinpath("results"), Path(output_dir).joinpath(run.run_identifier + "_results"))


def run_exomiser(output_dir: Path, config: ExomiserConfig):
    run_exomiser_local(output_dir, config) if config.run.environment == "local" else run_exomiser_docker(output_dir,
                                                                                                         config)
