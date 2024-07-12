cipher = "ERVV GDB BRX WKHB"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 

for shift in range(1,26):
  plaintext = ''
  for char in cipher:
    if char in alphabet:
      position = alphabet.index(char)
      og_position = (position - shift) % 26  
      plaintext += alphabet[og_position]
    else:
      plaintext += char

  print("Numero de salto %s, el mensaje descifrado es: %s" % (shift, plaintext))

  # Se corrige el codigo 