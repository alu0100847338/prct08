#!/src/bin/python
PI = 3.14155926535897931159979634685441852
import sys
def aproximacion(n_intervalos):
  n = int (n_intervalos)
  if (n!=0):
    suma = 0
    for i in range(1,n+1):
      xi = (i - (1/2)) / float(n_intervalos)
      f_xi = 4 / (1 + xi**2)
      b = i / float(n)
      a = b - (1 / float(n_intervalos))
      suma = suma + f_xi
    pi = suma/n
    return pi
    
def error(n_intervalos, n_test, umbral):
   incorrectos=0
   for i in range(n_test):
     valor_pi=aproximacion(n_intervalos)
     valor=valor_pi-PI
     if(abs(valor)>umbral):
       incorrectos=incorrectos+1
   porcentaje=(incorrectos/float(n_test))*100
   return porcentaje
    
if __name__ == "__main__":
  
 if(len(sys.argv)==4):
   n_intervalos = int(sys.argv[1])
   n_test = int(sys.argv[2])
   umbral=float(sys.argv[3])
   
   
 else:
   print'La forma de uso es: "modulo.py, n, m", por lo que se utilizaran los valores por defecto'
   n_intervalos = 10
   n_test= 10
   umbral=0.00001
   
 porcentaje=error(n_intervalos,n_test,umbral)
 print 'El numero de porcentaje es del ', porcentaje
 

