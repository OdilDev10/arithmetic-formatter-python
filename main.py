

import re
import sys
global y 

lineas = "------"



def arithmetic_arranger(operaciones, respuestas = True):
	global y

	for x in operaciones:
		y = x.split()		
		print("  ",y[0],end="     ")
		
	print("\n")		

	for x in operaciones:
		y = x.split()
		print(y[1],end="")		
		print("",y[2],end="       ")
		
	print("\n")		
	for x in operaciones:
		print(lineas,end="     ")
		
	print("\n")	

	for x in operaciones:
		y = x.split()		
		if respuestas == True:
			resultado = calcular(operaciones)	


def calcular(operaciones):
	resultado = []
	# for x in operaciones:
	if y[1] == "+":
		calculo = int(y[0]) + int(y[2])
			
		print(" ",calculo,end="     ")
	else:
		calculo = int(y[0]) - int(y[2])
		print(" ",calculo,end="     ")
			
print("\n")


arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])

#    32      3801      45      123
# + 698    -    2    + 43    +  49
# -----    ------    ----    -----

# arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)

#   32         1      9999      523
# +  8    - 3801    + 9999    -  49
# ----    ------    ------    -----
#   40     -3800     19998      474



