## Types of media:
- Text
- Image -> Video
- Audio
- Text in Image

## Types of file:
- PDFs
- .docx & similar word documents
- .jpg & .png & other image files
- .mp3 files for audio
- .mp4 files for audio & video

## Feature Extraction:
- text:
  - Keywords using LDA
  - ~~BERT Feature embeddings~~
- image:
  - text using OCR
  - ~~caption using CLIP~~
  - ~~ResNet50 feature embeddings~~
  - keyword tags
- audio:
  - ~~speech-to-text using Whisper~~
  - audio embeddings?

## Search Engine Optimization (UI/UX)
- Summary/Answer highlighting for query, just how google does it!


## Data
- Image:
  - image object
  - image filename
  - created_on
  - tags (strings)
  - caption <- Thinh
  - feature vector

## services
[ ] Image(filename) loading service
[ ] Storage Service
  - get file
  - add file
    - hash the filename
    - return 403 if duplicate filename exists
    - call controller service (event trigger)
    - return 200 if success
  - delete file
[ ] API
  - query
  related storage service
    - add file
    - get file
    - read file

## Bugs
- ~~".doc" file~~
- ~~"RALwinter.JPG"~~
- ~~add support "wpd"~~
- ~~Thumbs.db~~
- Error handling
