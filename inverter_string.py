def inverte(texto):
  palavraInvertida = ""
  i = len(texto) - 1
  while i >= 0:
    palavraInvertida += texto[i]
    i = i - 1
  print(palavraInvertida)

inverte("Bom dia, como você dormiu?")