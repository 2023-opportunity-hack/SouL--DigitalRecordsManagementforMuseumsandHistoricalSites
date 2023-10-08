from .config import INDEX_NAME, URL, USER_NAME, KEY_PATH, PASSWORD
from .fernetKeyManager import FernetKeyManager

from dataclasses import dataclass
from elasticsearch import Elasticsearch
from typing import List

@dataclass
class ElasticSearchReqDoc:
  filename: str
  chunk_id: int
  file_type: str
  #keywords: List[str]
  creation_date: str  # MM/DD/YYYY
  feat_vec: List[float]

MAPPINGS = {
  "mappings": {
    "properties": {
      "filename": {
        "type": "keyword"
      },
      "chunkId": {
        "type": "keyword"
      },
      "fileType": {
        "type": "keyword"
      },
      #"keywords": {
      #  "type": "keyword"
      #},
      #"location": {
      #  "type": "geo_point"
      #},
      "dateCreated": {
        "type": "date",
        "format": "MM/dd/yyyy"
      },
      "vectorEmbeddings": {
        "type": "dense_vector",
        "dims": 768,
      }
    }
  }
}

class ElasticSearchClient:
    def __init__(self, host, username, password, index_name=INDEX_NAME):
        self.host = host
        self.username = username
        self.password = password
        print(self.password)
        self.es = Elasticsearch([host], basic_auth=(username, password))
        self.index_name = index_name
        self.create_index()

    def create_index(self):
        # Check if the index exists
        index_exists = self.es.indices.exists(index=self.index_name)

        # If the index does not exist, create it
        if not index_exists:
            tmp = self.es.indices.create(index=self.index_name, ignore=400, body=MAPPINGS)
            print(tmp)
        else:
            print("Index already exists")

    def insert_document(self, documentObj: ElasticSearchReqDoc):
        self.es.index(index=self.index_name, body=self.create_document(documentObj))

    def search(self, query):
        response = self.es.search(index=self.index_name, body=query)
        return response['hits']['hits']

    def create_document(self, documentObj: ElasticSearchReqDoc):
        return {
            'filename': documentObj.filename,
            'chunkId': documentObj.chunk_id,
            'fileType': documentObj.file_type,
            #'keywords': documentObj.keywords,
            #'location': documentObj.location,
            'dateCreated': documentObj.creation_date,
            'vectorEmbeddings': documentObj.feat_vec
            }
    

    def apply_filter( filter_field,filter_value,filter_type=None):
        """
        Apply a filter to an Elasticsearch search query based on filter_type and filter_value.
        
        Args:
            search (elasticsearch_dsl.Search): The Elasticsearch search object.
            filter_type (str): The type of filter to apply.
            filter_value: The value to filter by.
            
        Returns:
            elasticsearch_dsl.Search: The updated Elasticsearch search query.
        """
        

        if filter_type == 'term':
            # 'term': {'field_name': 'exact_term'}
            return {'term': {filter_field: filter_value}}
        
        elif filter_type == 'range':
            # Assuming filter_value is a dictionary with 'gte' and 'lte' keys
            # 'range': {'field_name': {'gte': 10, 'lte': 20}}
            return {'range': {filter_field: filter_value}}
        
        elif filter_type == 'prefix':
            # 'prefix': {'field_name': 'prefix'}
            return {'prefix': {filter_field: filter_value}}
        
        elif filter_type == 'wildcard':
            # 'wildcard': {'field_name': 'wildcard*'}
            return {'wildcard': {filter_field: filter_value}}
        
        elif filter_type == 'fuzzy':
            # 'fuzzy': {'field_name': 'approximate_term'}
            return {'fuzzy': {filter_field: filter_value}}
        
        else:
            return {"match": {filter_field: filter_value}}


    def search_filters(self,filter_field, filter_value,filter_type=None):
        query = {"query":{}}
        query["query"] = self.apply_filter(filter_field, filter_value,filter_type)
        return self.search(query)


    def compare_vector_embeddings(self, query_vector):
        query = {
            'query': {
                'script_score': {
                    'query': {
                        'match_all': {}
                    },
                    'script': {
                        'source': 'cosineSimilarity(params.queryVector, doc["vectorEmbeddings"]) + 1.0',
                        'params': {
                            'queryVector': query_vector
                        }
                    }
                }
            }
        }

        # Execute the similarity query
        results = self.search(query)
        print(results)
        ret = []
        fn_set = set()
        for res in results:
          _src = res['_source']
          if _src['filename'] in fn_set: continue  # TODO (rohan): in-future we will use the chunk ids for better UI
          fn_set.add(_src['filename'])
          ret.append({
            'score': res['_score'],
            'filename': _src['filename'],
            'creation_date': _src['dateCreated'],
            'filetype': _src['fileType'],
          })
        return ret


    def view_data(self):
        query = {"query": {"match_all": {}}}
        return self.search(query)

    def view_top_n_items(self, n=10):
        query = {"query": {"match_all": {}}, "size": n}
        return self.search(query)


ES = ElasticSearchClient(URL, USER_NAME, FernetKeyManager(KEY_PATH).decrypt_password(PASSWORD))
