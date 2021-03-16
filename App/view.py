﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- los n videos con más LIKES para el nombre de una categoría específica")

def printResults(ord_videos,sample):
    size  = lt.size(ord_videos)
    if size > sample:
        print('Los primero ', sample, ' videos ordenados son:')
        i = 0
        while i < sample:
            video = lt.getElement(ord_videos, i)
            print('Titulo: '+ video['title']+' Channel title: '+video['channel_title']+' trending date: '+
             video['trending_date']+ ' Country'+ video['country']+ ' Views: '+ video['views']+' likes: '+
              video['likes']+' dislikes: '+ video['dislikes'])
            i+=1

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = controller.initCatalog()
        print("Cargando información de los archivos ....")
        controller.loadData(catalog)
        print(catalog['category'])

    elif int(inputs[0]) == 2:
        n = input('Cuantos videos desea listar: ')
        category = input('Digite el nombre de la categoria: ')
        videos = controller.getVideosByCategory(catalog,category)
        '''printResults(videos,int(n))'''
        print(videos)


    else:
        sys.exit(0)
sys.exit(0)
