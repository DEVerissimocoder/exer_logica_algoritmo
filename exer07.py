def dobro_area_quadrado(lado):
    """
    Calcula o dobro da área de um quadrado dado o lado.
    :param lado: Lado do quadrado
    :return: Dobro da área do quadrado
    """
    area = lado * lado
    return 2 * area
# Solicita o lado do quadrado ao usuário
lado = float(input("Informe o lado do quadrado: "))
print(dobro_area_quadrado(lado))
    