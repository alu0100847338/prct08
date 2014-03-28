#!/usr/bin/python
import sys
import modulo

argumentos = sys.argv[1:]
if (len(argumentos) == 8):
  n = int (argumentos[0])
  aproximaciones = int (argumentos[1])
  umbral = []
  for i in range (2,7):
    umbral.append(float (argumentos[i]))
  nombre_fichero = argumentos[7]
else:
  print "Introduzca el numero de intervalos (n > 0):"
  n = int (raw_input ());
  print "Introduzca el numero de aproximaciones:"
  aproximaciones = int (raw_input ());
  print "Introduzca 5 umbrales de error:"
  umbral = []
  for i in range (5):
    print "Introduzca el umbral", i, ":"
    umbral.append(float (raw_input ()));
  print "Introduzca el nombre del fichero para almacenar los resultados:"
  nombre_fichero = raw_input ();
