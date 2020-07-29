print("*"*20)
print("Bienvenido, ¿deseas calcular tu peso en Marte?")
print("*"*20)
respuesta = input("(1)Si / (2)No \n")
if respuesta == "1":
  print("¿En que planeta desea estar?")
  print("a. Marte")
  print("b. Luna de la Tierra")
  planeta = input("cual escoge: ")

  def calcular_peso(gravedad_planeta):
    peso_user = int(input("Ingrese el peso en kilogramos: "))
    gravedad_tierra = 9.85
    peso_final = int((peso_user*gravedad_marte)/gravedad_tierra)
    print("Su peso es: ",peso_final," kg")

  if (planeta == "a"):
    
    gravedad_marte = 3.71
    calcular_peso(gravedad_marte)

  if (planeta == "b"):
    peso_user = int(input("Ingrese el peso en kilogramos: "))
    gravedad_tierra = 9.85
    gravedad_luna = 1.62
    peso_final = int((peso_user*gravedad_luna)/gravedad_tierra)
    print("Su peso es: ",peso_final," kg")

else:
  print("¿Entonces para que me usas ?")