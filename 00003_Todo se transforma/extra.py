libros = ["Ensayo sobre la ceguera", "Socorro", "Mi planta naranja lima"]

def listo():
  if "Fundación" in libros:
    return "¡Muy bien!"
  else:
    raise RuntimeError("No te olvides de agregar 'Fundación' a la lista de libros")
  