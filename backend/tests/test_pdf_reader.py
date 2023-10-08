from src.pdf_reader import read

def test_read():
  inp = './tests/dummy.pdf'
  exp = 'Opportunity Hack 2023 is great! This is after a couple of lines This is on next page!'
  act = read(inp)
  assert act == exp
