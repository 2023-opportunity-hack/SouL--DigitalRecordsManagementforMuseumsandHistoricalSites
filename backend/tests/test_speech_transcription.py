from src.speech_transcription import transcribe

def test_transcribe():
  inp = './tests/audio.m4a'
  exp = 'Hey Siri, set a timer for 5 minutes.'
  act = transcribe(inp)
  assert act == exp
