# our scripts
from src import text_vectorization

# 3rd-party libs
import uvicorn
import os

from fastapi import FastAPI, UploadFile, HTTPException
from starlette.responses import FileResponse
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()
STORAGE_DIR = './sfs/'
os.makedirs(STORAGE_DIR, exist_ok=True)
# TODO (rohan): add CORS middleware

@app.get('/')
def root():
  return {'msg': 'hello world'}

# TODO (rohan): query api
class SearchResponse(BaseModel):
  filename: str
  rank: int

@app.get('/search')
def search(
  query: str,
  date: Optional[str]=None,
  filetype: Optional[str]=None,
  limit: int=10,
  offset: int=0
) -> List[SearchResponse]:
  # preprocess query
  query = query.strip()
  # get query embeddings
  query_vec = text_vectorization.vectorize(query).squeeze()
  # search in elastic search > will return list of filenames
  #result = elastic_search.retrieve(query_vec)
  # TODO (rohan): query postgres for metadata
  # add rank to the filenames & return
  '''
  ret = []
  for i, fn in enumerate(result):
    ret.append({
      'filename': fn,
      'rank': i+1
    })
  return ret
  '''
    
  return [{'filename': 'hello.world', 'rank':1}]

@app.post('/uploadfile', status_code=200)
def upload(file: UploadFile):
  save_fn = os.path.join(STORAGE_DIR, file.filename)
  if os.path.exists(save_fn): raise HTTPException(status_code=403, detail=f'\'{file.filename}\' already exists')
  with open(save_fn, 'wb') as f: f.write(file.file.read())
  # TODO (rohan): trigger controller service
  return {'filename': file.filename}

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
  else: raise NotImplementedError(f'\'{file_ext}\' extension media type not implemented')

  # TODO (rohan): streaming response
  return FileResponse(save_fn, media_type=media_type, filename=filename)

# TODO (rohan): delete file


if __name__ == '__main__':
  uvicorn.run(app, port=8080, host='localhost')
