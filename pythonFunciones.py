#!/usr/bin/python
from string import maketrans
import re

def hola(nombre):
	print "Hola " + nombre;

def numera(inicial,final,paso):
	numeracion = range(inicial, final, paso);
	print numeracion;



nombre = raw_input("escribe tu nombre: ");

hola(nombre);

inicial = int(raw_input("Indica numero inicial: "));
final = int(raw_input("indica numero final: "));
paso = int(raw_input("indica paso: "));

numera(inicial,final,paso);



lista='Coacalco','Coatlicue','Coahoulia','Acoxpa', 'Coapa', 'Oaxaca', 'Acolman', 'Acapulco'


def buscando():
        print 'Buscando en la lista.'
        criterio=raw_input('indica el lugar: ')
        print 'Palabra clave: ' + criterio
        for locacion in lista:
                if re.search(criterio , locacion):
                        print '---------------'
                        print locacion
                        print '---------------'


print lista;

buscando();
