from elasticsearch import Elasticsearch

# Define the Elasticsearch server's address and authentication credentials
elasticsearch_host = 'http://localhost:9200'  # Replace with your Elasticsearch server's address
username = 'test'  # Replace with your Elasticsearch username
password = 'test123'  # Replace with your Elasticsearch password

# Create an Elasticsearch instance with authentication
es = Elasticsearch([elasticsearch_host], basic_auth=(username, password))

# Test the connection
if es.ping():
    print("Connected to Elasticsearch")
else:
    print("Connection failed")

# Create an index (you can customize the settings and mappings as needed)
index_name = 'search_items'  # Define your index name
if not es.indices.exists(index=index_name):
    es.indices.create(index=index_name, ignore=400)

# Sample document
document = {
    'Filename': 'example.pdf',
    'Paragraph_id': 1,
    'FileType': 'pdf',
    'tags': ['history', 'documents'],
    'Vector_embeddings': [0.17, 0.5, 0.4]
}

# Index the document
es.index(index=index_name, document=document)

# Define your query (e.g., match all documents)
query = {
    "query": {
        "match": {
        "tags": "history"
        }
    }
}

# Execute the query and retrieve data
response = es.search(index=index_name, body=query)

# Extract and print the retrieved documents
for hit in response['hits']['hits']:
    document = hit['_source']
    print(document)