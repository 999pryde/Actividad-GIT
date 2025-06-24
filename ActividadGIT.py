import os

os.system("cls")



nombre = ""

listaNombre = [] 



while True:



  while True:

    print ("1.- Agregar alumnos")

    print ("2.- Mostrar todos los alumnos")

    print ("3.- Eliminar alumno")

    print ("4.- Salir")



    try:

      opcion = int(input("\nIngrese su eleccion (1/2/3/4): "))

      if (1 <= opcion and opcion <=4):

        break

      else:

        print("Por favor seleccione las opciones mostradas (1/2/3/4).")

    except ValueError:

      print("ERROR. Ingrese un dato valido de numero entero (1/2/3/4).")

  

  if opcion == 1:

    while True:

      nombre = input("\nIngrese su nombre: ")

      if (nombre.isalpha()):

        print("Su nombre se ingreso correctamente.")

        listaNombre.append(nombre)

        break

      else:

        print("\nIngrese su nombre correctamente: ") 



  if opcion == 2:

    print (listaNombre)



  if opcion == 3:

    

    while True:

      try:

        nombreEliminar = input("\nIngrese el nombre del alumno que desea eliminar: ")

        if listaNombre == nombreEliminar:

          listaNombre.remove(listaNombre)

          print("Alumno eliminado con exito!.")

          break

        else:

          print("Ingrese el Nombre correctamente.")

      except ValueError:

          print("ERROR.Ingrese el Nombre correctamente.")    



  if opcion == 4:

    break

