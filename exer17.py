tamanho = float(input("informe o tamanho em metros quadrados"))
qtd_litros = tamanho/6
qtd_latas=qtd_litros+(10/100*qtd_litros)/18
qtd_galoes=qtd_litros/3,6



print(f' """ 
	---------------------------------------------------------
	LATAS: {qtd_latas*80} / 1 (uma) lata custa: R$ 80,00
	---------------------------------------------------------
	GALÕES: {qtd_galoes*25} /  1 (um) Galão custa: R$ 25,00
	 """)
if (qtd_latas - int(qtd_latas))>0:
	qtd_latas = qtd_latas- (qtd_latas-int(qtd_latas))+1
if (qtd_latas%18 )
