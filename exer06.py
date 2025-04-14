def area_circulo(raio):
    """
    Calcula a área de um círculo dado o raio.
    :param raio: Raio do círculo
    :return: Área do círculo
    """
    pi = 3.14159
    area = pi * (raio ** 2)
    return area
# Solicita o raio do círculo ao usuário
raio = float(input("Informe o raio do círculo: "))
print(area_circulo(raio))