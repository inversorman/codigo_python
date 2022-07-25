datos_personales={
 
}
datos_laborales={
  '001':['',160,'','','','']
}
salir=0
while salir==0:
  print('Ingrese la opcion que desea:')
  opcion=int(input("1)Ingrese un trabajador\n2)Modificar datos\n3)Ingrese datos laborales\n4)Editar datos\n5)Salir\nElija una opcion:"))

  if opcion == 1:
    DNI=input('ingrese su DNI:')
    nombre=input('ingrese su nombre:')
    apellido=input('ingrese su apellido:')
    cargo=input('ingrese su cargo:')
    hijos=input('ingrese el numero de hijos que tiene')
    estado=input('ingrese su estado laboral')
    lista=[nombre,apellido,cargo,hijos,estado]
    datos_personales[DNI]=lista
    print(datos_personales)
    print('Verifique sus datos:',datos_personales,'\nes correcto?')
  if opcion == 2:
