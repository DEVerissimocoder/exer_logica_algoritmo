
multa=0
excesso=0

peso=float(input("informe o peso "))
if peso>50:
        excesso=peso - 50
        multa=excesso*4
        print(f"multa de {multa} e excesso de {excesso}kg")
else:
        print("peso normal")