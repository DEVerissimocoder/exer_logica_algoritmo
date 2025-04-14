
lista=[]
def numeros_inteiros(lista):    
    dicionario={"produto": lista[0]*2*lista[1]/2,
                "soma": (lista[0]*3)+lista[2],
                "potencia":lista[2]**3
                }
    return dicionario

opcao=1
while opcao!=0:
    numero=float(input("numero "))
    lista.append(numero)    
    opcao = int(input("""
                qualquer numero - continuar informando numeros
                0- parar de informar números
                """))
    
print(numeros_inteiros(lista))