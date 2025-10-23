import random
numero_secreto = random.randint(1,50)

acumulador = 0

for i in range (5):
 
 numero_ingresado = int(input ( "ingrese numero del 1 al 50: "))
 
 acumulador+= numero_ingresado 
 
 if numero_secreto == numero_ingresado:
  
  print ("Acerto el numero, fin del juego")
  break

 elif numero_secreto > numero_ingresado:
  print ( "El numero es mayor")

 elif numero_secreto < numero_ingresado:
  print ( "El numero es menor")

else:
 print (f"Se terminaron los intentos, perdiste. El numero era {numero_secreto}")