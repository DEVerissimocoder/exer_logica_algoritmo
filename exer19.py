num1 = int(input("digite um número "))
num2 = int(input("digite outro número "))

maior=0
menor=0

if num1>num2:
    maior=num1
    menor=num2
else:
    maior=num2
    menor=num1

print(f"maior: {maior}, menor: {menor}")