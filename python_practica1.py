import random
numero_secreto = random.randint(1,50)

def numero_valido():
 while True:
  try:
   numero_solicitado = input ("ingrese numero del 1 al 50: ")
   numero_correcto = int(numero_solicitado)

   if (numero_correcto >= 1) and (numero_correcto <= 50):
    return numero_correcto
   else:
    print ("Debe ingresar un numero entre 1 y 50. Intente nuevamente")

  except ValueError:
   print ("Error. Debe ingresar un numero entero.")

for i in range (5):
 
  numero_ingresado = numero_valido()
 
  if numero_secreto == numero_ingresado:
   print ("Acerto el numero, fin del juego")
   break

  elif numero_secreto > numero_ingresado:
    print ( "El numero es mayor")

  elif numero_secreto < numero_ingresado:
    print ( "El numero es menor")

else:
 print (f"Se terminaron los intentos, perdiste. El numero era {numero_secreto}")