def converte_para_cm(metros):
    """
    Converte metros para centímetros.
    
    :param metros: valor em metros
    :return: valor em centímetros
    """
    return metros * 100
metros=int(input("informe o valor em metros: "))
print(converte_para_cm(metros))