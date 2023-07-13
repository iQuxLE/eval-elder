# Exomiser Runner for PhEval

This is the Exomiser plugin for PhEval. Documentation on how to set up and run the PhEval pipeline with the Exomiser runner is detailed [here](https://monarch-initiative.github.io/pheval/exomiser_pipeline/).

## Configuring a run:

### Setting up the input directory

A `config.yaml` should be located in the input directory and formatted like so:

```yaml
tool: exomiser
tool_version: 13.2.0
phenotype_only: False # NOTE phenotype-only preset analysis should only be run with Exomiser versions >= 13.2.0
tool_specific_configuration_options:
  environment: local
  exomiser_software_directory: exomiser-cli-13.2.0
  analysis_configuration_file: preset-exome-analysis.yml
  max_jobs: 0
  application_properties:
    remm_version:
    cadd_version:
    hg19_data_version: 2302
    hg19_local_frequency_path: # name of hg19 local frequency file 
    hg38_data_version: 2302
    hg38_local_frequency_path: # name of hg38 local frequency file 
    phenotype_data_version: 2302
    cache_type:
    cache_caffeine_spec:
  post_process:
    score_name: combinedScore
    sort_order: DESCENDING
```
The bare minimum fields are filled to give an idea on the requirements. This is so that the application.properties for Exomiser can be correctly configured. An example config has been provided `pheval.exomiser/config.yaml`.

The Exomiser input data directories (phenotype and variant) should also be located in the input directory - or a symlink pointing to the location.

The `exomiser_software_directory` points to the name of the Exomiser distribution directory located in the input directory.

The analysis configuration file (in this case: `preset-exome-analysis.yml` should be located within the input directory.

If using optional databases, such as REMM/CADD/local frequency the optional data input should look like so in the input
directory:

```tree
├── cadd
│   └── {{CADD-VERSION}}
│       ├── hg19
│       │   ├── InDels.tsv.gz
│       │   └── whole_genome_SNVs.tsv.gz
│       └── hg38
│           ├── InDels.tsv.gz
│           └── whole_genome_SNVs.tsv.gz
├── local
│   ├── local_frequency_test_hg19.tsv.gz
│   └── local_frequency_test_hg38.tsv.gz
└── remm
    ├── ReMM.v{{REMM-VERSION}}.hg19.tsv.gz
    └── ReMM.v{{REMM-VERSION}}.hg38.tsv.gz
```


The overall structure of the input directory may look something like this (omitting some files for clarity):
```tree

    
.
├── 2302_hg19
│   ├── 2302_hg19_clinvar_whitelist.tsv.gz
│   ├── 2302_hg19_clinvar_whitelist.tsv.gz.tbi
│   ├── 2302_hg19_genome.h2.db
│   ├── 2302_hg19_transcripts_ensembl.ser
│   ├── 2302_hg19_transcripts_refseq.ser
│   ├── 2302_hg19_transcripts_ucsc.ser
│   └── 2302_hg19_variants.mv.db
├── 2302_phenotype
│   ├── 2302_phenotype.h2.db
│   ├── hp.obo
│   ├── phenix
│   │   ├── ALL_SOURCES_ALL_FREQUENCIES_genes_to_phenotype.txt
│   │   ├── hp.obo
│   │   └── out
│   └── rw_string_10.mv
├── config.yaml
├── exomiser-cli-13.2.0
│   ├── lib
│   └── exomiser-cli-13.2.0.jar
├── preset-exome-analysis.yml
├── cadd
│   └── {{CADD-VERSION}}
│       ├── hg19
│       │   ├── InDels.tsv.gz
│       │   └── whole_genome_SNVs.tsv.gz
│       └── hg38
│           ├── InDels.tsv.gz
│           └── whole_genome_SNVs.tsv.gz
├── exomiser-cli-13.2.0
│   ├── exomiser-cli-13.2.0.jar
│   └── local_frequency_test_hg38.tsv.gz
├── local
│   ├── local_frequency_test_hg19.tsv.gz
│   └── local_frequency_test_hg38.tsv.gz
└── remm
    ├── ReMM.v{{REMM-VERSION}}.hg19.tsv.gz
    └── ReMM.v{{REMM-VERSION}}.hg38.tsv.gz
```
### Setting up the testdata directory

The Exomiser plugin for PhEval accepts phenopackets and vcf files as an input for running Exomiser. The plugin can be run in `phenotype_only` mode, where only phenopackets are required as an input, however, this *must* be specified in the `config.yaml`.

The testdata directory should include subdirectories named `phenopackets` and `vcf` if running with variant prioritisation.

e.g., 

```tree
├── testdata_dir
   ├── phenopackets
   └── vcf
```

## Run command

Once the testdata and input directories are correctly configured for the run, the `pheval run` command can be executed.

```bash
pheval run --input-dir /path/to/input_dir \
--testdata-dir /path/to/testdata_dir \
--runner exomiserphevalrunner \
--output-dir /path/to/output_dir \
--version 13.2.0
```

## Common errors

You may see an error that is related to the current `setuptools` being used:

```shell
pkg_resources.extern.packaging.requirements.InvalidRequirement: Expected closing RIGHT_PARENTHESIS
    requests (<3,>=2.12.*) ; extra == 'parse'
             ~~~~~~~~~~^
```

To fix the error, `setuptools` needs to be downgraded to version 66:

```shell
pip uninstall setuptools
pip install -U setuptools=="66"
```