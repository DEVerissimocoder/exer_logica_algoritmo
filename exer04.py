nota = 0
soma_notas=0
for i in range(0,4):
    nota=float(input(f" digite a {i+1}ª nota "))
    soma_notas+=nota

print(f"media: {soma_notas/4}")