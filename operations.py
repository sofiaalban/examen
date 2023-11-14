def obtener_representacion_byte(caracter):
  representacion_byte = ' '.join(format(b, '08b') for b in caracter.encode())
  return representacion_byte
