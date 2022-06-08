from datetime import datetime

from opentelemetry.instrumentation.elasticsearch import ElasticsearchInstrumentor

import elasticsearch
from abstractTrace import AbstractTrace

ElasticsearchInstrumentor().instrument()


class ElasticTrace(AbstractTrace):
    def __init__(self):
        self.es = elasticsearch.Elasticsearch("http://localhost:9200")

    def testTrace(self):
        doc = {
            'author': 'kimchy',
            'text': 'Elasticsearch: cool. bonsai cool.',
            'timestamp': datetime.now(),
        }
        resp = self.es.index(index="test-index", id=1, document=doc)
        print(resp['result'])

        resp = self.es.get(index="test-index", id=1)
        print(resp['_source'])

        self.es.indices.refresh(index="test-index")

        resp = self.es.search(index="test-index", query={"match_all": {}})
        print("Got %d Hits:" % resp['hits']['total']['value'])
        for hit in resp['hits']['hits']:
            print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
