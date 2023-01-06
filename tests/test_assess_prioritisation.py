import unittest
from collections import defaultdict

from pheval.utils.phenopacket_utils import VariantData

from pheval_exomiser.post_process.assess_prioritisation import (
    RankExomiserResult,
    SimplifiedExomiserResult,
    StandardiseExomiserResult,
)


class TestSimplifiedExomiserResult(unittest.TestCase):
    def setUp(self) -> None:
        self.simplified_exomiser_result = SimplifiedExomiserResult(
            exomiser_result={
                "geneIdentifier": {
                    "geneId": "ENSG00000187172",
                    "geneSymbol": "BAGE2",
                    "hgncId": "HGNC:15723",
                    "hgncSymbol": "BAGE2",
                    "entrezId": "85319",
                    "ensemblId": "ENSG00000187172",
                },
                "modeOfInheritance": "AUTOSOMAL_RECESSIVE",
                "combinedScore": 0.0026222891432373043,
                "variantScore": 0.800000011920929,
                "pValue": 0.4406854103343465,
                "contributingVariants": [
                    {
                        "genomeAssembly": "HG19",
                        "contigName": "21",
                        "start": 11021215,
                        "end": 11021215,
                        "ref": "T",
                        "alt": "TA",
                        "id": "rs71222366",
                        "type": "INS",
                        "length": 1,
                        "changeLength": 1,
                        "phredScore": 1139.4,
                        "variantEffect": "SPLICE_REGION_VARIANT",
                        "filterStatus": "PASSED",
                        "contributesToGeneScore": True,
                        "variantScore": 0.8,
                        "frequencyScore": 1.0,
                        "pathogenicityScore": 0.8,
                        "predictedPathogenic": True,
                        "passedFilterTypes": [
                            "FAILED_VARIANT_FILTER",
                            "PATHOGENICITY_FILTER",
                            "FREQUENCY_FILTER",
                            "VARIANT_EFFECT_FILTER",
                            "INHERITANCE_FILTER",
                        ],
                        "frequencyData": {"rsId": "rs71222366", "score": 1.0},
                        "pathogenicityData": {
                            "clinVarData": {"primaryInterpretation": "NOT_PROVIDED"}
                        },
                        "compatibleInheritanceModes": ["AUTOSOMAL_DOMINANT", "AUTOSOMAL_RECESSIVE"],
                        "contributingInheritanceModes": [
                            "AUTOSOMAL_DOMINANT",
                            "AUTOSOMAL_RECESSIVE",
                        ],
                        "transcriptAnnotations": [
                            {
                                "variantEffect": "SPLICE_REGION_VARIANT",
                                "geneSymbol": "BAGE2",
                                "accession": "ENST00000470054.1",
                                "hgvsGenomic": "g.37108680_37108681insT",
                                "hgvsCdna": "n.1714-5_1714-4insT",
                                "rankType": "INTRON",
                                "rank": 8,
                                "rankTotal": 9,
                            }
                        ],
                    },
                    {
                        "genomeAssembly": "HG19",
                        "contigName": "21",
                        "start": 11038722,
                        "end": 11038722,
                        "ref": "C",
                        "alt": "A",
                        "id": "rs62209718",
                        "type": "SNV",
                        "length": 1,
                        "phredScore": 786.44,
                        "variantEffect": "SPLICE_REGION_VARIANT",
                        "filterStatus": "PASSED",
                        "contributesToGeneScore": True,
                        "variantScore": 0.8,
                        "frequencyScore": 1.0,
                        "pathogenicityScore": 0.8,
                        "predictedPathogenic": True,
                        "passedFilterTypes": [
                            "FAILED_VARIANT_FILTER",
                            "PATHOGENICITY_FILTER",
                            "FREQUENCY_FILTER",
                            "VARIANT_EFFECT_FILTER",
                            "INHERITANCE_FILTER",
                        ],
                        "frequencyData": {"rsId": "rs10433074", "score": 1.0},
                        "pathogenicityData": {
                            "clinVarData": {"primaryInterpretation": "NOT_PROVIDED"}
                        },
                        "compatibleInheritanceModes": ["AUTOSOMAL_DOMINANT", "AUTOSOMAL_RECESSIVE"],
                        "contributingInheritanceModes": ["AUTOSOMAL_RECESSIVE"],
                        "transcriptAnnotations": [
                            {
                                "variantEffect": "SPLICE_REGION_VARIANT",
                                "geneSymbol": "BAGE2",
                                "accession": "ENST00000470054.1",
                                "hgvsGenomic": "g.37091174G>T",
                                "hgvsCdna": "n.1476+6G>T",
                                "rankType": "INTRON",
                                "rank": 6,
                                "rankTotal": 9,
                            }
                        ],
                    },
                ],
                "acmgAssignments": [
                    {
                        "variantEvaluation": {
                            "genomeAssembly": "HG19",
                            "contigName": "21",
                            "start": 11021215,
                            "end": 11021215,
                            "ref": "T",
                            "alt": "TA",
                            "id": "rs71222366",
                            "type": "INS",
                            "length": 1,
                            "changeLength": 1,
                            "phredScore": 1139.4,
                            "variantEffect": "SPLICE_REGION_VARIANT",
                            "filterStatus": "PASSED",
                            "contributesToGeneScore": True,
                            "variantScore": 0.8,
                            "frequencyScore": 1.0,
                            "pathogenicityScore": 0.8,
                            "predictedPathogenic": True,
                            "passedFilterTypes": [
                                "FAILED_VARIANT_FILTER",
                                "PATHOGENICITY_FILTER",
                                "FREQUENCY_FILTER",
                                "VARIANT_EFFECT_FILTER",
                                "INHERITANCE_FILTER",
                            ],
                            "frequencyData": {"rsId": "rs71222366", "score": 1.0},
                            "pathogenicityData": {
                                "clinVarData": {"primaryInterpretation": "NOT_PROVIDED"}
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
                                    "variantEffect": "SPLICE_REGION_VARIANT",
                                    "geneSymbol": "BAGE2",
                                    "accession": "ENST00000470054.1",
                                    "hgvsGenomic": "g.37108680_37108681insT",
                                    "hgvsCdna": "n.1714-5_1714-4insT",
                                    "rankType": "INTRON",
                                    "rank": 8,
                                    "rankTotal": 9,
                                }
                            ],
                        }
                    }
                ],
            },
            identifier="BAGE2_AUTOSOMAL_RECESSIVE",
            simplified_exomiser_result=defaultdict(dict),
            ranking_method="combinedScore",
        )

    def test_add_gene(self):
        self.assertEqual(self.simplified_exomiser_result.simplified_exomiser_result, {})
        self.simplified_exomiser_result.add_gene()
        self.assertEqual(
            self.simplified_exomiser_result.simplified_exomiser_result,
            {
                "BAGE2_AUTOSOMAL_RECESSIVE": {
                    "geneSymbol": "BAGE2",
                    "geneIdentifier": "ENSG00000187172",
                }
            },
        )

    def test_add_ranking_method_val(self):
        self.assertEqual(self.simplified_exomiser_result.simplified_exomiser_result, {})
        self.simplified_exomiser_result.add_ranking_method_val()
        self.assertEqual(
            self.simplified_exomiser_result.simplified_exomiser_result,
            {"BAGE2_AUTOSOMAL_RECESSIVE": {"combinedScore": 0.0026}},
        )

    def test_add_moi(self):
        self.assertEqual(self.simplified_exomiser_result.simplified_exomiser_result, {})
        self.simplified_exomiser_result.add_moi()
        self.assertEqual(
            self.simplified_exomiser_result.simplified_exomiser_result,
            {"BAGE2_AUTOSOMAL_RECESSIVE": {"modeOfInheritance": "AUTOSOMAL_RECESSIVE"}},
        )

    def test_add_contributing_variants(self):
        self.assertEqual(self.simplified_exomiser_result.simplified_exomiser_result, {})
        self.simplified_exomiser_result.add_contributing_variants()
        self.assertEqual(
            self.simplified_exomiser_result.simplified_exomiser_result,
            {
                "BAGE2_AUTOSOMAL_RECESSIVE": {
                    "contributingVariants": [
                        VariantData(chrom="21", pos=11021215, ref="T", alt="TA", gene="BAGE2"),
                        VariantData(chrom="21", pos=11038722, ref="C", alt="A", gene="BAGE2"),
                    ]
                }
            },
        )

    def test_create_simplified_result(self):
        self.assertEqual(self.simplified_exomiser_result.simplified_exomiser_result, {})
        self.simplified_exomiser_result.create_simplified_result()
        self.assertEqual(
            self.simplified_exomiser_result.simplified_exomiser_result,
            {
                "BAGE2_AUTOSOMAL_RECESSIVE": {
                    "geneSymbol": "BAGE2",
                    "geneIdentifier": "ENSG00000187172",
                    "combinedScore": 0.0026,
                    "modeOfInheritance": "AUTOSOMAL_RECESSIVE",
                    "contributingVariants": [
                        VariantData(chrom="21", pos=11021215, ref="T", alt="TA", gene="BAGE2"),
                        VariantData(chrom="21", pos=11038722, ref="C", alt="A", gene="BAGE2"),
                    ],
                }
            },
        )


class TestRankExomiserResult(unittest.TestCase):
    def setUp(self) -> None:
        self.combined_score_exomiser_result = RankExomiserResult(
            simplified_exomiser_result={
                "SPNS1_AUTOSOMAL_DOMINANT": {
                    "geneSymbol": "SPNS1",
                    "geneIdentifier": "ENSG00000169682",
                    "combinedScore": 0.8764321,
                    "modeOfInheritance": "AUTOSOMAL_DOMINANT",
                    "contributingVariants": [
                        VariantData(chrom="16", pos=28995541, ref="C", alt="A", gene="SPNS1")
                    ],
                },
                "ZNF804B_AUTOSOMAL_DOMINANT": {
                    "geneSymbol": "ZNF804B",
                    "geneIdentifier": "ENSG00000182348",
                    "combinedScore": 0.57778,
                    "modeOfInheritance": "AUTOSOMAL_DOMINANT",
                    "contributingVariants": [
                        VariantData(chrom="7", pos=88965159, ref="T", alt="G", gene="ZNF804B")
                    ],
                },
                "SMCO2_AUTOSOMAL_DOMINANT": {
                    "geneSymbol": "SMCO2",
                    "geneIdentifier": "ENSG00000165935",
                    "combinedScore": 0.0,
                    "modeOfInheritance": "AUTOSOMAL_DOMINANT",
                    "contributingVariants": [
                        VariantData(chrom="12", pos=27623658, ref="T", alt="A", gene="SMCO2")
                    ],
                },
                "MROH2B_AUTOSOMAL_DOMINANT": {
                    "geneSymbol": "MROH2B",
                    "geneIdentifier": "ENSG00000171495",
                    "combinedScore": 0.0,
                    "modeOfInheritance": "AUTOSOMAL_DOMINANT",
                    "contributingVariants": [
                        VariantData(chrom="5", pos=41055906, ref="C", alt="G", gene="MROH2B")
                    ],
                },
                "ZSCAN12_AUTOSOMAL_DOMINANT": {
                    "geneSymbol": "ZSCAN12",
                    "geneIdentifier": "ENSG00000158691",
                    "combinedScore": 0.23494,
                    "modeOfInheritance": "AUTOSOMAL_DOMINANT",
                    "contributingVariants": [
                        VariantData(chrom="6", pos=28359223, ref="C", alt="A", gene="ZSCAN12")
                    ],
                },
                "CASS4_AUTOSOMAL_DOMINANT": {
                    "geneSymbol": "CASS4",
                    "geneIdentifier": "ENSG00000087589",
                    "combinedScore": 0.57778,
                    "modeOfInheritance": "AUTOSOMAL_DOMINANT",
                    "contributingVariants": [
                        VariantData(chrom="20", pos=55026995, ref="G", alt="A", gene="CASS4")
                    ],
                },
            },
            ranking_method="combinedScore",
        )
        self.pvalue_exomiser_result = RankExomiserResult(
            simplified_exomiser_result={
                "SPNS1_AUTOSOMAL_DOMINANT": {
                    "geneSymbol": "SPNS1",
                    "geneIdentifier": "ENSG00000169682",
                    "pValue": 0.8764321,
                    "modeOfInheritance": "AUTOSOMAL_DOMINANT",
                    "contributingVariants": [
                        VariantData(chrom="16", pos=28995541, ref="C", alt="A", gene="SPNS1")
                    ],
                },
                "ZNF804B_AUTOSOMAL_DOMINANT": {
                    "geneSymbol": "ZNF804B",
                    "geneIdentifier": "ENSG00000182348",
                    "pValue": 0.57778,
                    "modeOfInheritance": "AUTOSOMAL_DOMINANT",
                    "contributingVariants": [
                        VariantData(chrom="7", pos=88965159, ref="T", alt="G", gene="ZNF804B")
                    ],
                },
                "SMCO2_AUTOSOMAL_DOMINANT": {
                    "geneSymbol": "SMCO2",
                    "geneIdentifier": "ENSG00000165935",
                    "pValue": 0.321354,
                    "modeOfInheritance": "AUTOSOMAL_DOMINANT",
                    "contributingVariants": [
                        VariantData(chrom="12", pos=27623658, ref="T", alt="A", gene="SMCO2")
                    ],
                },
                "MROH2B_AUTOSOMAL_DOMINANT": {
                    "geneSymbol": "MROH2B",
                    "geneIdentifier": "ENSG00000171495",
                    "pValue": 0.0112456,
                    "modeOfInheritance": "AUTOSOMAL_DOMINANT",
                    "contributingVariants": [
                        VariantData(chrom="5", pos=41055906, ref="C", alt="G", gene="MROH2B")
                    ],
                },
                "ZSCAN12_AUTOSOMAL_DOMINANT": {
                    "geneSymbol": "ZSCAN12",
                    "geneIdentifier": "ENSG00000158691",
                    "pValue": 0.0823742,
                    "modeOfInheritance": "AUTOSOMAL_DOMINANT",
                    "contributingVariants": [
                        VariantData(chrom="6", pos=28359223, ref="C", alt="A", gene="ZSCAN12")
                    ],
                },
                "CASS4_AUTOSOMAL_DOMINANT": {
                    "geneSymbol": "CASS4",
                    "geneIdentifier": "ENSG00000087589",
                    "pValue": 0.57778,
                    "modeOfInheritance": "AUTOSOMAL_DOMINANT",
                    "contributingVariants": [
                        VariantData(chrom="20", pos=55026995, ref="G", alt="A", gene="CASS4")
                    ],
                },
            },
            ranking_method="pValue",
        )

    def test_sort_exomiser_result(self):
        self.assertEqual(
            self.combined_score_exomiser_result.sort_exomiser_result(),
            [
                (
                    "SPNS1_AUTOSOMAL_DOMINANT",
                    {
                        "geneSymbol": "SPNS1",
                        "geneIdentifier": "ENSG00000169682",
                        "combinedScore": 0.8764321,
                        "modeOfInheritance": "AUTOSOMAL_DOMINANT",
                        "contributingVariants": [
                            VariantData(chrom="16", pos=28995541, ref="C", alt="A", gene="SPNS1")
                        ],
                    },
                ),
                (
                    "ZNF804B_AUTOSOMAL_DOMINANT",
                    {
                        "geneSymbol": "ZNF804B",
                        "geneIdentifier": "ENSG00000182348",
                        "combinedScore": 0.57778,
                        "modeOfInheritance": "AUTOSOMAL_DOMINANT",
                        "contributingVariants": [
                            VariantData(chrom="7", pos=88965159, ref="T", alt="G", gene="ZNF804B")
                        ],
                    },
                ),
                (
                    "CASS4_AUTOSOMAL_DOMINANT",
                    {
                        "geneSymbol": "CASS4",
                        "geneIdentifier": "ENSG00000087589",
                        "combinedScore": 0.57778,
                        "modeOfInheritance": "AUTOSOMAL_DOMINANT",
                        "contributingVariants": [
                            VariantData(chrom="20", pos=55026995, ref="G", alt="A", gene="CASS4")
                        ],
                    },
                ),
                (
                    "ZSCAN12_AUTOSOMAL_DOMINANT",
                    {
                        "geneSymbol": "ZSCAN12",
                        "geneIdentifier": "ENSG00000158691",
                        "combinedScore": 0.23494,
                        "modeOfInheritance": "AUTOSOMAL_DOMINANT",
                        "contributingVariants": [
                            VariantData(chrom="6", pos=28359223, ref="C", alt="A", gene="ZSCAN12")
                        ],
                    },
                ),
                (
                    "SMCO2_AUTOSOMAL_DOMINANT",
                    {
                        "geneSymbol": "SMCO2",
                        "geneIdentifier": "ENSG00000165935",
                        "combinedScore": 0.0,
                        "modeOfInheritance": "AUTOSOMAL_DOMINANT",
                        "contributingVariants": [
                            VariantData(chrom="12", pos=27623658, ref="T", alt="A", gene="SMCO2")
                        ],
                    },
                ),
                (
                    "MROH2B_AUTOSOMAL_DOMINANT",
                    {
                        "geneSymbol": "MROH2B",
                        "geneIdentifier": "ENSG00000171495",
                        "combinedScore": 0.0,
                        "modeOfInheritance": "AUTOSOMAL_DOMINANT",
                        "contributingVariants": [
                            VariantData(chrom="5", pos=41055906, ref="C", alt="G", gene="MROH2B")
                        ],
                    },
                ),
            ],
        )

    def test_sort_exomiser_result_pvalue(self):
        self.assertEqual(
            self.pvalue_exomiser_result.sort_exomiser_result_pvalue(),
            [
                (
                    "MROH2B_AUTOSOMAL_DOMINANT",
                    {
                        "geneSymbol": "MROH2B",
                        "geneIdentifier": "ENSG00000171495",
                        "pValue": 0.0112456,
                        "modeOfInheritance": "AUTOSOMAL_DOMINANT",
                        "contributingVariants": [
                            VariantData(chrom="5", pos=41055906, ref="C", alt="G", gene="MROH2B")
                        ],
                    },
                ),
                (
                    "ZSCAN12_AUTOSOMAL_DOMINANT",
                    {
                        "geneSymbol": "ZSCAN12",
                        "geneIdentifier": "ENSG00000158691",
                        "pValue": 0.0823742,
                        "modeOfInheritance": "AUTOSOMAL_DOMINANT",
                        "contributingVariants": [
                            VariantData(chrom="6", pos=28359223, ref="C", alt="A", gene="ZSCAN12")
                        ],
                    },
                ),
                (
                    "SMCO2_AUTOSOMAL_DOMINANT",
                    {
                        "geneSymbol": "SMCO2",
                        "geneIdentifier": "ENSG00000165935",
                        "pValue": 0.321354,
                        "modeOfInheritance": "AUTOSOMAL_DOMINANT",
                        "contributingVariants": [
                            VariantData(chrom="12", pos=27623658, ref="T", alt="A", gene="SMCO2")
                        ],
                    },
                ),
                (
                    "ZNF804B_AUTOSOMAL_DOMINANT",
                    {
                        "geneSymbol": "ZNF804B",
                        "geneIdentifier": "ENSG00000182348",
                        "pValue": 0.57778,
                        "modeOfInheritance": "AUTOSOMAL_DOMINANT",
                        "contributingVariants": [
                            VariantData(chrom="7", pos=88965159, ref="T", alt="G", gene="ZNF804B")
                        ],
                    },
                ),
                (
                    "CASS4_AUTOSOMAL_DOMINANT",
                    {
                        "geneSymbol": "CASS4",
                        "geneIdentifier": "ENSG00000087589",
                        "pValue": 0.57778,
                        "modeOfInheritance": "AUTOSOMAL_DOMINANT",
                        "contributingVariants": [
                            VariantData(chrom="20", pos=55026995, ref="G", alt="A", gene="CASS4")
                        ],
                    },
                ),
                (
                    "SPNS1_AUTOSOMAL_DOMINANT",
                    {
                        "geneSymbol": "SPNS1",
                        "geneIdentifier": "ENSG00000169682",
                        "pValue": 0.8764321,
                        "modeOfInheritance": "AUTOSOMAL_DOMINANT",
                        "contributingVariants": [
                            VariantData(chrom="16", pos=28995541, ref="C", alt="A", gene="SPNS1")
                        ],
                    },
                ),
            ],
        )

    def test_rank_results(self):
        self.assertEqual(
            self.combined_score_exomiser_result.rank_results(),
            {
                "SPNS1_AUTOSOMAL_DOMINANT": {
                    "geneSymbol": "SPNS1",
                    "geneIdentifier": "ENSG00000169682",
                    "combinedScore": 0.8764321,
                    "modeOfInheritance": "AUTOSOMAL_DOMINANT",
                    "contributingVariants": [
                        VariantData(chrom="16", pos=28995541, ref="C", alt="A", gene="SPNS1")
                    ],
                    "rank": 1,
                },
                "ZNF804B_AUTOSOMAL_DOMINANT": {
                    "geneSymbol": "ZNF804B",
                    "geneIdentifier": "ENSG00000182348",
                    "combinedScore": 0.57778,
                    "modeOfInheritance": "AUTOSOMAL_DOMINANT",
                    "contributingVariants": [
                        VariantData(chrom="7", pos=88965159, ref="T", alt="G", gene="ZNF804B")
                    ],
                    "rank": 2,
                },
                "CASS4_AUTOSOMAL_DOMINANT": {
                    "geneSymbol": "CASS4",
                    "geneIdentifier": "ENSG00000087589",
                    "combinedScore": 0.57778,
                    "modeOfInheritance": "AUTOSOMAL_DOMINANT",
                    "contributingVariants": [
                        VariantData(chrom="20", pos=55026995, ref="G", alt="A", gene="CASS4")
                    ],
                    "rank": 2,
                },
                "ZSCAN12_AUTOSOMAL_DOMINANT": {
                    "geneSymbol": "ZSCAN12",
                    "geneIdentifier": "ENSG00000158691",
                    "combinedScore": 0.23494,
                    "modeOfInheritance": "AUTOSOMAL_DOMINANT",
                    "contributingVariants": [
                        VariantData(chrom="6", pos=28359223, ref="C", alt="A", gene="ZSCAN12")
                    ],
                    "rank": 4,
                },
                "SMCO2_AUTOSOMAL_DOMINANT": {
                    "geneSymbol": "SMCO2",
                    "geneIdentifier": "ENSG00000165935",
                    "combinedScore": 0.0,
                    "modeOfInheritance": "AUTOSOMAL_DOMINANT",
                    "contributingVariants": [
                        VariantData(chrom="12", pos=27623658, ref="T", alt="A", gene="SMCO2")
                    ],
                    "rank": 5,
                },
                "MROH2B_AUTOSOMAL_DOMINANT": {
                    "geneSymbol": "MROH2B",
                    "geneIdentifier": "ENSG00000171495",
                    "combinedScore": 0.0,
                    "modeOfInheritance": "AUTOSOMAL_DOMINANT",
                    "contributingVariants": [
                        VariantData(chrom="5", pos=41055906, ref="C", alt="G", gene="MROH2B")
                    ],
                    "rank": 5,
                },
            },
        )
        self.assertEqual(
            self.pvalue_exomiser_result.rank_results(),
            {
                "MROH2B_AUTOSOMAL_DOMINANT": {
                    "geneSymbol": "MROH2B",
                    "geneIdentifier": "ENSG00000171495",
                    "pValue": 0.0112456,
                    "modeOfInheritance": "AUTOSOMAL_DOMINANT",
                    "contributingVariants": [
                        VariantData(chrom="5", pos=41055906, ref="C", alt="G", gene="MROH2B")
                    ],
                    "rank": 1,
                },
                "ZSCAN12_AUTOSOMAL_DOMINANT": {
                    "geneSymbol": "ZSCAN12",
                    "geneIdentifier": "ENSG00000158691",
                    "pValue": 0.0823742,
                    "modeOfInheritance": "AUTOSOMAL_DOMINANT",
                    "contributingVariants": [
                        VariantData(chrom="6", pos=28359223, ref="C", alt="A", gene="ZSCAN12")
                    ],
                    "rank": 2,
                },
                "SMCO2_AUTOSOMAL_DOMINANT": {
                    "geneSymbol": "SMCO2",
                    "geneIdentifier": "ENSG00000165935",
                    "pValue": 0.321354,
                    "modeOfInheritance": "AUTOSOMAL_DOMINANT",
                    "contributingVariants": [
                        VariantData(chrom="12", pos=27623658, ref="T", alt="A", gene="SMCO2")
                    ],
                    "rank": 3,
                },
                "ZNF804B_AUTOSOMAL_DOMINANT": {
                    "geneSymbol": "ZNF804B",
                    "geneIdentifier": "ENSG00000182348",
                    "pValue": 0.57778,
                    "modeOfInheritance": "AUTOSOMAL_DOMINANT",
                    "contributingVariants": [
                        VariantData(chrom="7", pos=88965159, ref="T", alt="G", gene="ZNF804B")
                    ],
                    "rank": 4,
                },
                "CASS4_AUTOSOMAL_DOMINANT": {
                    "geneSymbol": "CASS4",
                    "geneIdentifier": "ENSG00000087589",
                    "pValue": 0.57778,
                    "modeOfInheritance": "AUTOSOMAL_DOMINANT",
                    "contributingVariants": [
                        VariantData(chrom="20", pos=55026995, ref="G", alt="A", gene="CASS4")
                    ],
                    "rank": 4,
                },
                "SPNS1_AUTOSOMAL_DOMINANT": {
                    "geneSymbol": "SPNS1",
                    "geneIdentifier": "ENSG00000169682",
                    "pValue": 0.8764321,
                    "modeOfInheritance": "AUTOSOMAL_DOMINANT",
                    "contributingVariants": [
                        VariantData(chrom="16", pos=28995541, ref="C", alt="A", gene="SPNS1")
                    ],
                    "rank": 6,
                },
            },
        )


exomiser_result = [
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


class TestStandardiseExomiserResult(unittest.TestCase):
    def setUp(self) -> None:
        self.exomiser_result = StandardiseExomiserResult(exomiser_result, "combinedScore")

    def test_simplify_exomiser_result(self):
        self.assertEqual(
            self.exomiser_result.simplify_exomiser_result(),
            {
                "PLXNA1_AUTOSOMAL_DOMINANT": {
                    "geneSymbol": "PLXNA1",
                    "geneIdentifier": "ENSG00000114554",
                    "combinedScore": 0.0484,
                    "modeOfInheritance": "AUTOSOMAL_DOMINANT",
                    "contributingVariants": [
                        VariantData(chrom="3", pos=126730873, ref="G", alt="A", gene="PLXNA1")
                    ],
                },
                "PLXNA1_AUTOSOMAL_RECESSIVE": {
                    "geneSymbol": "PLXNA1",
                    "geneIdentifier": "ENSG00000114554",
                    "combinedScore": 0.046,
                    "modeOfInheritance": "AUTOSOMAL_RECESSIVE",
                    "contributingVariants": [
                        VariantData(chrom="3", pos=126730873, ref="G", alt="A", gene="PLXNA1"),
                        VariantData(chrom="3", pos=126741108, ref="G", alt="A", gene="PLXNA1"),
                    ],
                },
            },
        )

    def test_standardise_result(self):
        self.assertEqual(
            self.exomiser_result.standardise_result(),
            {
                "PLXNA1_AUTOSOMAL_DOMINANT": {
                    "geneSymbol": "PLXNA1",
                    "geneIdentifier": "ENSG00000114554",
                    "combinedScore": 0.0484,
                    "modeOfInheritance": "AUTOSOMAL_DOMINANT",
                    "contributingVariants": [
                        VariantData(chrom="3", pos=126730873, ref="G", alt="A", gene="PLXNA1")
                    ],
                    "rank": 1,
                },
                "PLXNA1_AUTOSOMAL_RECESSIVE": {
                    "geneSymbol": "PLXNA1",
                    "geneIdentifier": "ENSG00000114554",
                    "combinedScore": 0.046,
                    "modeOfInheritance": "AUTOSOMAL_RECESSIVE",
                    "contributingVariants": [
                        VariantData(chrom="3", pos=126730873, ref="G", alt="A", gene="PLXNA1"),
                        VariantData(chrom="3", pos=126741108, ref="G", alt="A", gene="PLXNA1"),
                    ],
                    "rank": 2,
                },
            },
        )
