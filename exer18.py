tamanho= float(input("informe o tamanho do arquivo "))
velocidade= float(input("informe a velocidade do link de internet "))

bits_v=velocidade*10**6
bits_t=tamanho*1024**2*8
bits_s=bits_t/bits_v

minutos=bits_s/60
segundos= (minutos-int(minutos))*60
print(f'''O DOWNLOAD LEVARÁ: {int(minutos)} MINUTOS e 
      {int(segundos)} SEGUNDOS''')
