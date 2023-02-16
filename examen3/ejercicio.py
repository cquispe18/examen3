#1. Crea un programa en Python que simule una lista de compras. 
# El programa debe permitir al usuario agregar productos al final de la lista,
# eliminar productos del inicio de la lista y mostrar todos los productos en la lista en orden de compra.
def agregar_producto():
    global productos
    nombre = input("ingrese el nombre: ")
    productos.append(nombre)
    print(nombre)
    
    
def eliminar_producto():
    global productos
    productos.remove(productos[0])

    
    
def listar():
    global usuarios
    print( productos)



productos = []
while True:
    print("Lista de compras")
    print("[1]..agregar producto..")
    print("[2]..eliminar producto..")
    print("[3]..listar productos..")
    print("[4]..salir..")
    
    opcion = int(input("\nSeleccione una opcion: "))
    
    if opcion ==1:
        agregar_producto()
    elif opcion == 2:
        eliminar_producto()
    elif opcion == 3:
        listar()
    elif opcion == 4:
        break