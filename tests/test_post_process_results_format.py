import dataclasses
import unittest

from pheval.utils.phenopacket_utils import VariantData

from pheval_exomiser.post_process.post_process_results_format import (
    RankExomiserResult,
    SimplifiedExomiserGeneResult,
    SimplifiedExomiserVariantResult,
    StandardiseExomiserResult,
)

example_exomiser_result = [
    {
        "geneSymbol": "PLXNA1",
        "geneIdentifier": {
            "geneId": "ENSG00000114554",
            "geneSymbol": "PLXNA1",
            "hgncId": "HGNC:9099",
            "hgncSymbol": "PLXNA1",
            "entrezId": "5361",
            "ensemblId": "ENSG00000114554",
            "ucscId": "uc003ejg.3",
        },
        "combinedScore": 0.048419416654489886,
        "priorityScore": 0.500087835782324,
        "variantScore": 0.5566032528877258,
        "pValue": 0.18761854103343464,
        "priorityResults": {
            "HIPHIVE_PRIORITY": {
                "priorityType": "HIPHIVE_PRIORITY",
                "geneId": 5361,
                "geneSymbol": "PLXNA1",
                "score": 0.500087835782324,
                "ppiScore": 0.500087835782324,
                "queryPhenotypeTerms": [
                    {"id": "HP:0000256", "label": "Macrocephaly"},
                    {"id": "HP:0002059", "label": "Cerebral atrophy"},
                    {"id": "HP:0100309", "label": "Subdural hemorrhage"},
                    {"id": "HP:0003150", "label": "Glutaric aciduria"},
                    {"id": "HP:0001332", "label": "Dystonia"},
                ],
                "phenotypeEvidence": [
                    {
                        "score": 0.2201534815163801,
                        "model": {
                            "organism": "MOUSE",
                            "entrezGeneId": 5361,
                            "humanGeneSymbol": "PLXNA1",
                            "modelGeneId": "MGI:107685",
                            "modelGeneSymbol": "Plxna1",
                            "phenotypeIds": ["MP:0000953"],
                            "id": "MGI:107685_MGI:3831891",
                        },
                        "bestModelPhenotypeMatches": [
                            {
                                "query": {"id": "HP:0002059", "label": "Cerebral atrophy"},
                                "match": {
                                    "id": "MP:0000953",
                                    "label": "abnormal oligodendrocyte morphology",
                                },
                                "lcs": {
                                    "id": "HP:0002011",
                                    "label": "Morphological central nervous system abnormality",
                                },
                                "ic": 2.564961484335766,
                                "simj": 0.3076923076923077,
                                "score": 0.888379940260449,
                            },
                            {
                                "query": {"id": "HP:0100309", "label": "Subdural hemorrhage"},
                                "match": {
                                    "id": "MP:0000953",
                                    "label": "abnormal oligodendrocyte morphology",
                                },
                                "lcs": {
                                    "id": "HP:0002011",
                                    "label": "Morphological central nervous system abnormality",
                                },
                                "ic": 2.564961484335766,
                                "simj": 0.2222222222222222,
                                "score": 0.7549777751454035,
                            },
                        ],
                    }
                ],
                "ppiEvidence": [
                    {
                        "score": 0.37302057935946703,
                        "model": {
                            "organism": "HUMAN",
                            "disease": {
                                "diseaseId": "ORPHA:33001",
                                "diseaseName": "Lymphedema-distichiasis syndrome",
                                "associatedGeneId": 2303,
                                "diseaseType": "DISEASE",
                                "inheritanceMode": "AUTOSOMAL_DOMINANT",
                                "phenotypeIds": [
                                    "HP:0000010",
                                    "HP:0000075",
                                    "HP:0000093",
                                    "HP:0000175",
                                    "HP:0000204",
                                    "HP:0000465",
                                    "HP:0000508",
                                    "HP:0000509",
                                    "HP:0000518",
                                    "HP:0000613",
                                    "HP:0000656",
                                    "HP:0000819",
                                    "HP:0001324",
                                    "HP:0001581",
                                    "HP:0001643",
                                    "HP:0001970",
                                    "HP:0002619",
                                    "HP:0003550",
                                    "HP:0004930",
                                    "HP:0009743",
                                    "HP:0009745",
                                    "HP:0011675",
                                    "HP:0100244",
                                    "HP:0100820",
                                    "HP:0200020",
                                ],
                                "id": "ORPHA:33001",
                                "associatedGeneSymbol": "FOXC2",
                            },
                            "entrezGeneId": 2303,
                            "humanGeneSymbol": "FOXC2",
                            "diseaseId": "ORPHA:33001",
                            "diseaseTerm": "Lymphedema-distichiasis syndrome",
                            "phenotypeIds": [
                                "HP:0000010",
                                "HP:0000075",
                                "HP:0000093",
                                "HP:0000175",
                                "HP:0000204",
                                "HP:0000465",
                                "HP:0000508",
                                "HP:0000509",
                                "HP:0000518",
                                "HP:0000613",
                                "HP:0000656",
                                "HP:0000819",
                                "HP:0001324",
                                "HP:0001581",
                                "HP:0001643",
                                "HP:0001970",
                                "HP:0002619",
                                "HP:0003550",
                                "HP:0004930",
                                "HP:0009743",
                                "HP:0009745",
                                "HP:0011675",
                                "HP:0100244",
                                "HP:0100820",
                                "HP:0200020",
                            ],
                            "id": "ORPHA:33001_2303",
                        },
                        "bestModelPhenotypeMatches": [
                            {
                                "query": {"id": "HP:0003150", "label": "Glutaric aciduria"},
                                "match": {"id": "HP:0000093", "label": "Proteinuria"},
                                "lcs": {
                                    "id": "HP:0033354",
                                    "label": "Abnormal urine metabolite level",
                                },
                                "ic": 4.187537448397988,
                                "simj": 0.5555555555555556,
                                "score": 1.5252572548768413,
                            },
                            {
                                "query": {"id": "HP:0100309", "label": "Subdural hemorrhage"},
                                "match": {"id": "HP:0002619", "label": "Varicose veins"},
                                "lcs": {
                                    "id": "HP:0025015",
                                    "label": "Abnormal vascular morphology",
                                },
                                "ic": 2.9688246275384604,
                                "simj": 0.25,
                                "score": 0.8615138750389427,
                            },
                        ],
                    },
                    {
                        "score": 0.6557657231285885,
                        "model": {
                            "organism": "MOUSE",
                            "entrezGeneId": 2303,
                            "humanGeneSymbol": "FOXC2",
                            "modelGeneId": "MGI:1347481",
                            "modelGeneSymbol": "Foxc2",
                            "phenotypeIds": [
                                "MP:0000029",
                                "MP:0000111",
                                "MP:0000141",
                                "MP:0000154",
                                "MP:0000163",
                                "MP:0000431",
                                "MP:0001614",
                                "MP:0001691",
                                "MP:0001915",
                                "MP:0002400",
                                "MP:0002989",
                                "MP:0003345",
                                "MP:0003400",
                                "MP:0004204",
                                "MP:0004318",
                                "MP:0004384",
                                "MP:0004443",
                                "MP:0004445",
                                "MP:0004447",
                                "MP:0004449",
                                "MP:0004456",
                                "MP:0004476",
                                "MP:0004592",
                                "MP:0004599",
                                "MP:0005105",
                                "MP:0005587",
                                "MP:0006020",
                                "MP:0006054",
                                "MP:0008380",
                                "MP:0011108",
                                "MP:0030026",
                                "MP:0030121",
                            ],
                            "id": "MGI:1347481_MGI:2170157",
                        },
                        "bestModelPhenotypeMatches": [
                            {
                                "query": {"id": "HP:0000256", "label": "Macrocephaly"},
                                "match": {"id": "MP:0004384", "label": "small interparietal bone"},
                                "lcs": {"id": "MP:0000438", "label": "abnormal cranium morphology"},
                                "ic": 2.555277672562376,
                                "simj": 0.68,
                                "score": 1.3181763225541625,
                            },
                            {
                                "query": {"id": "HP:0002059", "label": "Cerebral atrophy"},
                                "match": {"id": "MP:0003400", "label": "kinked neural tube"},
                                "lcs": {
                                    "id": "HP:0002011",
                                    "label": "Morphological central nervous system abnormality",
                                },
                                "ic": 2.564961484335766,
                                "simj": 0.32,
                                "score": 0.9059733301744842,
                            },
                            {
                                "query": {"id": "HP:0003150", "label": "Glutaric aciduria"},
                                "match": {"id": "MP:0002989", "label": "small kidney"},
                                "lcs": {
                                    "id": "HP:0000079",
                                    "label": "Abnormality of the urinary system",
                                },
                                "ic": 3.4863678415566968,
                                "simj": 0.23333333333333334,
                                "score": 0.9019344930185133,
                            },
                            {
                                "query": {"id": "HP:0100309", "label": "Subdural hemorrhage"},
                                "match": {"id": "MP:0001915", "label": "intracranial hemorrhage"},
                                "lcs": {"id": "MP:0001915", "label": "intracranial hemorrhage"},
                                "ic": 7.415808888728614,
                                "simj": 0.9655172413793104,
                                "score": 2.675834699835067,
                            },
                        ],
                    },
                ],
                "mouseScore": 0.2201534815163801,
            },
            "OMIM_PRIORITY": {
                "priorityType": "OMIM_PRIORITY",
                "geneId": 5361,
                "geneSymbol": "PLXNA1",
                "score": 1.0,
                "scoresByMode": {
                    "AUTOSOMAL_DOMINANT": 1.0,
                    "AUTOSOMAL_RECESSIVE": 1.0,
                    "X_RECESSIVE": 0.5,
                    "X_DOMINANT": 0.5,
                    "MITOCHONDRIAL": 0.5,
                },
            },
        },
        "compatibleInheritanceModes": ["AUTOSOMAL_DOMINANT", "AUTOSOMAL_RECESSIVE"],
        "geneScores": [
            {
                "geneIdentifier": {
                    "geneId": "ENSG00000114554",
                    "geneSymbol": "PLXNA1",
                    "hgncId": "HGNC:9099",
                    "hgncSymbol": "PLXNA1",
                    "entrezId": "5361",
                    "ensemblId": "ENSG00000114554",
                    "ucscId": "uc003ejg.3",
                },
                "modeOfInheritance": "AUTOSOMAL_DOMINANT",
                "combinedScore": 0.048419416654489886,
                "phenotypeScore": 0.500087835782324,
                "variantScore": 0.5566032528877258,
                "pValue": 0.18761854103343464,
                "contributingVariants": [
                    {
                        "genomeAssembly": "HG19",
                        "contigName": "3",
                        "start": 126730873,
                        "end": 126730873,
                        "ref": "G",
                        "alt": "A",
                        "id": "rs78052417",
                        "type": "SNV",
                        "length": 1,
                        "phredScore": 2970.4399999999996,
                        "variantEffect": "MISSENSE_VARIANT",
                        "filterStatus": "PASSED",
                        "contributesToGeneScore": True,
                        "variantScore": 0.55660325,
                        "frequencyScore": 0.9972702,
                        "pathogenicityScore": 0.5581268,
                        "predictedPathogenic": True,
                        "passedFilterTypes": [
                            "FAILED_VARIANT_FILTER",
                            "PATHOGENICITY_FILTER",
                            "FREQUENCY_FILTER",
                            "VARIANT_EFFECT_FILTER",
                            "INHERITANCE_FILTER",
                        ],
                        "frequencyData": {
                            "rsId": "rs78052417",
                            "knownFrequencies": [
                                {"source": "THOUSAND_GENOMES", "frequency": 0.01997},
                                {"source": "TOPMED", "frequency": 0.001133},
                                {"source": "EXAC_NON_FINNISH_EUROPEAN", "frequency": 0.004534462},
                                {"source": "GNOMAD_E_NFE", "frequency": 0.0035905354},
                            ],
                            "score": 0.9972702,
                        },
                        "pathogenicityData": {
                            "clinVarData": {"primaryInterpretation": "NOT_PROVIDED"},
                            "mostPathogenicScore": {"source": "MVP", "score": 0.5581268},
                            "score": 0.5581268,
                            "predictedPathogenicityScores": [
                                {"source": "REVEL", "score": 0.348},
                                {"source": "MVP", "score": 0.5581268},
                            ],
                        },
                        "compatibleInheritanceModes": ["AUTOSOMAL_DOMINANT", "AUTOSOMAL_RECESSIVE"],
                        "contributingInheritanceModes": [
                            "AUTOSOMAL_DOMINANT",
                            "AUTOSOMAL_RECESSIVE",
                        ],
                        "transcriptAnnotations": [
                            {
                                "variantEffect": "MISSENSE_VARIANT",
                                "geneSymbol": "PLXNA1",
                                "accession": "ENST00000251772.4",
                                "hgvsGenomic": "g.126730873G>A",
                                "hgvsCdna": "c.2116G>A",
                                "hgvsProtein": "p.(Ala706Thr)",
                                "rankType": "EXON",
                                "rank": 9,
                                "rankTotal": 31,
                            },
                            {
                                "variantEffect": "MISSENSE_VARIANT",
                                "geneSymbol": "PLXNA1",
                                "accession": "ENST00000393409.2",
                                "hgvsGenomic": "g.126730873G>A",
                                "hgvsCdna": "c.2185G>A",
                                "hgvsProtein": "p.(Ala729Thr)",
                                "rankType": "EXON",
                                "rank": 9,
                                "rankTotal": 31,
                            },
                        ],
                    }
                ],
                "acmgAssignments": [
                    {
                        "variantEvaluation": {
                            "genomeAssembly": "HG19",
                            "contigName": "3",
                            "start": 126730873,
                            "end": 126730873,
                            "ref": "G",
                            "alt": "A",
                            "id": "rs78052417",
                            "type": "SNV",
                            "length": 1,
                            "phredScore": 2970.4399999999996,
                            "variantEffect": "MISSENSE_VARIANT",
                            "filterStatus": "PASSED",
                            "contributesToGeneScore": True,
                            "variantScore": 0.55660325,
                            "frequencyScore": 0.9972702,
                            "pathogenicityScore": 0.5581268,
                            "predictedPathogenic": True,
                            "passedFilterTypes": [
                                "FAILED_VARIANT_FILTER",
                                "PATHOGENICITY_FILTER",
                                "FREQUENCY_FILTER",
                                "VARIANT_EFFECT_FILTER",
                                "INHERITANCE_FILTER",
                            ],
                            "frequencyData": {
                                "rsId": "rs78052417",
                                "knownFrequencies": [
                                    {"source": "THOUSAND_GENOMES", "frequency": 0.01997},
                                    {"source": "TOPMED", "frequency": 0.001133},
                                    {
                                        "source": "EXAC_NON_FINNISH_EUROPEAN",
                                        "frequency": 0.004534462,
                                    },
                                    {"source": "GNOMAD_E_NFE", "frequency": 0.0035905354},
                                ],
                                "score": 0.9972702,
                            },
                            "pathogenicityData": {
                                "clinVarData": {"primaryInterpretation": "NOT_PROVIDED"},
                                "mostPathogenicScore": {"source": "MVP", "score": 0.5581268},
                                "score": 0.5581268,
                                "predictedPathogenicityScores": [
                                    {"source": "REVEL", "score": 0.348},
                                    {"source": "MVP", "score": 0.5581268},
                                ],
                            },
                            "compatibleInheritanceModes": [
                                "AUTOSOMAL_DOMINANT",
                                "AUTOSOMAL_RECESSIVE",
                            ],
                            "contributingInheritanceModes": [
                                "AUTOSOMAL_DOMINANT",
                                "AUTOSOMAL_RECESSIVE",
                            ],
                            "transcriptAnnotations": [
                                {
                                    "variantEffect": "MISSENSE_VARIANT",
                                    "geneSymbol": "PLXNA1",
                                    "accession": "ENST00000251772.4",
                                    "hgvsGenomic": "g.126730873G>A",
                                    "hgvsCdna": "c.2116G>A",
                                    "hgvsProtein": "p.(Ala706Thr)",
                                    "rankType": "EXON",
                                    "rank": 9,
                                    "rankTotal": 31,
                                },
                                {
                                    "variantEffect": "MISSENSE_VARIANT",
                                    "geneSymbol": "PLXNA1",
                                    "accession": "ENST00000393409.2",
                                    "hgvsGenomic": "g.126730873G>A",
                                    "hgvsCdna": "c.2185G>A",
                                    "hgvsProtein": "p.(Ala729Thr)",
                                    "rankType": "EXON",
                                    "rank": 9,
                                    "rankTotal": 31,
                                },
                            ],
                        },
                        "geneIdentifier": {
                            "geneId": "ENSG00000114554",
                            "geneSymbol": "PLXNA1",
                            "hgncId": "HGNC:9099",
                            "hgncSymbol": "PLXNA1",
                            "entrezId": "5361",
                            "ensemblId": "ENSG00000114554",
                            "ucscId": "uc003ejg.3",
                        },
                        "modeOfInheritance": "AUTOSOMAL_DOMINANT",
                        "disease": {"diseaseType": "UNCONFIRMED", "inheritanceMode": "UNKNOWN"},
                        "acmgEvidence": {"empty": True},
                        "acmgClassification": "UNCERTAIN_SIGNIFICANCE",
                    }
                ],
            },
            {
                "geneIdentifier": {
                    "geneId": "ENSG00000114554",
                    "geneSymbol": "PLXNA1",
                    "hgncId": "HGNC:9099",
                    "hgncSymbol": "PLXNA1",
                    "entrezId": "5361",
                    "ensemblId": "ENSG00000114554",
                    "ucscId": "uc003ejg.3",
                },
                "modeOfInheritance": "AUTOSOMAL_RECESSIVE",
                "combinedScore": 0.04598293574097189,
                "phenotypeScore": 0.500087835782324,
                "variantScore": 0.5507028996944427,
                "pValue": 0.19066565349544073,
                "contributingVariants": [
                    {
                        "genomeAssembly": "HG19",
                        "contigName": "3",
                        "start": 126730873,
                        "end": 126730873,
                        "ref": "G",
                        "alt": "A",
                        "id": "rs78052417",
                        "type": "SNV",
                        "length": 1,
                        "phredScore": 2970.4399999999996,
                        "variantEffect": "MISSENSE_VARIANT",
                        "filterStatus": "PASSED",
                        "contributesToGeneScore": True,
                        "variantScore": 0.55660325,
                        "frequencyScore": 0.9972702,
                        "pathogenicityScore": 0.5581268,
                        "predictedPathogenic": True,
                        "passedFilterTypes": [
                            "FAILED_VARIANT_FILTER",
                            "PATHOGENICITY_FILTER",
                            "FREQUENCY_FILTER",
                            "VARIANT_EFFECT_FILTER",
                            "INHERITANCE_FILTER",
                        ],
                        "frequencyData": {
                            "rsId": "rs78052417",
                            "knownFrequencies": [
                                {"source": "THOUSAND_GENOMES", "frequency": 0.01997},
                                {"source": "TOPMED", "frequency": 0.001133},
                                {"source": "EXAC_NON_FINNISH_EUROPEAN", "frequency": 0.004534462},
                                {"source": "GNOMAD_E_NFE", "frequency": 0.0035905354},
                            ],
                            "score": 0.9972702,
                        },
                        "pathogenicityData": {
                            "clinVarData": {"primaryInterpretation": "NOT_PROVIDED"},
                            "mostPathogenicScore": {"source": "MVP", "score": 0.5581268},
                            "score": 0.5581268,
                            "predictedPathogenicityScores": [
                                {"source": "REVEL", "score": 0.348},
                                {"source": "MVP", "score": 0.5581268},
                            ],
                        },
                        "compatibleInheritanceModes": ["AUTOSOMAL_DOMINANT", "AUTOSOMAL_RECESSIVE"],
                        "contributingInheritanceModes": [
                            "AUTOSOMAL_DOMINANT",
                            "AUTOSOMAL_RECESSIVE",
                        ],
                        "transcriptAnnotations": [
                            {
                                "variantEffect": "MISSENSE_VARIANT",
                                "geneSymbol": "PLXNA1",
                                "accession": "ENST00000251772.4",
                                "hgvsGenomic": "g.126730873G>A",
                                "hgvsCdna": "c.2116G>A",
                                "hgvsProtein": "p.(Ala706Thr)",
                                "rankType": "EXON",
                                "rank": 9,
                                "rankTotal": 31,
                            },
                            {
                                "variantEffect": "MISSENSE_VARIANT",
                                "geneSymbol": "PLXNA1",
                                "accession": "ENST00000393409.2",
                                "hgvsGenomic": "g.126730873G>A",
                                "hgvsCdna": "c.2185G>A",
                                "hgvsProtein": "p.(Ala729Thr)",
                                "rankType": "EXON",
                                "rank": 9,
                                "rankTotal": 31,
                            },
                        ],
                    },
                    {
                        "genomeAssembly": "HG19",
                        "contigName": "3",
                        "start": 126741108,
                        "end": 126741108,
                        "ref": "G",
                        "alt": "A",
                        "id": "rs73196567",
                        "type": "SNV",
                        "length": 1,
                        "phredScore": 3055.4399999999996,
                        "variantEffect": "MISSENSE_VARIANT",
                        "filterStatus": "PASSED",
                        "contributesToGeneScore": True,
                        "variantScore": 0.54480255,
                        "frequencyScore": 0.98371375,
                        "pathogenicityScore": 0.5538222,
                        "predictedPathogenic": True,
                        "passedFilterTypes": [
                            "FAILED_VARIANT_FILTER",
                            "PATHOGENICITY_FILTER",
                            "FREQUENCY_FILTER",
                            "VARIANT_EFFECT_FILTER",
                            "INHERITANCE_FILTER",
                        ],
                        "frequencyData": {
                            "rsId": "rs73196567",
                            "knownFrequencies": [
                                {"source": "THOUSAND_GENOMES", "frequency": 0.01997},
                                {"source": "TOPMED", "frequency": 0.002267},
                                {"source": "EXAC_EAST_ASIAN", "frequency": 0.0116198},
                                {"source": "EXAC_NON_FINNISH_EUROPEAN", "frequency": 0.0015265311},
                                {"source": "EXAC_OTHER", "frequency": 0.11363637},
                                {"source": "EXAC_SOUTH_ASIAN", "frequency": 0.0060716453},
                                {"source": "GNOMAD_E_EAS", "frequency": 0.01740543},
                                {"source": "GNOMAD_E_NFE", "frequency": 0.0017979468},
                                {"source": "GNOMAD_E_SAS", "frequency": 0.00325013},
                            ],
                            "score": 0.98371375,
                        },
                        "pathogenicityData": {
                            "clinVarData": {"primaryInterpretation": "NOT_PROVIDED"},
                            "mostPathogenicScore": {"source": "MVP", "score": 0.5538222},
                            "score": 0.5538222,
                            "predictedPathogenicityScores": [
                                {"source": "REVEL", "score": 0.301},
                                {"source": "MVP", "score": 0.5538222},
                            ],
                        },
                        "compatibleInheritanceModes": ["AUTOSOMAL_RECESSIVE"],
                        "contributingInheritanceModes": ["AUTOSOMAL_RECESSIVE"],
                        "transcriptAnnotations": [
                            {
                                "variantEffect": "MISSENSE_VARIANT",
                                "geneSymbol": "PLXNA1",
                                "accession": "ENST00000251772.4",
                                "hgvsGenomic": "g.126741108G>A",
                                "hgvsCdna": "c.4150G>A",
                                "hgvsProtein": "p.(Val1384Met)",
                                "rankType": "EXON",
                                "rank": 21,
                                "rankTotal": 31,
                            },
                            {
                                "variantEffect": "MISSENSE_VARIANT",
                                "geneSymbol": "PLXNA1",
                                "accession": "ENST00000393409.2",
                                "hgvsGenomic": "g.126741108G>A",
                                "hgvsCdna": "c.4219G>A",
                                "hgvsProtein": "p.(Val1407Met)",
                                "rankType": "EXON",
                                "rank": 21,
                                "rankTotal": 31,
                            },
                        ],
                    },
                ],
                "acmgAssignments": [
                    {
                        "variantEvaluation": {
                            "genomeAssembly": "HG19",
                            "contigName": "3",
                            "start": 126730873,
                            "end": 126730873,
                            "ref": "G",
                            "alt": "A",
                            "id": "rs78052417",
                            "type": "SNV",
                            "length": 1,
                            "phredScore": 2970.4399999999996,
                            "variantEffect": "MISSENSE_VARIANT",
                            "filterStatus": "PASSED",
                            "contributesToGeneScore": True,
                            "variantScore": 0.55660325,
                            "frequencyScore": 0.9972702,
                            "pathogenicityScore": 0.5581268,
                            "predictedPathogenic": True,
                            "passedFilterTypes": [
                                "FAILED_VARIANT_FILTER",
                                "PATHOGENICITY_FILTER",
                                "FREQUENCY_FILTER",
                                "VARIANT_EFFECT_FILTER",
                                "INHERITANCE_FILTER",
                            ],
                            "frequencyData": {
                                "rsId": "rs78052417",
                                "knownFrequencies": [
                                    {"source": "THOUSAND_GENOMES", "frequency": 0.01997},
                                    {"source": "TOPMED", "frequency": 0.001133},
                                    {
                                        "source": "EXAC_NON_FINNISH_EUROPEAN",
                                        "frequency": 0.004534462,
                                    },
                                    {"source": "GNOMAD_E_NFE", "frequency": 0.0035905354},
                                ],
                                "score": 0.9972702,
                            },
                            "pathogenicityData": {
                                "clinVarData": {"primaryInterpretation": "NOT_PROVIDED"},
                                "mostPathogenicScore": {"source": "MVP", "score": 0.5581268},
                                "score": 0.5581268,
                                "predictedPathogenicityScores": [
                                    {"source": "REVEL", "score": 0.348},
                                    {"source": "MVP", "score": 0.5581268},
                                ],
                            },
                            "compatibleInheritanceModes": [
                                "AUTOSOMAL_DOMINANT",
                                "AUTOSOMAL_RECESSIVE",
                            ],
                            "contributingInheritanceModes": [
                                "AUTOSOMAL_DOMINANT",
                                "AUTOSOMAL_RECESSIVE",
                            ],
                            "transcriptAnnotations": [
                                {
                                    "variantEffect": "MISSENSE_VARIANT",
                                    "geneSymbol": "PLXNA1",
                                    "accession": "ENST00000251772.4",
                                    "hgvsGenomic": "g.126730873G>A",
                                    "hgvsCdna": "c.2116G>A",
                                    "hgvsProtein": "p.(Ala706Thr)",
                                    "rankType": "EXON",
                                    "rank": 9,
                                    "rankTotal": 31,
                                },
                                {
                                    "variantEffect": "MISSENSE_VARIANT",
                                    "geneSymbol": "PLXNA1",
                                    "accession": "ENST00000393409.2",
                                    "hgvsGenomic": "g.126730873G>A",
                                    "hgvsCdna": "c.2185G>A",
                                    "hgvsProtein": "p.(Ala729Thr)",
                                    "rankType": "EXON",
                                    "rank": 9,
                                    "rankTotal": 31,
                                },
                            ],
                        },
                        "geneIdentifier": {
                            "geneId": "ENSG00000114554",
                            "geneSymbol": "PLXNA1",
                            "hgncId": "HGNC:9099",
                            "hgncSymbol": "PLXNA1",
                            "entrezId": "5361",
                            "ensemblId": "ENSG00000114554",
                            "ucscId": "uc003ejg.3",
                        },
                        "modeOfInheritance": "AUTOSOMAL_RECESSIVE",
                        "disease": {"diseaseType": "UNCONFIRMED", "inheritanceMode": "UNKNOWN"},
                        "acmgEvidence": {"empty": True},
                        "acmgClassification": "UNCERTAIN_SIGNIFICANCE",
                    },
                    {
                        "variantEvaluation": {
                            "genomeAssembly": "HG19",
                            "contigName": "3",
                            "start": 126741108,
                            "end": 126741108,
                            "ref": "G",
                            "alt": "A",
                            "id": "rs73196567",
                            "type": "SNV",
                            "length": 1,
                            "phredScore": 3055.4399999999996,
                            "variantEffect": "MISSENSE_VARIANT",
                            "filterStatus": "PASSED",
                            "contributesToGeneScore": True,
                            "variantScore": 0.54480255,
                            "frequencyScore": 0.98371375,
                            "pathogenicityScore": 0.5538222,
                            "predictedPathogenic": True,
                            "passedFilterTypes": [
                                "FAILED_VARIANT_FILTER",
                                "PATHOGENICITY_FILTER",
                                "FREQUENCY_FILTER",
                                "VARIANT_EFFECT_FILTER",
                                "INHERITANCE_FILTER",
                            ],
                            "frequencyData": {
                                "rsId": "rs73196567",
                                "knownFrequencies": [
                                    {"source": "THOUSAND_GENOMES", "frequency": 0.01997},
                                    {"source": "TOPMED", "frequency": 0.002267},
                                    {"source": "EXAC_EAST_ASIAN", "frequency": 0.0116198},
                                    {
                                        "source": "EXAC_NON_FINNISH_EUROPEAN",
                                        "frequency": 0.0015265311,
                                    },
                                    {"source": "EXAC_OTHER", "frequency": 0.11363637},
                                    {"source": "EXAC_SOUTH_ASIAN", "frequency": 0.0060716453},
                                    {"source": "GNOMAD_E_EAS", "frequency": 0.01740543},
                                    {"source": "GNOMAD_E_NFE", "frequency": 0.0017979468},
                                    {"source": "GNOMAD_E_SAS", "frequency": 0.00325013},
                                ],
                                "score": 0.98371375,
                            },
                            "pathogenicityData": {
                                "clinVarData": {"primaryInterpretation": "NOT_PROVIDED"},
                                "mostPathogenicScore": {"source": "MVP", "score": 0.5538222},
                                "score": 0.5538222,
                                "predictedPathogenicityScores": [
                                    {"source": "REVEL", "score": 0.301},
                                    {"source": "MVP", "score": 0.5538222},
                                ],
                            },
                            "compatibleInheritanceModes": ["AUTOSOMAL_RECESSIVE"],
                            "contributingInheritanceModes": ["AUTOSOMAL_RECESSIVE"],
                            "transcriptAnnotations": [
                                {
                                    "variantEffect": "MISSENSE_VARIANT",
                                    "geneSymbol": "PLXNA1",
                                    "accession": "ENST00000251772.4",
                                    "hgvsGenomic": "g.126741108G>A",
                                    "hgvsCdna": "c.4150G>A",
                                    "hgvsProtein": "p.(Val1384Met)",
                                    "rankType": "EXON",
                                    "rank": 21,
                                    "rankTotal": 31,
                                },
                                {
                                    "variantEffect": "MISSENSE_VARIANT",
                                    "geneSymbol": "PLXNA1",
                                    "accession": "ENST00000393409.2",
                                    "hgvsGenomic": "g.126741108G>A",
                                    "hgvsCdna": "c.4219G>A",
                                    "hgvsProtein": "p.(Val1407Met)",
                                    "rankType": "EXON",
                                    "rank": 21,
                                    "rankTotal": 31,
                                },
                            ],
                        },
                        "geneIdentifier": {
                            "geneId": "ENSG00000114554",
                            "geneSymbol": "PLXNA1",
                            "hgncId": "HGNC:9099",
                            "hgncSymbol": "PLXNA1",
                            "entrezId": "5361",
                            "ensemblId": "ENSG00000114554",
                            "ucscId": "uc003ejg.3",
                        },
                        "modeOfInheritance": "AUTOSOMAL_RECESSIVE",
                        "disease": {"diseaseType": "UNCONFIRMED", "inheritanceMode": "UNKNOWN"},
                        "acmgEvidence": {"empty": True},
                        "acmgClassification": "UNCERTAIN_SIGNIFICANCE",
                    },
                ],
            },
            {
                "geneIdentifier": {
                    "geneId": "ENSG00000114554",
                    "geneSymbol": "PLXNA1",
                    "hgncId": "HGNC:9099",
                    "hgncSymbol": "PLXNA1",
                    "entrezId": "5361",
                    "ensemblId": "ENSG00000114554",
                    "ucscId": "uc003ejg.3",
                },
                "modeOfInheritance": "X_RECESSIVE",
                "combinedScore": 2.2792733292760184e-05,
                "phenotypeScore": 0.250043917891162,
                "pValue": 0.8396823708206687,
            },
            {
                "geneIdentifier": {
                    "geneId": "ENSG00000114554",
                    "geneSymbol": "PLXNA1",
                    "hgncId": "HGNC:9099",
                    "hgncSymbol": "PLXNA1",
                    "entrezId": "5361",
                    "ensemblId": "ENSG00000114554",
                    "ucscId": "uc003ejg.3",
                },
                "modeOfInheritance": "X_DOMINANT",
                "combinedScore": 2.2792733292760184e-05,
                "phenotypeScore": 0.250043917891162,
                "pValue": 0.8405273556231003,
            },
            {
                "geneIdentifier": {
                    "geneId": "ENSG00000114554",
                    "geneSymbol": "PLXNA1",
                    "hgncId": "HGNC:9099",
                    "hgncSymbol": "PLXNA1",
                    "entrezId": "5361",
                    "ensemblId": "ENSG00000114554",
                    "ucscId": "uc003ejg.3",
                },
                "modeOfInheritance": "MITOCHONDRIAL",
                "combinedScore": 2.2792733292760184e-05,
                "phenotypeScore": 0.250043917891162,
                "pValue": 0.8404544072948328,
            },
        ],
        "variantEvaluations": [
            {
                "genomeAssembly": "HG19",
                "contigName": "3",
                "start": 126730873,
                "end": 126730873,
                "ref": "G",
                "alt": "A",
                "id": "rs78052417",
                "type": "SNV",
                "length": 1,
                "phredScore": 2970.4399999999996,
                "variantEffect": "MISSENSE_VARIANT",
                "filterStatus": "PASSED",
                "contributesToGeneScore": True,
                "variantScore": 0.55660325,
                "frequencyScore": 0.9972702,
                "pathogenicityScore": 0.5581268,
                "predictedPathogenic": True,
                "passedFilterTypes": [
                    "FAILED_VARIANT_FILTER",
                    "PATHOGENICITY_FILTER",
                    "FREQUENCY_FILTER",
                    "VARIANT_EFFECT_FILTER",
                    "INHERITANCE_FILTER",
                ],
                "frequencyData": {
                    "rsId": "rs78052417",
                    "knownFrequencies": [
                        {"source": "THOUSAND_GENOMES", "frequency": 0.01997},
                        {"source": "TOPMED", "frequency": 0.001133},
                        {"source": "EXAC_NON_FINNISH_EUROPEAN", "frequency": 0.004534462},
                        {"source": "GNOMAD_E_NFE", "frequency": 0.0035905354},
                    ],
                    "score": 0.9972702,
                },
                "pathogenicityData": {
                    "clinVarData": {"primaryInterpretation": "NOT_PROVIDED"},
                    "mostPathogenicScore": {"source": "MVP", "score": 0.5581268},
                    "score": 0.5581268,
                    "predictedPathogenicityScores": [
                        {"source": "REVEL", "score": 0.348},
                        {"source": "MVP", "score": 0.5581268},
                    ],
                },
                "compatibleInheritanceModes": ["AUTOSOMAL_DOMINANT", "AUTOSOMAL_RECESSIVE"],
                "contributingInheritanceModes": ["AUTOSOMAL_DOMINANT", "AUTOSOMAL_RECESSIVE"],
                "transcriptAnnotations": [
                    {
                        "variantEffect": "MISSENSE_VARIANT",
                        "geneSymbol": "PLXNA1",
                        "accession": "ENST00000251772.4",
                        "hgvsGenomic": "g.126730873G>A",
                        "hgvsCdna": "c.2116G>A",
                        "hgvsProtein": "p.(Ala706Thr)",
                        "rankType": "EXON",
                        "rank": 9,
                        "rankTotal": 31,
                    },
                    {
                        "variantEffect": "MISSENSE_VARIANT",
                        "geneSymbol": "PLXNA1",
                        "accession": "ENST00000393409.2",
                        "hgvsGenomic": "g.126730873G>A",
                        "hgvsCdna": "c.2185G>A",
                        "hgvsProtein": "p.(Ala729Thr)",
                        "rankType": "EXON",
                        "rank": 9,
                        "rankTotal": 31,
                    },
                ],
            },
            {
                "genomeAssembly": "HG19",
                "contigName": "3",
                "start": 126741108,
                "end": 126741108,
                "ref": "G",
                "alt": "A",
                "id": "rs73196567",
                "type": "SNV",
                "length": 1,
                "phredScore": 3055.4399999999996,
                "variantEffect": "MISSENSE_VARIANT",
                "filterStatus": "PASSED",
                "contributesToGeneScore": True,
                "variantScore": 0.54480255,
                "frequencyScore": 0.98371375,
                "pathogenicityScore": 0.5538222,
                "predictedPathogenic": True,
                "passedFilterTypes": [
                    "FAILED_VARIANT_FILTER",
                    "PATHOGENICITY_FILTER",
                    "FREQUENCY_FILTER",
                    "VARIANT_EFFECT_FILTER",
                    "INHERITANCE_FILTER",
                ],
                "frequencyData": {
                    "rsId": "rs73196567",
                    "knownFrequencies": [
                        {"source": "THOUSAND_GENOMES", "frequency": 0.01997},
                        {"source": "TOPMED", "frequency": 0.002267},
                        {"source": "EXAC_EAST_ASIAN", "frequency": 0.0116198},
                        {"source": "EXAC_NON_FINNISH_EUROPEAN", "frequency": 0.0015265311},
                        {"source": "EXAC_OTHER", "frequency": 0.11363637},
                        {"source": "EXAC_SOUTH_ASIAN", "frequency": 0.0060716453},
                        {"source": "GNOMAD_E_EAS", "frequency": 0.01740543},
                        {"source": "GNOMAD_E_NFE", "frequency": 0.0017979468},
                        {"source": "GNOMAD_E_SAS", "frequency": 0.00325013},
                    ],
                    "score": 0.98371375,
                },
                "pathogenicityData": {
                    "clinVarData": {"primaryInterpretation": "NOT_PROVIDED"},
                    "mostPathogenicScore": {"source": "MVP", "score": 0.5538222},
                    "score": 0.5538222,
                    "predictedPathogenicityScores": [
                        {"source": "REVEL", "score": 0.301},
                        {"source": "MVP", "score": 0.5538222},
                    ],
                },
                "compatibleInheritanceModes": ["AUTOSOMAL_RECESSIVE"],
                "contributingInheritanceModes": ["AUTOSOMAL_RECESSIVE"],
                "transcriptAnnotations": [
                    {
                        "variantEffect": "MISSENSE_VARIANT",
                        "geneSymbol": "PLXNA1",
                        "accession": "ENST00000251772.4",
                        "hgvsGenomic": "g.126741108G>A",
                        "hgvsCdna": "c.4150G>A",
                        "hgvsProtein": "p.(Val1384Met)",
                        "rankType": "EXON",
                        "rank": 21,
                        "rankTotal": 31,
                    },
                    {
                        "variantEffect": "MISSENSE_VARIANT",
                        "geneSymbol": "PLXNA1",
                        "accession": "ENST00000393409.2",
                        "hgvsGenomic": "g.126741108G>A",
                        "hgvsCdna": "c.4219G>A",
                        "hgvsProtein": "p.(Val1407Met)",
                        "rankType": "EXON",
                        "rank": 21,
                        "rankTotal": 31,
                    },
                ],
            },
            {
                "genomeAssembly": "HG19",
                "contigName": "3",
                "start": 126747190,
                "end": 126747190,
                "ref": "G",
                "alt": "A",
                "id": "rs73196573",
                "type": "SNV",
                "length": 1,
                "phredScore": 867.44,
                "variantEffect": "SPLICE_REGION_VARIANT",
                "filterStatus": "PASSED",
                "variantScore": 0.44459406,
                "frequencyScore": 0.55574256,
                "pathogenicityScore": 0.8,
                "predictedPathogenic": True,
                "passedFilterTypes": [
                    "FAILED_VARIANT_FILTER",
                    "PATHOGENICITY_FILTER",
                    "FREQUENCY_FILTER",
                    "VARIANT_EFFECT_FILTER",
                    "INHERITANCE_FILTER",
                ],
                "frequencyData": {
                    "rsId": "rs73196573",
                    "knownFrequencies": [
                        {"source": "THOUSAND_GENOMES", "frequency": 0.2995},
                        {"source": "TOPMED", "frequency": 0.7016},
                        {"source": "UK10K", "frequency": 1.4546001},
                        {"source": "ESP_AFRICAN_AMERICAN", "frequency": 0.2502},
                        {"source": "ESP_EUROPEAN_AMERICAN", "frequency": 1.0249},
                        {"source": "ESP_ALL", "frequency": 0.7626},
                        {"source": "EXAC_AFRICAN_INC_AFRICAN_AMERICAN", "frequency": 0.19733596},
                        {"source": "EXAC_AMERICAN", "frequency": 0.2787586},
                        {"source": "EXAC_FINNISH", "frequency": 0.4754938},
                        {"source": "EXAC_NON_FINNISH_EUROPEAN", "frequency": 1.2409139},
                        {"source": "EXAC_OTHER", "frequency": 0.530504},
                        {"source": "EXAC_SOUTH_ASIAN", "frequency": 0.0551572},
                        {"source": "GNOMAD_E_AFR", "frequency": 0.2140411},
                        {"source": "GNOMAD_E_AMR", "frequency": 0.3137948},
                        {"source": "GNOMAD_E_ASJ", "frequency": 0.16163793},
                        {"source": "GNOMAD_E_FIN", "frequency": 0.4726635},
                        {"source": "GNOMAD_E_NFE", "frequency": 1.2459831},
                        {"source": "GNOMAD_E_OTH", "frequency": 0.6594259},
                        {"source": "GNOMAD_E_SAS", "frequency": 0.04284208},
                        {"source": "GNOMAD_G_AFR", "frequency": 0.2522936},
                        {"source": "GNOMAD_G_AMR", "frequency": 0.23866348},
                        {"source": "GNOMAD_G_ASJ", "frequency": 0.33112583},
                        {"source": "GNOMAD_G_FIN", "frequency": 0.744559},
                        {"source": "GNOMAD_G_NFE", "frequency": 1.080288},
                        {"source": "GNOMAD_G_OTH", "frequency": 0.6122449},
                    ],
                    "score": 0.55574256,
                },
                "pathogenicityData": {
                    "clinVarData": {
                        "alleleId": "1547890",
                        "primaryInterpretation": "BENIGN",
                        "reviewStatus": "criteria provided, single submitter",
                    }
                },
                "compatibleInheritanceModes": ["AUTOSOMAL_RECESSIVE"],
                "transcriptAnnotations": [
                    {
                        "variantEffect": "SPLICE_REGION_VARIANT",
                        "geneSymbol": "PLXNA1",
                        "accession": "ENST00000251772.4",
                        "hgvsGenomic": "g.126747190G>A",
                        "hgvsCdna": "c.4600+7G>A",
                        "hgvsProtein": "p.?",
                        "rankType": "INTRON",
                        "rank": 24,
                        "rankTotal": 30,
                    },
                    {
                        "variantEffect": "SPLICE_REGION_VARIANT",
                        "geneSymbol": "PLXNA1",
                        "accession": "ENST00000393409.2",
                        "hgvsGenomic": "g.126747190G>A",
                        "hgvsCdna": "c.4669+7G>A",
                        "hgvsProtein": "p.?",
                        "rankType": "INTRON",
                        "rank": 24,
                        "rankTotal": 30,
                    },
                ],
            },
        ],
        "compatibleGeneScores": [
            {
                "geneIdentifier": {
                    "geneId": "ENSG00000114554",
                    "geneSymbol": "PLXNA1",
                    "hgncId": "HGNC:9099",
                    "hgncSymbol": "PLXNA1",
                    "entrezId": "5361",
                    "ensemblId": "ENSG00000114554",
                    "ucscId": "uc003ejg.3",
                },
                "modeOfInheritance": "AUTOSOMAL_DOMINANT",
                "combinedScore": 0.048419416654489886,
                "phenotypeScore": 0.500087835782324,
                "variantScore": 0.5566032528877258,
                "pValue": 0.18761854103343464,
                "contributingVariants": [
                    {
                        "genomeAssembly": "HG19",
                        "contigName": "3",
                        "start": 126730873,
                        "end": 126730873,
                        "ref": "G",
                        "alt": "A",
                        "id": "rs78052417",
                        "type": "SNV",
                        "length": 1,
                        "phredScore": 2970.4399999999996,
                        "variantEffect": "MISSENSE_VARIANT",
                        "filterStatus": "PASSED",
                        "contributesToGeneScore": True,
                        "variantScore": 0.55660325,
                        "frequencyScore": 0.9972702,
                        "pathogenicityScore": 0.5581268,
                        "predictedPathogenic": True,
                        "passedFilterTypes": [
                            "FAILED_VARIANT_FILTER",
                            "PATHOGENICITY_FILTER",
                            "FREQUENCY_FILTER",
                            "VARIANT_EFFECT_FILTER",
                            "INHERITANCE_FILTER",
                        ],
                        "frequencyData": {
                            "rsId": "rs78052417",
                            "knownFrequencies": [
                                {"source": "THOUSAND_GENOMES", "frequency": 0.01997},
                                {"source": "TOPMED", "frequency": 0.001133},
                                {"source": "EXAC_NON_FINNISH_EUROPEAN", "frequency": 0.004534462},
                                {"source": "GNOMAD_E_NFE", "frequency": 0.0035905354},
                            ],
                            "score": 0.9972702,
                        },
                        "pathogenicityData": {
                            "clinVarData": {"primaryInterpretation": "NOT_PROVIDED"},
                            "mostPathogenicScore": {"source": "MVP", "score": 0.5581268},
                            "score": 0.5581268,
                            "predictedPathogenicityScores": [
                                {"source": "REVEL", "score": 0.348},
                                {"source": "MVP", "score": 0.5581268},
                            ],
                        },
                        "compatibleInheritanceModes": ["AUTOSOMAL_DOMINANT", "AUTOSOMAL_RECESSIVE"],
                        "contributingInheritanceModes": [
                            "AUTOSOMAL_DOMINANT",
                            "AUTOSOMAL_RECESSIVE",
                        ],
                        "transcriptAnnotations": [
                            {
                                "variantEffect": "MISSENSE_VARIANT",
                                "geneSymbol": "PLXNA1",
                                "accession": "ENST00000251772.4",
                                "hgvsGenomic": "g.126730873G>A",
                                "hgvsCdna": "c.2116G>A",
                                "hgvsProtein": "p.(Ala706Thr)",
                                "rankType": "EXON",
                                "rank": 9,
                                "rankTotal": 31,
                            },
                            {
                                "variantEffect": "MISSENSE_VARIANT",
                                "geneSymbol": "PLXNA1",
                                "accession": "ENST00000393409.2",
                                "hgvsGenomic": "g.126730873G>A",
                                "hgvsCdna": "c.2185G>A",
                                "hgvsProtein": "p.(Ala729Thr)",
                                "rankType": "EXON",
                                "rank": 9,
                                "rankTotal": 31,
                            },
                        ],
                    }
                ],
                "acmgAssignments": [
                    {
                        "variantEvaluation": {
                            "genomeAssembly": "HG19",
                            "contigName": "3",
                            "start": 126730873,
                            "end": 126730873,
                            "ref": "G",
                            "alt": "A",
                            "id": "rs78052417",
                            "type": "SNV",
                            "length": 1,
                            "phredScore": 2970.4399999999996,
                            "variantEffect": "MISSENSE_VARIANT",
                            "filterStatus": "PASSED",
                            "contributesToGeneScore": True,
                            "variantScore": 0.55660325,
                            "frequencyScore": 0.9972702,
                            "pathogenicityScore": 0.5581268,
                            "predictedPathogenic": True,
                            "passedFilterTypes": [
                                "FAILED_VARIANT_FILTER",
                                "PATHOGENICITY_FILTER",
                                "FREQUENCY_FILTER",
                                "VARIANT_EFFECT_FILTER",
                                "INHERITANCE_FILTER",
                            ],
                            "frequencyData": {
                                "rsId": "rs78052417",
                                "knownFrequencies": [
                                    {"source": "THOUSAND_GENOMES", "frequency": 0.01997},
                                    {"source": "TOPMED", "frequency": 0.001133},
                                    {
                                        "source": "EXAC_NON_FINNISH_EUROPEAN",
                                        "frequency": 0.004534462,
                                    },
                                    {"source": "GNOMAD_E_NFE", "frequency": 0.0035905354},
                                ],
                                "score": 0.9972702,
                            },
                            "pathogenicityData": {
                                "clinVarData": {"primaryInterpretation": "NOT_PROVIDED"},
                                "mostPathogenicScore": {"source": "MVP", "score": 0.5581268},
                                "score": 0.5581268,
                                "predictedPathogenicityScores": [
                                    {"source": "REVEL", "score": 0.348},
                                    {"source": "MVP", "score": 0.5581268},
                                ],
                            },
                            "compatibleInheritanceModes": [
                                "AUTOSOMAL_DOMINANT",
                                "AUTOSOMAL_RECESSIVE",
                            ],
                            "contributingInheritanceModes": [
                                "AUTOSOMAL_DOMINANT",
                                "AUTOSOMAL_RECESSIVE",
                            ],
                            "transcriptAnnotations": [
                                {
                                    "variantEffect": "MISSENSE_VARIANT",
                                    "geneSymbol": "PLXNA1",
                                    "accession": "ENST00000251772.4",
                                    "hgvsGenomic": "g.126730873G>A",
                                    "hgvsCdna": "c.2116G>A",
                                    "hgvsProtein": "p.(Ala706Thr)",
                                    "rankType": "EXON",
                                    "rank": 9,
                                    "rankTotal": 31,
                                },
                                {
                                    "variantEffect": "MISSENSE_VARIANT",
                                    "geneSymbol": "PLXNA1",
                                    "accession": "ENST00000393409.2",
                                    "hgvsGenomic": "g.126730873G>A",
                                    "hgvsCdna": "c.2185G>A",
                                    "hgvsProtein": "p.(Ala729Thr)",
                                    "rankType": "EXON",
                                    "rank": 9,
                                    "rankTotal": 31,
                                },
                            ],
                        },
                        "geneIdentifier": {
                            "geneId": "ENSG00000114554",
                            "geneSymbol": "PLXNA1",
                            "hgncId": "HGNC:9099",
                            "hgncSymbol": "PLXNA1",
                            "entrezId": "5361",
                            "ensemblId": "ENSG00000114554",
                            "ucscId": "uc003ejg.3",
                        },
                        "modeOfInheritance": "AUTOSOMAL_DOMINANT",
                        "disease": {"diseaseType": "UNCONFIRMED", "inheritanceMode": "UNKNOWN"},
                        "acmgEvidence": {"empty": True},
                        "acmgClassification": "UNCERTAIN_SIGNIFICANCE",
                    }
                ],
            },
            {
                "geneIdentifier": {
                    "geneId": "ENSG00000114554",
                    "geneSymbol": "PLXNA1",
                    "hgncId": "HGNC:9099",
                    "hgncSymbol": "PLXNA1",
                    "entrezId": "5361",
                    "ensemblId": "ENSG00000114554",
                    "ucscId": "uc003ejg.3",
                },
                "modeOfInheritance": "AUTOSOMAL_RECESSIVE",
                "combinedScore": 0.04598293574097189,
                "phenotypeScore": 0.500087835782324,
                "variantScore": 0.5507028996944427,
                "pValue": 0.19066565349544073,
                "contributingVariants": [
                    {
                        "genomeAssembly": "HG19",
                        "contigName": "3",
                        "start": 126730873,
                        "end": 126730873,
                        "ref": "G",
                        "alt": "A",
                        "id": "rs78052417",
                        "type": "SNV",
                        "length": 1,
                        "phredScore": 2970.4399999999996,
                        "variantEffect": "MISSENSE_VARIANT",
                        "filterStatus": "PASSED",
                        "contributesToGeneScore": True,
                        "variantScore": 0.55660325,
                        "frequencyScore": 0.9972702,
                        "pathogenicityScore": 0.5581268,
                        "predictedPathogenic": True,
                        "passedFilterTypes": [
                            "FAILED_VARIANT_FILTER",
                            "PATHOGENICITY_FILTER",
                            "FREQUENCY_FILTER",
                            "VARIANT_EFFECT_FILTER",
                            "INHERITANCE_FILTER",
                        ],
                        "frequencyData": {
                            "rsId": "rs78052417",
                            "knownFrequencies": [
                                {"source": "THOUSAND_GENOMES", "frequency": 0.01997},
                                {"source": "TOPMED", "frequency": 0.001133},
                                {"source": "EXAC_NON_FINNISH_EUROPEAN", "frequency": 0.004534462},
                                {"source": "GNOMAD_E_NFE", "frequency": 0.0035905354},
                            ],
                            "score": 0.9972702,
                        },
                        "pathogenicityData": {
                            "clinVarData": {"primaryInterpretation": "NOT_PROVIDED"},
                            "mostPathogenicScore": {"source": "MVP", "score": 0.5581268},
                            "score": 0.5581268,
                            "predictedPathogenicityScores": [
                                {"source": "REVEL", "score": 0.348},
                                {"source": "MVP", "score": 0.5581268},
                            ],
                        },
                        "compatibleInheritanceModes": ["AUTOSOMAL_DOMINANT", "AUTOSOMAL_RECESSIVE"],
                        "contributingInheritanceModes": [
                            "AUTOSOMAL_DOMINANT",
                            "AUTOSOMAL_RECESSIVE",
                        ],
                        "transcriptAnnotations": [
                            {
                                "variantEffect": "MISSENSE_VARIANT",
                                "geneSymbol": "PLXNA1",
                                "accession": "ENST00000251772.4",
                                "hgvsGenomic": "g.126730873G>A",
                                "hgvsCdna": "c.2116G>A",
                                "hgvsProtein": "p.(Ala706Thr)",
                                "rankType": "EXON",
                                "rank": 9,
                                "rankTotal": 31,
                            },
                            {
                                "variantEffect": "MISSENSE_VARIANT",
                                "geneSymbol": "PLXNA1",
                                "accession": "ENST00000393409.2",
                                "hgvsGenomic": "g.126730873G>A",
                                "hgvsCdna": "c.2185G>A",
                                "hgvsProtein": "p.(Ala729Thr)",
                                "rankType": "EXON",
                                "rank": 9,
                                "rankTotal": 31,
                            },
                        ],
                    },
                    {
                        "genomeAssembly": "HG19",
                        "contigName": "3",
                        "start": 126741108,
                        "end": 126741108,
                        "ref": "G",
                        "alt": "A",
                        "id": "rs73196567",
                        "type": "SNV",
                        "length": 1,
                        "phredScore": 3055.4399999999996,
                        "variantEffect": "MISSENSE_VARIANT",
                        "filterStatus": "PASSED",
                        "contributesToGeneScore": True,
                        "variantScore": 0.54480255,
                        "frequencyScore": 0.98371375,
                        "pathogenicityScore": 0.5538222,
                        "predictedPathogenic": True,
                        "passedFilterTypes": [
                            "FAILED_VARIANT_FILTER",
                            "PATHOGENICITY_FILTER",
                            "FREQUENCY_FILTER",
                            "VARIANT_EFFECT_FILTER",
                            "INHERITANCE_FILTER",
                        ],
                        "frequencyData": {
                            "rsId": "rs73196567",
                            "knownFrequencies": [
                                {"source": "THOUSAND_GENOMES", "frequency": 0.01997},
                                {"source": "TOPMED", "frequency": 0.002267},
                                {"source": "EXAC_EAST_ASIAN", "frequency": 0.0116198},
                                {"source": "EXAC_NON_FINNISH_EUROPEAN", "frequency": 0.0015265311},
                                {"source": "EXAC_OTHER", "frequency": 0.11363637},
                                {"source": "EXAC_SOUTH_ASIAN", "frequency": 0.0060716453},
                                {"source": "GNOMAD_E_EAS", "frequency": 0.01740543},
                                {"source": "GNOMAD_E_NFE", "frequency": 0.0017979468},
                                {"source": "GNOMAD_E_SAS", "frequency": 0.00325013},
                            ],
                            "score": 0.98371375,
                        },
                        "pathogenicityData": {
                            "clinVarData": {"primaryInterpretation": "NOT_PROVIDED"},
                            "mostPathogenicScore": {"source": "MVP", "score": 0.5538222},
                            "score": 0.5538222,
                            "predictedPathogenicityScores": [
                                {"source": "REVEL", "score": 0.301},
                                {"source": "MVP", "score": 0.5538222},
                            ],
                        },
                        "compatibleInheritanceModes": ["AUTOSOMAL_RECESSIVE"],
                        "contributingInheritanceModes": ["AUTOSOMAL_RECESSIVE"],
                        "transcriptAnnotations": [
                            {
                                "variantEffect": "MISSENSE_VARIANT",
                                "geneSymbol": "PLXNA1",
                                "accession": "ENST00000251772.4",
                                "hgvsGenomic": "g.126741108G>A",
                                "hgvsCdna": "c.4150G>A",
                                "hgvsProtein": "p.(Val1384Met)",
                                "rankType": "EXON",
                                "rank": 21,
                                "rankTotal": 31,
                            },
                            {
                                "variantEffect": "MISSENSE_VARIANT",
                                "geneSymbol": "PLXNA1",
                                "accession": "ENST00000393409.2",
                                "hgvsGenomic": "g.126741108G>A",
                                "hgvsCdna": "c.4219G>A",
                                "hgvsProtein": "p.(Val1407Met)",
                                "rankType": "EXON",
                                "rank": 21,
                                "rankTotal": 31,
                            },
                        ],
                    },
                ],
                "acmgAssignments": [
                    {
                        "variantEvaluation": {
                            "genomeAssembly": "HG19",
                            "contigName": "3",
                            "start": 126730873,
                            "end": 126730873,
                            "ref": "G",
                            "alt": "A",
                            "id": "rs78052417",
                            "type": "SNV",
                            "length": 1,
                            "phredScore": 2970.4399999999996,
                            "variantEffect": "MISSENSE_VARIANT",
                            "filterStatus": "PASSED",
                            "contributesToGeneScore": True,
                            "variantScore": 0.55660325,
                            "frequencyScore": 0.9972702,
                            "pathogenicityScore": 0.5581268,
                            "predictedPathogenic": True,
                            "passedFilterTypes": [
                                "FAILED_VARIANT_FILTER",
                                "PATHOGENICITY_FILTER",
                                "FREQUENCY_FILTER",
                                "VARIANT_EFFECT_FILTER",
                                "INHERITANCE_FILTER",
                            ],
                            "frequencyData": {
                                "rsId": "rs78052417",
                                "knownFrequencies": [
                                    {"source": "THOUSAND_GENOMES", "frequency": 0.01997},
                                    {"source": "TOPMED", "frequency": 0.001133},
                                    {
                                        "source": "EXAC_NON_FINNISH_EUROPEAN",
                                        "frequency": 0.004534462,
                                    },
                                    {"source": "GNOMAD_E_NFE", "frequency": 0.0035905354},
                                ],
                                "score": 0.9972702,
                            },
                            "pathogenicityData": {
                                "clinVarData": {"primaryInterpretation": "NOT_PROVIDED"},
                                "mostPathogenicScore": {"source": "MVP", "score": 0.5581268},
                                "score": 0.5581268,
                                "predictedPathogenicityScores": [
                                    {"source": "REVEL", "score": 0.348},
                                    {"source": "MVP", "score": 0.5581268},
                                ],
                            },
                            "compatibleInheritanceModes": [
                                "AUTOSOMAL_DOMINANT",
                                "AUTOSOMAL_RECESSIVE",
                            ],
                            "contributingInheritanceModes": [
                                "AUTOSOMAL_DOMINANT",
                                "AUTOSOMAL_RECESSIVE",
                            ],
                            "transcriptAnnotations": [
                                {
                                    "variantEffect": "MISSENSE_VARIANT",
                                    "geneSymbol": "PLXNA1",
                                    "accession": "ENST00000251772.4",
                                    "hgvsGenomic": "g.126730873G>A",
                                    "hgvsCdna": "c.2116G>A",
                                    "hgvsProtein": "p.(Ala706Thr)",
                                    "rankType": "EXON",
                                    "rank": 9,
                                    "rankTotal": 31,
                                },
                                {
                                    "variantEffect": "MISSENSE_VARIANT",
                                    "geneSymbol": "PLXNA1",
                                    "accession": "ENST00000393409.2",
                                    "hgvsGenomic": "g.126730873G>A",
                                    "hgvsCdna": "c.2185G>A",
                                    "hgvsProtein": "p.(Ala729Thr)",
                                    "rankType": "EXON",
                                    "rank": 9,
                                    "rankTotal": 31,
                                },
                            ],
                        },
                        "geneIdentifier": {
                            "geneId": "ENSG00000114554",
                            "geneSymbol": "PLXNA1",
                            "hgncId": "HGNC:9099",
                            "hgncSymbol": "PLXNA1",
                            "entrezId": "5361",
                            "ensemblId": "ENSG00000114554",
                            "ucscId": "uc003ejg.3",
                        },
                        "modeOfInheritance": "AUTOSOMAL_RECESSIVE",
                        "disease": {"diseaseType": "UNCONFIRMED", "inheritanceMode": "UNKNOWN"},
                        "acmgEvidence": {"empty": True},
                        "acmgClassification": "UNCERTAIN_SIGNIFICANCE",
                    },
                    {
                        "variantEvaluation": {
                            "genomeAssembly": "HG19",
                            "contigName": "3",
                            "start": 126741108,
                            "end": 126741108,
                            "ref": "G",
                            "alt": "A",
                            "id": "rs73196567",
                            "type": "SNV",
                            "length": 1,
                            "phredScore": 3055.4399999999996,
                            "variantEffect": "MISSENSE_VARIANT",
                            "filterStatus": "PASSED",
                            "contributesToGeneScore": True,
                            "variantScore": 0.54480255,
                            "frequencyScore": 0.98371375,
                            "pathogenicityScore": 0.5538222,
                            "predictedPathogenic": True,
                            "passedFilterTypes": [
                                "FAILED_VARIANT_FILTER",
                                "PATHOGENICITY_FILTER",
                                "FREQUENCY_FILTER",
                                "VARIANT_EFFECT_FILTER",
                                "INHERITANCE_FILTER",
                            ],
                            "frequencyData": {
                                "rsId": "rs73196567",
                                "knownFrequencies": [
                                    {"source": "THOUSAND_GENOMES", "frequency": 0.01997},
                                    {"source": "TOPMED", "frequency": 0.002267},
                                    {"source": "EXAC_EAST_ASIAN", "frequency": 0.0116198},
                                    {
                                        "source": "EXAC_NON_FINNISH_EUROPEAN",
                                        "frequency": 0.0015265311,
                                    },
                                    {"source": "EXAC_OTHER", "frequency": 0.11363637},
                                    {"source": "EXAC_SOUTH_ASIAN", "frequency": 0.0060716453},
                                    {"source": "GNOMAD_E_EAS", "frequency": 0.01740543},
                                    {"source": "GNOMAD_E_NFE", "frequency": 0.0017979468},
                                    {"source": "GNOMAD_E_SAS", "frequency": 0.00325013},
                                ],
                                "score": 0.98371375,
                            },
                            "pathogenicityData": {
                                "clinVarData": {"primaryInterpretation": "NOT_PROVIDED"},
                                "mostPathogenicScore": {"source": "MVP", "score": 0.5538222},
                                "score": 0.5538222,
                                "predictedPathogenicityScores": [
                                    {"source": "REVEL", "score": 0.301},
                                    {"source": "MVP", "score": 0.5538222},
                                ],
                            },
                            "compatibleInheritanceModes": ["AUTOSOMAL_RECESSIVE"],
                            "contributingInheritanceModes": ["AUTOSOMAL_RECESSIVE"],
                            "transcriptAnnotations": [
                                {
                                    "variantEffect": "MISSENSE_VARIANT",
                                    "geneSymbol": "PLXNA1",
                                    "accession": "ENST00000251772.4",
                                    "hgvsGenomic": "g.126741108G>A",
                                    "hgvsCdna": "c.4150G>A",
                                    "hgvsProtein": "p.(Val1384Met)",
                                    "rankType": "EXON",
                                    "rank": 21,
                                    "rankTotal": 31,
                                },
                                {
                                    "variantEffect": "MISSENSE_VARIANT",
                                    "geneSymbol": "PLXNA1",
                                    "accession": "ENST00000393409.2",
                                    "hgvsGenomic": "g.126741108G>A",
                                    "hgvsCdna": "c.4219G>A",
                                    "hgvsProtein": "p.(Val1407Met)",
                                    "rankType": "EXON",
                                    "rank": 21,
                                    "rankTotal": 31,
                                },
                            ],
                        },
                        "geneIdentifier": {
                            "geneId": "ENSG00000114554",
                            "geneSymbol": "PLXNA1",
                            "hgncId": "HGNC:9099",
                            "hgncSymbol": "PLXNA1",
                            "entrezId": "5361",
                            "ensemblId": "ENSG00000114554",
                            "ucscId": "uc003ejg.3",
                        },
                        "modeOfInheritance": "AUTOSOMAL_RECESSIVE",
                        "disease": {"diseaseType": "UNCONFIRMED", "inheritanceMode": "UNKNOWN"},
                        "acmgEvidence": {"empty": True},
                        "acmgClassification": "UNCERTAIN_SIGNIFICANCE",
                    },
                ],
            },
        ],
    }
]


class TestSimplifiedExomiserGeneResult(unittest.TestCase):
    def setUp(self) -> None:
        self.simplified_exomiser_gene_result = SimplifiedExomiserGeneResult(
            exomiser_result=example_exomiser_result[0],
            simplified_exomiser_gene_result=[],
            ranking_method="combinedScore",
        )

    def test_add_gene_record(self):
        self.assertEqual(
            self.simplified_exomiser_gene_result.add_gene_record(),
            {"gene_symbol": "PLXNA1", "gene_identifier": "ENSG00000114554"},
        )

    def test_add_ranking_score(self):
        self.assertEqual(
            self.simplified_exomiser_gene_result.add_ranking_score(
                {"gene_symbol": "PLXNA1", "gene_identifier": "ENSG00000114554"}
            ),
            {
                "gene_symbol": "PLXNA1",
                "gene_identifier": "ENSG00000114554",
                "score": 0.0484,
            },
        )

    def test_create_simplified_gene_result(self):
        self.assertEqual(
            self.simplified_exomiser_gene_result.create_simplified_gene_result(),
            [
                {
                    "gene_symbol": "PLXNA1",
                    "gene_identifier": "ENSG00000114554",
                    "score": 0.0484,
                }
            ],
        )


class TestSimplifiedExomiserVariantResult(unittest.TestCase):
    def setUp(self) -> None:
        self.simplified_exomiser_variant_result = SimplifiedExomiserVariantResult(
            exomiser_result=example_exomiser_result[0]["geneScores"][0],
            simplified_exomiser_variant_result=[],
            ranking_method="combinedScore",
            ranking_score=0.6589364,
        )

    def test_create_simplified_variant_result(self):
        self.assertEqual(
            self.simplified_exomiser_variant_result.create_simplified_variant_result(),
            [
                {
                    "variant": dataclasses.asdict(
                        VariantData(chrom="3", pos=126730873, ref="G", alt="A", gene="PLXNA1")
                    ),
                    "score": 0.6589364,
                }
            ],
        )


class TestRankExomiserResult(unittest.TestCase):
    def setUp(self) -> None:
        self.simplified_gene_result = RankExomiserResult(
            simplified_exomiser_result=[
                {
                    "gene_symbol": "PLXNA1",
                    "gene_identifier": "ENSG00000114554",
                    "score": 0.8764,
                },
                {
                    "gene_symbol": "SPNS1",
                    "gene_identifier": "ENSG00000169682",
                    "score": 0.3765,
                },
                {
                    "gene_symbol": "ZNF804B",
                    "gene_identifier": "ENSG00000182348",
                    "score": 0.5777,
                },
                {
                    "gene_symbol": "SMCO2",
                    "gene_identifier": "ENSG00000165935",
                    "score": 0.5777,
                },
            ],
            ranking_method="combinedScore",
        )
        self.simplified_variant_result = RankExomiserResult(
            simplified_exomiser_result=[
                {
                    "variant": VariantData(
                        chrom="3", pos=126730873, ref="G", alt="A", gene="PLXNA1"
                    ),
                    "score": 0.8764,
                },
                {
                    "variant": VariantData(
                        chrom="16", pos=28995541, ref="C", alt="A", gene="SPNS1"
                    ),
                    "score": 0.3765,
                },
                {
                    "variant": VariantData(
                        chrom="7", pos=88965159, ref="T", alt="G", gene="ZNF804B"
                    ),
                    "score": 0.5777,
                },
                {
                    "variant": VariantData(
                        chrom="12", pos=27623658, ref="T", alt="A", gene="SMCO2"
                    ),
                    "score": 0.5777,
                },
            ],
            ranking_method="combinedScore",
        )
        self.simplified_gene_result_pvalue = RankExomiserResult(
            simplified_exomiser_result=[
                {"gene_symbol": "PLXNA1", "gene_identifier": "ENSG00000114554", "score": 0.8764},
                {"gene_symbol": "SPNS1", "gene_identifier": "ENSG00000169682", "score": 0.3765},
                {"gene_symbol": "ZNF804B", "gene_identifier": "ENSG00000182348", "score": 0.5777},
                {"gene_symbol": "SMCO2", "gene_identifier": "ENSG00000165935", "score": 0.5777},
            ],
            ranking_method="pValue",
        )

    def test_sort_exomiser_result_gene(self):
        self.assertEqual(
            self.simplified_gene_result.sort_exomiser_result(),
            [
                {
                    "gene_symbol": "PLXNA1",
                    "gene_identifier": "ENSG00000114554",
                    "score": 0.8764,
                },
                {
                    "gene_symbol": "ZNF804B",
                    "gene_identifier": "ENSG00000182348",
                    "score": 0.5777,
                },
                {
                    "gene_symbol": "SMCO2",
                    "gene_identifier": "ENSG00000165935",
                    "score": 0.5777,
                },
                {
                    "gene_symbol": "SPNS1",
                    "gene_identifier": "ENSG00000169682",
                    "score": 0.3765,
                },
            ],
        )

    def test_sort_exomiser_result_variant(self):
        self.assertEqual(
            self.simplified_variant_result.sort_exomiser_result(),
            [
                {
                    "variant": VariantData(
                        chrom="3", pos=126730873, ref="G", alt="A", gene="PLXNA1"
                    ),
                    "score": 0.8764,
                },
                {
                    "variant": VariantData(
                        chrom="7", pos=88965159, ref="T", alt="G", gene="ZNF804B"
                    ),
                    "score": 0.5777,
                },
                {
                    "variant": VariantData(
                        chrom="12", pos=27623658, ref="T", alt="A", gene="SMCO2"
                    ),
                    "score": 0.5777,
                },
                {
                    "variant": VariantData(
                        chrom="16", pos=28995541, ref="C", alt="A", gene="SPNS1"
                    ),
                    "score": 0.3765,
                },
            ],
        )

    def test_sort_exomiser_result_pvalue(self):
        self.assertEqual(
            self.simplified_gene_result_pvalue.sort_exomiser_result_pvalue(),
            [
                {"gene_symbol": "SPNS1", "gene_identifier": "ENSG00000169682", "score": 0.3765},
                {"gene_symbol": "ZNF804B", "gene_identifier": "ENSG00000182348", "score": 0.5777},
                {"gene_symbol": "SMCO2", "gene_identifier": "ENSG00000165935", "score": 0.5777},
                {"gene_symbol": "PLXNA1", "gene_identifier": "ENSG00000114554", "score": 0.8764},
            ],
        )

    def test_rank_results_gene(self):
        self.assertEqual(
            self.simplified_gene_result.rank_results(),
            [
                {
                    "gene_symbol": "PLXNA1",
                    "gene_identifier": "ENSG00000114554",
                    "score": 0.8764,
                    "rank": 1,
                },
                {
                    "gene_symbol": "ZNF804B",
                    "gene_identifier": "ENSG00000182348",
                    "score": 0.5777,
                    "rank": 2,
                },
                {
                    "gene_symbol": "SMCO2",
                    "gene_identifier": "ENSG00000165935",
                    "score": 0.5777,
                    "rank": 2,
                },
                {
                    "gene_symbol": "SPNS1",
                    "gene_identifier": "ENSG00000169682",
                    "score": 0.3765,
                    "rank": 4,
                },
            ],
        )

    def test_rank_results_variant(self):
        self.assertEqual(
            self.simplified_variant_result.rank_results(),
            [
                {
                    "variant": VariantData(
                        chrom="3", pos=126730873, ref="G", alt="A", gene="PLXNA1"
                    ),
                    "rank": 1,
                    "score": 0.8764,
                },
                {
                    "variant": VariantData(
                        chrom="7", pos=88965159, ref="T", alt="G", gene="ZNF804B"
                    ),
                    "rank": 2,
                    "score": 0.5777,
                },
                {
                    "variant": VariantData(
                        chrom="12", pos=27623658, ref="T", alt="A", gene="SMCO2"
                    ),
                    "rank": 2,
                    "score": 0.5777,
                },
                {
                    "variant": VariantData(
                        chrom="16", pos=28995541, ref="C", alt="A", gene="SPNS1"
                    ),
                    "rank": 4,
                    "score": 0.3765,
                },
            ],
        )

    def test_rank_results_pvalue(self):
        self.assertEqual(
            self.simplified_gene_result_pvalue.rank_results(),
            [
                {
                    "gene_symbol": "SPNS1",
                    "gene_identifier": "ENSG00000169682",
                    "score": 0.3765,
                    "rank": 1,
                },
                {
                    "gene_symbol": "ZNF804B",
                    "gene_identifier": "ENSG00000182348",
                    "score": 0.5777,
                    "rank": 2,
                },
                {
                    "gene_symbol": "SMCO2",
                    "gene_identifier": "ENSG00000165935",
                    "score": 0.5777,
                    "rank": 2,
                },
                {
                    "gene_symbol": "PLXNA1",
                    "gene_identifier": "ENSG00000114554",
                    "score": 0.8764,
                    "rank": 4,
                },
            ],
        )


class TestStandardiseExomiserResults(unittest.TestCase):
    def setUp(self) -> None:
        self.standardised_result = StandardiseExomiserResult(
            exomiser_json_result=example_exomiser_result, ranking_method="combinedScore"
        )

    def test_simplify_gene_result(self):
        self.assertEqual(
            self.standardised_result.simplify_gene_result(),
            [
                {
                    "gene_symbol": "PLXNA1",
                    "gene_identifier": "ENSG00000114554",
                    "score": 0.0484,
                }
            ],
        )

    def test_simplify_variant_result(self):
        self.assertEqual(
            self.standardised_result.simplify_variant_result(),
            [
                {
                    "variant": dataclasses.asdict(
                        VariantData(chrom="3", pos=126730873, ref="G", alt="A", gene="PLXNA1")
                    ),
                    "score": 0.0484,
                },
                {
                    "variant": dataclasses.asdict(
                        VariantData(chrom="3", pos=126730873, ref="G", alt="A", gene="PLXNA1")
                    ),
                    "score": 0.0484,
                },
                {
                    "variant": dataclasses.asdict(
                        VariantData(chrom="3", pos=126741108, ref="G", alt="A", gene="PLXNA1")
                    ),
                    "score": 0.0484,
                },
            ],
        )

    def test_standardise_gene_result(self):
        self.assertEqual(
            self.standardised_result.standardise_gene_result(),
            [
                {
                    "gene_symbol": "PLXNA1",
                    "gene_identifier": "ENSG00000114554",
                    "score": 0.0484,
                    "rank": 1,
                }
            ],
        )

    def test_standardise_variant_result(self):
        self.assertEqual(
            self.standardised_result.standardise_variant_result(),
            [
                {
                    "variant": dataclasses.asdict(
                        VariantData(chrom="3", pos=126730873, ref="G", alt="A", gene="PLXNA1")
                    ),
                    "score": 0.0484,
                    "rank": 1,
                },
                {
                    "variant": dataclasses.asdict(
                        VariantData(chrom="3", pos=126730873, ref="G", alt="A", gene="PLXNA1")
                    ),
                    "score": 0.0484,
                    "rank": 1,
                },
                {
                    "variant": dataclasses.asdict(
                        VariantData(chrom="3", pos=126741108, ref="G", alt="A", gene="PLXNA1")
                    ),
                    "score": 0.0484,
                    "rank": 1,
                },
            ],
        )
