lista = ["Maria", "Helena", "Luiz"]

nome, nome2, nome3 = lista

print(nome)

nome, *resto = lista

print(resto)

nome, *_ = lista

print(_)

_, nome2, *_ = lista

print(nome2, _)