# PyPlus-Diego-Borlandi
Juegos.py modificado: usando PySimpleGui y archivos.
En el uso de estructura, elegí un diccionario, unicamente xq es muy de fácil acceso y adición de datos, 
para cada nombre de jugador, tengo asociado un string que representa uno de los tres juegos.


Justificando el porqué usé formato JSON, voy a tratar de explicarme lo mejor posible.

Elegí JSON ya que me brinda facilidades y es un formato universal,
hace que no dependa de python y su manejo está orientado a los archivos de texto.
Aparte, yo elegí guardar un diccionario en mi archivo, puedo tranquilamente tomar TODO el diccionario con otro programa,
es un acceso fácil e instantaneo.

Contra pickle, lo veo en ventaja, pickle maneja archivos binarios y estos deben ser decodificados para tomar sus datos,
sumado a que sólo es un formato utilizado en Python.

Pude haber utilizado CSV? yo creo que sí, pero JSON me costa 1 sola linea de codigo para almacenarle datos.
