# IMPORTS
from .config import INDEX_NAME, URL, USER_NAME, KEY_PATH, PASSWORD
from .fernetKeyManager import FernetKeyManager
import time
from dataclasses import dataclass
from elasticsearch import Elasticsearch
from typing import List

# TODO (rohan): clean up unwanted funcs

# ENTITY CLASSS
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
        self.es = Elasticsearch([host], basic_auth=(username, password))
        self.index_name = index_name
        self.create_index()  # Create the Elasticsearch index if it doesn't exist

    def create_index(self):
        start_time = time.time()

        # Check if the index exists
        index_exists = self.es.indices.exists(index=self.index_name)

        # If the index does not exist, create it using the defined mappings
        if not index_exists:
            self.es.indices.create(index=self.index_name, ignore=400, body=MAPPINGS)
        else:
            print("Index already exists")
        
        print(self.get_time_elapsed(start_time, "Creating Index"))

    def insert_document(self, documentObj: ElasticSearchReqDoc):
        start_time = time.time()

        # Insert a document into the Elasticsearch index
        self.es.index(index=self.index_name, body=self.create_document(documentObj))
        print(self.get_time_elapsed(start_time, "Inserting Document"))

    def search(self, query):
        start_time = time.time()

        # Perform a search query in the Elasticsearch index
        response = self.es.search(index=self.index_name, body=query)
        print(self.get_time_elapsed(start_time, "Searching a Query"))
        return response['hits']['hits']

    def create_document(self, documentObj: ElasticSearchReqDoc):
        # Create a document to be inserted into the index
        return {
                'filename': documentObj.filename,
                'chunkId': documentObj.chunk_id,
                'fileType': documentObj.file_type,
                #'keywords': documentObj.keywords,
                #'location': documentObj.location,
                'dateCreated': documentObj.creation_date,
                'vectorEmbeddings': documentObj.feat_vec
                }

    def apply_filter(self, filter_field, filter_value, filter_type=None):
        """
        Apply a filter to an Elasticsearch search query based on filter_type and filter_value.
        
        Args:
            filter_field (str): The field to filter on.
            filter_value: The value to filter by.
            filter_type (str): The type of filter to apply.
            
        Returns:
            dict: The Elasticsearch filter query.
        """
        if filter_type == 'term':
            # Create a term filter query
            return {'term': {filter_field: filter_value}}
        elif filter_type == 'range':
            # Create a range filter query (assumes filter_value is a dictionary with 'gte' and 'lte' keys)
            return {'range': {filter_field: filter_value}}
        elif filter_type == 'prefix':
            # Create a prefix filter query
            return {'prefix': {filter_field: filter_value}}
        elif filter_type == 'wildcard':
            # Create a wildcard filter query
            return {'wildcard': {filter_field: filter_value}}
        elif filter_type == 'fuzzy':
            # Create a fuzzy filter query
            return {'fuzzy': {filter_field: filter_value}}
        else:
            # Create a default match filter query
            return {"match": {filter_field: filter_value}}

    def search_filters(self, filter_field, filter_value, filter_type=None):
        # Perform a search with a specified filter
        query = {"query": {}}
        query["query"] = self.apply_filter(filter_field, filter_value, filter_type)
        return self.search(query)

    def compare_vector_embeddings(self, query_vector):
        """
        Compare vector embeddings using a cosine similarity script_score query.
        
        Args:
            query_vector (list): The vector to compare with.
            
        Returns:
            list: List of results including score, filename, creation_date, and filetype.
        """
        start_time = time.time()

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
        ret = []
        fn_set = set()
        for res in results:
            _src = res['_source']
            if _src['filename'] in fn_set:
                continue  # TODO (rohan): in-future we will use the chunk ids for better UI
            fn_set.add(_src['filename'])
            ret.append({
                'score': res['_score'],
                'filename': _src['filename'],
                'creation_date': _src['dateCreated'],
                'filetype': _src['fileType'],
            })

        print(self.get_time_elapsed(start_time, "Comparing Vector Embeddings"))
        return ret

    def view_data(self):
        start_time = time.time()

        # View all data in the Elasticsearch index
        query = {"query": {"match_all": {}}}
        print(self.get_time_elapsed(start_time, "Viewing All Data"))
        return self.search(query)

    def view_top_n_items(self, n=10):
        # View the top N items from the Elasticsearch index
        query = {"query": {"match_all": {}}, "size": n}
        return self.search(query)

    def get_time_elapsed(self, starttime, functionCallName):
        end_time = time.time()
        elapsed_time = end_time - starttime
        
        # Convert elapsed_time to minutes, seconds, and milliseconds
        minutes, seconds = divmod(int(elapsed_time), 60)
        milliseconds = int((elapsed_time - int(elapsed_time)) * 1000)
        
        return f"Total Time taken for the {functionCallName}: {minutes:02}:{seconds:02}:{milliseconds:03}"
# # Example usage
ES = ElasticSearchClient(URL, USER_NAME, FernetKeyManager(KEY_PATH).decrypt_password(PASSWORD))
ES.view_data()
