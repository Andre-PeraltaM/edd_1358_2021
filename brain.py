import math
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl

''' El cerebro de toda la libreria'''
def prueba(x):
	x = str(x)
	apertura = ['(','[','{']
	cierre = [')',']','}']

	lista ={')':'(',']':'[','}':'{'}

	orden = []

	for i in x:
		if i in apertura:
			orden.append(i)
			print('s')
		elif i in cierre:
			print('a')
			if orden[-1] == lista[i]:
				orden.pop()
			else:
				return False
	if len(orden) == 0:

		return True
	else:

		return False

def comprobar(funcion):

	x = prueba(funcion)

	if x == False:
		return False
	else:
		return True





def sic(x):
	return 1/math.cos(x)

def csc(x):
	return 1/math.sin(x)

def cot(x):
	return 1/math.tan(x)



def grafica(function):
	'''
	Tabula y grafica una función  
	'''
	
	x = np.linspace(-10,3,100)

	x_str = list(map(str,np.linspace(-10,3,100)))
	y = []
	for i in x_str:
		y.append(sustitucion(function,i))

	figura = plt.figure(figsize=(7,7),edgecolor = 'black') 
	grafico = figura.add_axes([0.1,0.1,0.9,0.9])
	grafico.plot(x,y ,'red',label = f"f(x)={function}")
	grafico.legend(loc = 0)

	plt.title(f" f(x) = :  {function} ") 
	ax = pl.gca()  # gca stands for 'get current axis'
	ax.spines['right'].set_color('none')
	ax.spines['top'].set_color('none')
	ax.xaxis.set_ticks_position('bottom')
	ax.spines['bottom'].set_position(('data',0))
	ax.yaxis.set_ticks_position('left')
	ax.spines['left'].set_position(('data',0))

	plt.xlabel("Eje X")

	plt.ylabel("Eje Y")
	plt.show()
	

def __parentesis(function,caracter = None):
	#ESTE METODO DEBE SER PRIVADO
	ecu = function
	objeto = DoubleLinkedList()
	objeto.introduce_funcion(ecu)

	tamaño = objeto.get_size()
	for i in range(tamaño):
		if objeto.pop(i) == '(':
			try:

				if (objeto.pop(i-1).isdecimal() or objeto.pop(i-1) == ')') and i-1 != -1 :
					objeto.insert('*(',i)
					objeto.delete(i+1)

				
			except Exception as e:
				pass
		if objeto.pop(i) == ')':
			try:
				if objeto.pop(i+1).isdecimal() or objeto.pop(i+1) == '(':
					objeto.insert(')*',i)
					objeto.delete(i+1)
			except Exception as e:
				pass

	return objeto.transversal()


def ecuacion(function):
	'''
	Sustituye los valores de una ecuacion en su forma str para hacerla valida por el metodo eval()
	Resive un valor Str y devuelve un valor str equivalente que puede ser introducido en eval()
	Si la función está mal entonces se devuelve 'error'
	'''
	

	tabla_de_valores = { 88: '(x)', 120: '(x)', 94: '**'}
	function = function.translate(tabla_de_valores)
	#Las anteriores 3 lineas son para sustituir X, x y ^
	diccionario_otras_variables = {'sec':'(sic','csc':'(csc','cot':'(cot','sen':'(math.sin','cos':'(math.cos','tan':'(math.tan','senh':'(math.sinh','cosh':'(math.cosh','tanh':'(math.tanh','sin^-1': '(math.asin', 'cos^-1' : '(math.acos' , 'tan^-1' : '(math.atan','π':'(math.pi)','sqrt':'(math.sqrt','√':'(math.sqrt','Ln':'PROCESO','PROCESO':'(math.log10','PROCESO':'(math.log','PROCESO':'(math.acos','PROCESO':'(math.asin','PROCESO':'(math.atan','e':'(math.e)'}

	#math.log(x, base)
	for i in diccionario_otras_variables:
		if i in function:
			for j in range(function.count(i)):
				z = function[function.find(i)+len(i)+1:]
				function = function[:function.find(i)+len(i)+1+z.find(')')] + ')' + function [function.find(i)+len(i)+1+z.find(')')+1:] 
				function = function.replace(i,diccionario_otras_variables[i],1)


	function = __parentesis(function,'(')#Hace que los parentesis multipliquen
	function = __parentesis(function,')')
	
	#Valor absoluto
	return function
def sustitucion(function, value = '1'):
	'''
	Sustituye los valores de X en una ecuación por el valor dado
	Si no se da un valor se evalua en 1 
	'''
	function = function.replace('x',value)
	try:
		return eval(function)
	except ZeroDivisionError:
		return None
	except ValueError:
		return None


def tabulacion(function,value1 = -3,value2 = 3):
	'''
	Tabula una función tipo eval() en un rango de valores.
	Recibe una función str y dos valores que son los limites, para devolver una lista con los resultados
	'''
	valuesX = list(map(str,range(value1,value2+1)))

	rango_valoresY = []

	for i in valuesX:
		rango_valoresY.append(sustitucion(function,i)) 

	return rango_valoresY

def hay(un_objeto , en_este_argumento , y_este_aparece_solo = 1):
	'''
	Usando un if se lee de la siguiente manera:

	Si hay un objeto (x) en un argumento (y) , devuelve true si este elemento está presente éste numero de veces (z)

	Funcion que retorna True si un objeto está presente en un argumento (listas,tuplas,str etc.)
	Si le aplica el tercer argumento entonces se le puede pedir que nos diga si está presente el número de veces que queremos
	Si como tercer argumento se le pone un 0 entonces estamos diciendo que nos diga si no está


	'''
	cont = 0
	for i in en_este_argumento:
		if un_objeto == i:
			cont += 1

	if y_este_aparece_solo == cont:
		return True
	else:
		return False


#AQUI EMPEZAMOS CON LA CALCULADORA




def ecuacion2(function):
	'''
	Para cuando el programa use sympy
	'''
	tabla_de_valores = { 88: '(x)', 120: '(x)', 94: '**'}
	function = function.translate(tabla_de_valores)
	diccionario_otras_variables = {"ln":"sy.ln","log":"sy.log","cos":"sy.cos","sin":"sy.sin","tan":"sy.tan","cot":"sy.cot","sec":"sy.sec","csc":"sy.csc","sinc":"sy.sinc","acos":"sy.acos","asin":"sy.asin","atan":"sy.atan","acot":"sy.acot","asec":"sy.asec","acsc":"sy.acsc","acsc":"sy.acsc","π":"math.pi","e":"math.e"}
	#math.log(x, base)
	for i in diccionario_otras_variables:
		if i in function:
			for j in range(function.count(i)):
				z = function[function.find(i)+len(i)+1:]
				function = function[:function.find(i)+len(i)+1+z.find(')')] + ')' + function [function.find(i)+len(i)+1+z.find(')')+1:] 
				function = function.replace(i,diccionario_otras_variables[i],1)
	function = __parentesis(function,'(')#Hace que los parentesis multipliquen
	function = __parentesis(function,')')
	return function
class NodoDoble:
    def __init__( self , dato, anterior = None, siguiente = None):
        self.dato = dato
        self.siguiente = siguiente
        self.anterior = anterior

class DoubleLinkedList:
	def __init__(self):
		self.__head = None
		self.__tail = None
		self.__size = 0

	def get_size(self):
		return self.__size

	def is_empty(self):
		return self.__size == 0

	def append(self,value):
		if self.is_empty():
			nuevo = NodoDoble(value)
			self.__head = nuevo
			self.__tail = nuevo
		else:
			nuevo = NodoDoble(value,self.__tail,None)
			self.__tail.siguiente = nuevo #tail.next = nuevo
			self.__tail = nuevo
		self.__size += 1

	def transversal(self): 
		'''recorrido desde head'''
		resultado = ''
		curr_node = self.__head
		if curr_node != None:
			while curr_node != None :
				resultado = resultado + curr_node.dato
				curr_node = curr_node.siguiente
		else:
			print('Lista vacia')
		return resultado

	def pop(self,pos=-1):
		'''obtener el valor en la posición específica'''
		if self.__head != None:#Por si la lista está vacía
			if 0 == pos:#Esto es por si el elemento es head
				return self.__head.dato

			cont = 0
			curr_node = self.__head
			while( curr_node.siguiente != None ):
				if cont+1 == pos:
					return curr_node.siguiente.dato

				elif pos == -1 and curr_node.siguiente.siguiente == None:#En caso de que no ponga una posición se elimina el último valor
					return curr_node.siguiente.dato
				cont +=1
				curr_node = curr_node.siguiente
			return False
		else:
			print('Lista vacía')
	def insert(self,value,pos=-1):
		'''Introduce el valor en la posición específica'''
		if self.__head != None:#Por si la lista está vacía
			if 0 == pos:#Esto es por si el elemento es head
				x = self.__head
				self.__head = NodoDoble(value,None,x)
				return None

			cont = 0
			curr_node = self.__head
			while( curr_node.siguiente != None ):
				if cont+1 == pos:
					x = curr_node.siguiente
					curr_node.siguiente = NodoDoble(value,curr_node,x)
					return None

				elif (pos == -1 or pos == self.__size) and curr_node.siguiente.siguiente == None:#En caso de que no ponga una posición se elimina el último valor
					curr_node.siguiente.siguiente = NodoDoble(value,curr_node,None)
					return None
				cont +=1
				curr_node = curr_node.siguiente
			return False #Retorna False en caso de que esté fuera de rango
		else:
			print('Lista vacía')
	def introduce_funcion(self,funcion):
		for i in funcion:
			self.append(i)
	def delete(self,pos=-1):
		'''obtener el valor en la posición específica'''
		if self.__head != None:#Por si la lista está vacía
			if 0 == pos:#Esto es por si el elemento es head
				x = self.__head.dato
				self.__head = self.__head.siguiente
				return x

			cont = 0
			curr_node = self.__head
			while( curr_node.siguiente != None ):
				if cont+1 == pos:
					x = curr_node.siguiente.dato
					curr_node.siguiente = curr_node.siguiente.siguiente
					return x

				elif pos == -1 and curr_node.siguiente.siguiente == None:#En caso de que no ponga una posición se elimina el último valor
					x = curr_node.siguiente.dato
					curr_node.siguiente = curr_node.siguiente.siguiente
					return x
				cont +=1
				curr_node = curr_node.siguiente
			return False
		else:
			print('Lista vacía')

print(ecuacion('e**(5x)'))
