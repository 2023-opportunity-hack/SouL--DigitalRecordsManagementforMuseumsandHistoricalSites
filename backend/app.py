# our scripts
from src import text_vectorization
from src import controler_main as preprocessor
from database.elasticSearchClass import ES

# 3rd-party libs
import uvicorn
import os

from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse
from pydantic import BaseModel
from typing import List, Optional

# TODO (rohan): add constants to one file
# TODO (rohan): use a debug var
app = FastAPI()

# filesystem where we dump the object files
STORAGE_DIR = './sfs/'
os.makedirs(STORAGE_DIR, exist_ok=True)
# TODO (rohan): add CORS middleware
app.add_middleware(
  CORSMiddleware,
  allow_origins=['*'],
  allow_credentials=True,
  allow_methods=['*'],
  allow_headers=['*'],
)

@app.get('/')
def root():
  return {'msg': 'hello world'}

# TODO (rohan): query api
class SearchResponse(BaseModel):
  filename: str
  rank: int
  creation_date: str  ## MM/DD/YYYY
  filetype: str

# TODO (rohan): REDIS caching

@app.get('/search')
def search(
  query: str,
  filetype: Optional[str]=None,
  sort_by: Optional[str]=None,
  sort_order: Optional[str]=None,
  # TODO (rohan): using limit and offset for pagination
  limit: int=10,
  offset: int=0,
  # TODO (rohan)
  # total_results: int  # len of result
  # sort_by: str
  # start_date: Date obj  # creation date
  # end_date: Date obj  # creation date
) -> List[SearchResponse]:
  # preprocess query
  query = query.strip()
  # get query embeddings
  query_vec = text_vectorization.vectorize(query).squeeze().tolist()
  # search in elastic search > will return list of filenames
  result = ES.compare_vector_embeddings(query_vec)
  # TODO (rohan): query postgres for metadata
  # add rank to the filenames & return
  ret = []
  for i, res in enumerate(result):
    ret.append({
      'filename': res['filename'],
      'rank': i+1,
      'filetype': res['filetype'],
      'creation_date': res['creation_date']
    })
  return ret
    
  #return [{'filename': 'hello.world', 'rank':1}]

@app.post('/uploadfile', status_code=200)
def upload(file: UploadFile):
  filename = file.filename.split('/')[-1]  # we don't want the user to specify path, just a filename.extension
  save_fn = os.path.join(STORAGE_DIR, filename)
  if os.path.exists(save_fn): raise HTTPException(status_code=403, detail=f'\'{filename}\' already exists')
  with open(save_fn, 'wb') as f: f.write(file.file.read())
  preprocessor.preprocess(save_fn)
  return {'filename': filename}

@app.get('/getfile')
def getfile(filename: str):
  save_fn = os.path.join(STORAGE_DIR, filename)

  # determine media type
  audio_exts = ['m4a', 'mp3', 'wav']
  video_exts = ['mp4']
  pdf_exts = ['pdf']
  img_exts = ['jpg', 'jpeg', 'png']

  file_ext = filename.split('.')[-1]
  if file_ext in pdf_exts: media_type = 'application/pdf'
  elif file_ext in video_exts: media_type = 'video/mp4'
  elif file_ext in audio_exts: media_type = f'audio/mp3'
  elif file_ext in img_exts: media_type = f'image/jpeg'
  else:
    media_type = 'application/octet-stream'
    #raise NotImplementedError(f'\'{file_ext}\' extension media type not implemented')

  # TODO (rohan): streaming response
  return FileResponse(save_fn, media_type=media_type, filename=filename)

# TODO (rohan): delete file


if __name__ == '__main__':
  uvicorn.run(app, port=8080, host='0.0.0.0')
