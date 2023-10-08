from elasticsearch import Elasticsearch

from config import INDEX_NAME, URL, USER_NAME, KEY_PATH, PASSWORD
from fernetKeyManager import FernetKeyManager

class ElasticSearchClient:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password
        self.index = INDEX_NAME
        self.es = Elasticsearch([host], basic_auth=(username, password))

    def create_index(self, mappings=None):
        # Check if the index exists
        index_exists = self.es.indices.exists(index=self.index)

        # If the index does not exist, create it
        if not index_exists:
            self.es.indices.create(index=self.index, ignore=400, body=mappings)
        else:
            print("Index already exists")

    def insert_document(self, documentObj):
        self.es.index(index=self.index, body=self.create_document(documentObj))

    def search(self, query):
        response = self.es.search(index=self.index, body=query)
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


    def view_data(self):
        query = {"query": {"match_all": {}}}
        return self.search(query)

    def view_top_n_items(self, n=10):
        query = {"query": {"match_all": {}}, "size": n}
        return self.search(query)



# TESTING
fernetObj = FernetKeyManager(KEY_PATH)
es = ElasticSearchClient(URL, USER_NAME, fernetObj.decrypt_password(PASSWORD))
es.create_index()


from datetime import datetime

class DocumentObj:
    def __init__(self, filename, chunk_id, file_type, keywords, location, date_created, vector_embeddings):
        self.filename = filename
        self.chunk_id = chunk_id
        self.fileType = file_type
        self.keywords = keywords
        self.location = location
        self.dateCreated = date_created
        self.vectorEmbeddings = vector_embeddings

# Initialize an empty list to store the generated document objects
document_objects = []

# Define the number of document objects you want to create
num_documents = 500  # Change this to the desired number of objects

def random_date():
    import random
    from datetime import datetime, timedelta

    # Define the start and end dates for the date range
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31)

    # Calculate the range of days between the start and end dates
    date_range = end_date - start_date

    # Generate a random number of days within the date range
    random_days = random.randint(0, date_range.days)

    # Calculate the random date by adding the random number of days to the start date
    random_date = start_date + timedelta(days=random_days)

    # Print the random date
    return random_date.strftime("%Y-%m-%d")

# # Create document objects in a loop with incremental values
# for i in range(num_documents):
#     filename = f"file_{i}.txt"
#     chunk_id = i
#     file_type = "txt"
#     keywords = [f"keyword_{i}", f"keyword_{i+1}"]
#     location = f"location_{i}"
#     date_created =random_date() # Format date correctly
#     vector_embeddings = [0.1 * i, 0.2 * i, 0.3 * i]  # Adjust values as needed

#     document = DocumentObj(filename, chunk_id, file_type, keywords, location, date_created, vector_embeddings)
#     es.insert_document(document)  # Use the dictionary directly

top_items = es.view_data()
print(len(top_items))
