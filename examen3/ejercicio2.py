#2.Crea un programa en Python que mantenga un historial de tareas pendientes. 
# El programa debe permitir al usuario agregar una tarea al inicio de la lista,
#  eliminar una tarea del final de la lista y mostrar todas las tareas en la lista en orden inverso al que se agregaron.
#  Además, el programa debe contar la cantidad total de tareas en la lista y mostrar ese número al usuario.
class Nodo:
  def _init_ (self, datoInicial):
   self.dato = datoInicial
   self.siguiente = None

  #Getters
  def get_dato (self):
    return self.dato
  
  def get_siguiente (self):
    return self.siguiente
  
  #Setters
  def set_dato (self,nuevoDato):
    self.dato = nuevoDato

  def set_siguiente (self, nuevoSiguiente):
    self.siguiente = nuevoSiguiente

class ListaSimple:
  def _init_ (self):
    self.primero = None

  #MÉTODO: Verificar si está vacía.
  def estaVacia(self):
    return self.primero == None

  #MÉTODO: Agregar elemento al primero de la lista.
  def agregar(self,dato):
    nuevoNodo = Nodo(dato)
    nuevoNodo.set_siguiente(self.primero)
    self.primero = nuevoNodo
  
  #MÉTODO: Hallar el tamaño de la lista.
  def tamaño(self):
    actual = self.primero
    contador = 0
    while actual != None:
      contador = contador + 1
      actual = actual.get_siguiente()
    return contador

  #MÉTODO: Buscar un elemento específico.
  def buscar(self, dato):
    actual = self.primero
    encontrado = False
    while actual != None and not encontrado:
      if actual.get_dato() == dato:
        encontrado = True
      else:
        actual = actual.get_siguiente()
    
    return encontrado

  #MÉTODO: Eliminar un elemento.
  def remover_elemento (self, dato):
    aux = self.primero
    aux1 = None
    encontrado = False
    while not encontrado:
      if aux.get_dato() == dato:
        encontrado = True
      else:
        aux1 = aux
        aux = aux.siguiente
    if aux1 == None:
      self.primero = aux.siguiente
    else:
      aux1.set_siguiente(aux.siguiente)

  #MÉTODO: iterar.
  def iterar(self):
    actual=self.primero
    while actual:
      dato=actual.dato
      actual=actual.siguiente
      yield dato

####################################

  #MÉTODO: Agregar elemento al final de la lista.
  def agregar_final(self,dato):
    nuevoNodo = Nodo(dato)
    aux = self.primero
    while aux.siguiente:
      aux = aux.siguiente
    aux.siguiente = nuevoNodo

  #Insertar antes de un elemento buscado
  def agregar_antes_de_elemeno_buscado(self,dato,datoBuscado):
    nuevoNodo = Nodo(dato)
    aux = self.primero
    aux1 = None
    encontrado = False
    while aux != None and not encontrado:
      if aux.get_dato() == datoBuscado:
        aux1.siguiente = nuevoNodo
        nuevoNodo.siguiente = aux
        encontrado = True

      else:
        aux1 = aux
        aux = aux.siguiente
  #Insertar despues de un elemento buscado
  def agregar_despues_de_elemeno_buscado(self,dato,datoBuscado):
    nuevoNodo = Nodo(dato)
    aux = self.primero
    aux1 = aux
    encontrado = False
    while aux != None and not encontrado:
      if aux.get_dato() == datoBuscado:
        aux.siguiente = nuevoNodo
        nuevoNodo.siguiente = aux1
        encontrado = True

      else:
        
        aux = aux.siguiente
        aux1 = aux.siguiente

  #Remover primero      
  def remover_primero (self):
    aux = self.primero
    self.primero = aux.siguiente
    aux.siguiente = None
  
  #Remover ultimo
  def remover_ultimo (self):
    aux = self.primero
    aux1 = None
    while aux.siguiente != None:
      aux1 = aux
      aux = aux.siguiente
    aux1.siguiente = None
      


    
LS = ListaSimple()


#Insertar al inicio
LS.agregar("barrer")
LS.agregar("limpiar")
LS.agregar("cocinar")
LS.agregar("lavar")


#MÉTODO: Agregar elemento al final de la lista.
LS.agregar_final("planchar")

#remover nodo buscado
LS.remover_elemento("cocinar")

print(LS.estaVacia())

for d in LS.iterar():
    print(d)