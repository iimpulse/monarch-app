import pytest


@pytest.fixture
def histopheno_response():
    return {
        "responseHeader": {
            "QTime": 1,
            "params": {
                "facet.query": [
                    'object_closure:"HP:0000924"',
                    'object_closure:"HP:0000707"',
                    'object_closure:"HP:0000152"',
                    'object_closure:"HP:0001574"',
                    'object_closure:"HP:0000478"',
                    'object_closure:"HP:0001626"',
                    'object_closure:"HP:0001939"',
                    'object_closure:"HP:0000119"',
                    'object_closure:"HP:0025031"',
                    'object_closure:"HP:0002664"',
                    'object_closure:"HP:0001871"',
                    'object_closure:"HP:0002715"',
                    'object_closure:"HP:0000818"',
                    'object_closure:"HP:0003011"',
                    'object_closure:"HP:0002086"',
                    'object_closure:"HP:0000598"',
                    'object_closure:"HP:0003549"',
                    'object_closure:"HP:0001197"',
                    'object_closure:"HP:0001507"',
                    'object_closure:"HP:0000769"',
                ],
                "mm": "100%",
                "q": "*:*",
                "defType": "edismax",
                "facet_min_count": "1",
                "start": "0",
                "q.op": "AND",
                "fq": "subject_closure:MONDO\\:0020121",
                "rows": "0",
                "facet": "true",
            },
        },
        "response": {"num_found": 4361, "start": 0, "docs": []},
        "facet_counts": {
            "facet_fields": {},
            "facet_queries": {
                'object_closure:"HP:0000924"': 472,
                'object_closure:"HP:0000707"': 1077,
                'object_closure:"HP:0000152"': 583,
                'object_closure:"HP:0001574"': 47,
                'object_closure:"HP:0000478"': 289,
                'object_closure:"HP:0001626"': 178,
                'object_closure:"HP:0001939"': 215,
                'object_closure:"HP:0000119"': 44,
                'object_closure:"HP:0025031"': 143,
                'object_closure:"HP:0002664"': 149,
                'object_closure:"HP:0001871"': 177,
                'object_closure:"HP:0002715"': 22,
                'object_closure:"HP:0000818"': 25,
                'object_closure:"HP:0003011"': 1686,
                'object_closure:"HP:0002086"': 150,
                'object_closure:"HP:0000598"': 28,
                'object_closure:"HP:0003549"': 161,
                'object_closure:"HP:0001197"': 21,
                'object_closure:"HP:0001507"': 32,
                'object_closure:"HP:0000769"': 1,
            },
        },
    }
