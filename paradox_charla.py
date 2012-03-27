#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The Python Paradox
==================
**Lima - 2012**

    :por: Ider Delzo [*]_ <soloidx@gmail.com>
    :licencia: CC-by-nc 3.0

    Controles::

        >>> d()     #para avanzar un bloque/slide
        >>> d(i)     #para ir al ``i``ésimo bloque
        >>> d.again() #para repetir la última
        >>> d.jump(n) #para saltar n bloques (Ej: d.jump(-1) para volver al último bloque mostrado)
        >>> d.reset() #para iniciar de nuevo
"""
# <demo> --- stop ---

# introduccion básica al código:

print 'hola mundo'

for i in range(10):
    if i % 2 == 0:
        print 'el numero %i es par' % i

print 'ciclo terminado \\0/'


# <demo> --- stop ---

# funciones basicas:

def funcion(parametro):
    """
    do something
    """
    print "He aqui mi parametro \n%s" % parametro
    print "Fin"

# <demo> --- stop ---

# 2da demo

# <demo> --- stop ---

# 2da demo
# Modulos

import urllib

def descargar_imagen(direccion):
    """
    download a image from <<direccion>> and save it
    """
    #i guess the name based a split
    nombre = direccion.split('/')[-1]
    #and i save it in the script path
    urllib.urlretrieve(direccion, nombre)


# <demo> --- stop ---

# 3ra demo

# <demo> --- stop ---

# 3ra demo

"""
    Herramientas:

    Interpretes
    - IPython

    Entornos aislados:
    - Virtualenv

    Paquetes:
    - pip

    Deployment:
    - Fabric
"""

# <demo> --- stop ---

# 3ra demo ejemplo

from pyquery import PyQuery as pq

enlace = 'http://elcomercio.pe/'

pagina_procesada = pq(enlace)

lista_noticias = pagina_procesada('#show_news div h2 a')

# <demo> --- stop ---

# demo final

# ahora si

import urllib
from pyquery import PyQuery as pq


def descargar_imagen(direccion):
    """
    download a image from <<direccion>> and save it
    """
    print u'descargando %s' % direccion
    #i guess the name based a split
    nombre = direccion.split('/')[-1]
    #and i save it in the script path
    urllib.urlretrieve(direccion, nombre)


tag_magico = '.gallery-item a'

#obtengo una direccion desde un archivo

archivo = file('galerias.txt')
url = archivo.readlines()[0]

#se crea un objeto de pyquery

procesador_pyquery = pq(url)

#se obtiene los datos necesarios

lista_enlaces = procesador_pyquery(tag_magico)

#se descargan esos datos

for enlace in lista_enlaces:
    descargar_imagen(enlace)
