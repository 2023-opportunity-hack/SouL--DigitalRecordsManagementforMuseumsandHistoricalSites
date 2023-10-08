from elasticsearch import Elasticsearch

from config import INDEX_NAME, URL, USER_NAME, KEY_PATH, PASSWORD
from database.fernetKeyManager import FernetKeyManager

class ElasticSearchClient:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password
        self.es = Elasticsearch([host], basic_auth=(username, password))

    def create_index(self, index_name, mappings):
        # Check if the index exists
        index_exists = self.es.indices.exists(index=index_name)

        # If the index does not exist, create it
        if not index_exists:
            self.es.indices.create(index=index_name, ignore=400, body=mappings)
        else:
            print("Index already exists")

    def insert_document(self, index_name, documentObj):
        self.es.index(index=index_name, body=self.create_document(documentObj))

    def search(self, index_name, query):
        response = self.es.search(index=index_name, body=query)
        return response['hits']['hits']

    def create_document(self, documentObj):
        return {
            'filename': documentObj.filename,
            'chunkId': documentObj.chunk_id,
            'fileType': documentObj.fileType,
            'keywords': documentObj.keywords,
            'location': documentObj.location,
            'dateCreated': documentObj.dateCreated,
            'vectorEmbeddings': documentObj.vectorEmbeddings
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
        return self.search(INDEX_NAME, query)


    def compare_vector_embeddings(self, index_name, query_vector):
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
        results = self.search(index=index_name, body=query)

        # Process and print the results
        return results['hits']['hits']


    def view_data(self, index_name):
        query = {"query": {"match_all": {}}}
        return self.search(index_name, query)

    def view_top_n_items(self, index_name, n=10):
        query = {"query": {"match_all": {}}, "size": n}
        return self.search(index_name, query)


fernetObj = FernetKeyManager(KEY_PATH)

es = ElasticSearchClient(URL, USER_NAME, fernetObj.decrypt_password(PASSWORD))

es.create_index(INDEX_NAME, {
  "mappings": {
    "properties": {
      "_id": {
        "type": "keyword"
      },
      "filename": {
        "type": "keyword"
      },
      "chunkId": {
        "type": "keyword"
      },
      "fileType": {
        "type": "keyword"
      },
      "keywords": {
        "type": "keyword"
      },
      "location": {
        "type": "geo_point"
      },
      "dateCreated": {
        "type": "date"
      },
      "vectorEmbeddings": {
        "type": "dense_vector"
      }
    }
  }
})
es.insert_document(INDEX_NAME, '1', {"field1": "value1"})

top_items = es.view_top_n_items(INDEX_NAME, n=5)

