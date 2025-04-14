dicion={}
numeros=[]
def numeros_inteiros(dicionario):
    print(dicionario)

opcao=1
while opcao!=0:
    opcao = int(input("""
                qualquer numero - continuar informando numeros
                0- parar de informar números
                """))
    if (opcao==0):
        break
    numero=float(input("numero "))
    numeros.append(numero)
    if "numero" in dicion:
        dicion["numero"] += numero
    else:
        dicion["numero"] = numero
print(numeros_inteiros(dicion))