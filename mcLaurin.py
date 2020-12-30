import numpy as np
import math 
import sympy as sy
from sympy.interactive import printing
printing.init_printing(use_latex=True)
import matplotlib.pyplot as plt
from fractions import Fraction
import pandas as pd
import brain

class McTaylor:
    
    def __init__(self, fun):

        fun = brain.ecuacion2(fun)

        
        self.f = fun
        
    def calculate(self):
        
        global x, fx, n, x0
        x, fx, n, x0 = sy.symbols('x fx n x0') 
        #sym = "x, fx, n, x0 = sy.symbols('x fx n x0')"
        #self.f = ( sy.log(x) )
        
        ldict = {}
        sToCode  = "f = myExp "
        sToCode = sToCode.replace("myExp", self.f)
        exec(sToCode, globals(), ldict)
        f = ldict['f']
        
        
        xi = 0 
        itr = 7
        res = 0
        listx = np.array([])
        
        res =  (f.subs(x, xi )).evalf() 
        datos = []
        datos.append([f ,'->',res])
        
        
        
        for xp in range(1, itr + 1):
            f = sy.diff(f)
            f = f.doit()
            res =  (f.subs(x, xi )).evalf() 
            datos.append([f,'->',res])
        
            listx = np.append(listx, res)
        
        func =  ( (fx / sy.factorial(n) ) * (x - x0)**2 )
        
        xxx = []
        
        for xp in range( len(listx) ):
          xxx.append(  sy.Rational(float(listx[xp]), math.factorial(xp + 1)) * (x - xi)**(xp + 1) )
        filas = []
        for i in range(1,len(datos)+1):
          filas.append(i)
        
        resultadosFinales = pd.DataFrame(datos,filas,['Derivada',' ','Sustituyendo'])
        
        
        # print(resultadosFinales)
        # display(xxx)
        # print(xxx)
        
        return resultadosFinales, xxx

#obj = McTaylor('log(x)')
obj = McTaylor('e**(5*x)')
r1, r2 = obj.calculate()
print(r1)
print(r2)
