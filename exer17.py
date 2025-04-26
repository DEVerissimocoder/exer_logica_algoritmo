tamanho = float(input("informe o tamanho em metros quadrados\n"))
qtd_litros = tamanho/6
qtd_latas=(qtd_litros+(10/100*qtd_litros))/18
qtd_galoes=(qtd_litros+(10/100*qtd_litros))/3.6

qtd_latas = qtd_latas - (qtd_latas - int(qtd_latas))+1
qtd_galoes = qtd_galoes - (qtd_galoes - int(qtd_galoes))+1
print(f"""SEPARADO:
	   ------------------------------------------------------
	   LATAS: {qtd_latas}- a pagar: {qtd_latas*80}, 
	   ------------------------------------------------------
	   GALOES: {qtd_galoes} - a pagar: {qtd_galoes*25}
		-----------------------------------------------------\n
		""")

if (qtd_litros<=18):
	if(qtd_litros<=(3*3.6)):
		qtd_latas=0
		
		print(f"""MISTURADO:
	   ------------------------------------------------------
	   LATAS: {qtd_latas}- a pagar: {qtd_latas*80}, 
	   ------------------------------------------------------
	   GALOES: {qtd_galoes} - a pagar: {qtd_galoes*25}
		-----------------------------------------------------\n
		""")
	else:
		qtd_latas=1
		qtd_galoes=0
		print(f"""MISTURADO:
	   ------------------------------------------------------
	   LATAS: {qtd_latas}- a pagar: {qtd_latas*80}, 
	   ------------------------------------------------------
	   GALOES: {qtd_galoes} - a pagar: {qtd_galoes*25}
		-----------------------------------------------------\n
		""")
else:
	resto=qtd_litros%18
	qtd_galoes=resto/3.6
	qtd_galoes=int(qtd_galoes)+1
	qtd_latas-=1
	print(f"""MISTURADO:
	   ------------------------------------------------------
	   LATAS: {qtd_latas}- a pagar: {qtd_latas*80}, 
	   ------------------------------------------------------
	   GALOES: {qtd_galoes} - a pagar: {qtd_galoes*25}
		-----------------------------------------------------\n
		""")
