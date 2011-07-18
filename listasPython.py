#!/usr/bin/python
# Ejemplo ciudades
ciudades = ["Mexico", "Madrid", "Manzanillo", "Mazatlan", "Buenos Aires", "Mazatlan", "Bogota", "Santiago"];
# Imprime lista ciudades 
print ciudades;
# imprime ciudades 
print ciudades[0];
print ciudades[4];
print ciudades[2];

# Cantidad de ciudades en la lista
print "Cantidad de entradas en lista ciudades: ";
print len(ciudades);

# Recorrer la lista con for
for x in ciudades:
	print x;

# Funcion range
numeros = range(10);
for i in numeros:
	print i;

numeracion = range(5, 100, 5);
print numeracion;

# Ejemplos for - if 
edades = range(1,99);
tuEdad = int(raw_input("Tu edad por favor: "));

for k in edades:
	if tuEdad <= 18:
		print "Eres menor de edad";
		break;
	else:
		print "Ya eres mayor de edad";
		break;

tuCiudad = raw_input("Tu ciudad: ");
for c in ciudades:
	if c == tuCiudad:
		print c;
		break;
	else:
		print "Ciudad no registrada";
		break;
while tuEdad < 18:
	tuEdad = int(raw_input("Tu edad es menor... intenta de nuevo: "));
	if tuEdad > 17:
		print "Eres mayor de edad";
		break;
	else:
		print "eres menor";

