books = ["The Shining", "It", "Misery"]

def done():
  if "Insomnia" in books:
    return "Very well!"
  else:
    raise RuntimeError("Don't forget to add 'Insomnia' to the book list!")
  