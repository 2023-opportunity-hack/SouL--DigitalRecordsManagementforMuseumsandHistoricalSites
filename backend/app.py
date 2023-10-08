# Import necessary modules and classes
from src import text_vectorization
from src import controler_main as preprocessor
from database.elasticSearchClass import ES

import uvicorn
import os

from fastapi import FastAPI, UploadFile, HTTPException
from starlette.responses import FileResponse
from pydantic import BaseModel
from typing import List, Optional

# Create a FastAPI app
app = FastAPI()

# Specify the directory for storing uploaded files
STORAGE_DIR = './sfs/'
os.makedirs(STORAGE_DIR, exist_ok=True)

# Define the root endpoint


@app.get('/')
def root():
    return {'msg': 'hello world'}

# Define the response model for search results


class SearchResponse(BaseModel):
    filename: str
    rank: int
    creation_date: str  # MM/DD/YYYY
    filetype: str

# Define the /search endpoint for searching documents


@app.get('/search')
def search(
    query: str,
    filetype: Optional[str] = None,
    sort_by: Optional[str] = None,
    limit: int = 10,
    offset: int = 0,
) -> List[SearchResponse]:
    # Preprocess the query
    query = query.strip()

    # Get query embeddings
    query_vec = text_vectorization.vectorize(query).squeeze().tolist()

    # Search in ElasticSearch, which will return a list of filenames
    result = ES.compare_vector_embeddings(query_vec)

    # TODO (rohan): Query PostgreSQL for metadata
    # Add rank to the filenames and return the search results
    ret = []
    for i, res in enumerate(result):
        ret.append({
            'filename': res['filename'],
            'rank': i+1,
            'filetype': res['filetype'],
            'creation_date': res['creation_date']
        })
    return ret

# Define the /uploadfile endpoint for uploading documents


@app.post('/uploadfile', status_code=200)
def upload(file: UploadFile):
    filename = file.filename.split('/')[-1]  # Extract filename from the path
    save_fn = os.path.join(STORAGE_DIR, filename)

    # Check if the file already exists
    if os.path.exists(save_fn):
        raise HTTPException(
            status_code=403, detail=f'\'{filename}\' already exists')

    # Save the uploaded file
    with open(save_fn, 'wb') as f:
        f.write(file.file.read())

    # Preprocess the uploaded file
    preprocessor.preprocess(save_fn)

    return {'filename': filename}

# Define the /getfile endpoint for retrieving documents


@app.get('/getfile')
def getfile(filename: str):
    save_fn = os.path.join(STORAGE_DIR, filename)

    # Determine the media type based on file extension
    audio_exts = ['m4a', 'mp3', 'wav']
    video_exts = ['mp4']
    pdf_exts = ['pdf']
    img_exts = ['jpg', 'jpeg', 'png']

    file_ext = filename.split('.')[-1]
    if file_ext in pdf_exts:
        media_type = 'application/pdf'
    elif file_ext in video_exts:
        media_type = 'video/mp4'
    elif file_ext in audio_exts:
        media_type = f'audio/mp3'
    elif file_ext in img_exts:
        media_type = f'image/jpeg'
    else:
        raise NotImplementedError(
            f'\'{file_ext}\' extension media type not implemented')

    # TODO (rohan): Streaming response
    return FileResponse(save_fn, media_type=media_type, filename=filename)

# TODO (rohan): Delete file


# Run the FastAPI app using uvicorn
if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='localhost')
