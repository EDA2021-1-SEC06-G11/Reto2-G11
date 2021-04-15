"""
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
import time
import tracemalloc
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.DataStructures import mapentry as mediar
from DISClib.ADT import map as mp
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print('9- Cargar informacion en el catalogo')
    print("1- Encontrar buenos videos por categoría y país")
    print("2- Encontrar video tendencia por país")
    print("3- Encontrar video tendencia por categoría")
    print("4- Buscar los videos con más likes")
    print("0- Salir")

def printResults(ord_videos,sample):
    size  = lt.size(ord_videos)
    lista = []
    if int(size) > int(sample):
        print('Los primero ', sample, ' videos ordenados son:')
        i = 1
        while i <= int(sample):
            video = lt.getElement(ord_videos, i)
            if video['title'] not in lista: 
                print('Titulo: '+ video['title']+' Channel title: '+video['channel_title']+ ' Country'+ video['country']+ ' Views: '+ video['views']+' likes: '+
                video['likes']+' dislikes: '+ video['dislikes'])
                lista.append(video['title'])
            else:
                sample += 1
            i+=1
def printResults1(ord_videos,sample):
    size  = lt.size(ord_videos)
    if size > sample:
        print('Los primero ', sample, ' videos ordenados son:')
        i = 1
        while i < (sample+1):
            video = lt.getElement(ord_videos, i)
            print('Titulo: '+ video['title']+' Channel title: '+video['channel_title']+' trending date: '+
             video['trending_date']+ ' Country'+ video['country']+ ' Views: '+ video['views']+' likes: '+
              video['likes']+' dislikes: '+ video['dislikes'])
            i+=1

def printResults2(video):
    print('El video que tuvo más trending dates fue: ')
    print('Titulo: '+ video[0]['title']+' Channel title: '+ video[0]['channel_title']+' Country: '+video[0]['country']+' Days: '+str(video[1]))

def printResults3(video):
    print('El video que tuvo más trending dates fue: ')
    print('Titulo: '+ video[0]['title']+' Channel Title: '+video[0]['channel_title']+' Category: '+ video[0]['category_id'] + ' Dias: '+ str(video[1]) )

def printResults4(list_sorted,sample):
    size  = lt.size(list_sorted)
    lista = []
    if int(size) > sample:
        print('Los primero ', sample, ' videos ordenados son:')
        i = 1
        while i <= sample:
            video = lt.getElement(list_sorted, i)
            if video['title'] not in lista:
                print('Titulo: '+ video['title']+' Channel title: '+video['channel_title']+' trending date: '+
                video['trending_date']+ ' Publish time'+ video['publish_time']+ ' Views: '+ video['views']+' likes: '+
                video['likes']+' dislikes: '+ video['dislikes'] + 'tags: '+video['tags'] +  'pais: '+video['country'])
                lista.append(video['title'])
            else:
                sample+=1
            i += 1
catalog = None


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 9:
        print("Cargando información de los archivos ....")
        catalog = controller.initCatalog()
        answer = controller.loadData(catalog)
        print("Tiempo [ms]: ", f"{answer[0]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{answer[1]:.3f}")

    elif int(inputs[0]) == 8:
        n = input('Cuantos videos desea listar: ')
        category = input('Digite el nombre de la categoria: ')
        videos = controller.getVideosByCategory(catalog,category)
        printResults(videos,int(n))

    elif int(inputs[0]) == 1:
        n = input('Cuantos videos desea listar: ')
        category = input('Digite el nombre de la categoria: ')
        country = input('Digite el pais que desea listar: ')
        videos = controller.getVideosByCategoryAndCountry(catalog,category,country)
        printResults1(videos[0],int(n))
        print("Tiempo [ms]: ", f"{videos[1][0]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{videos[1][1]:.3f}")
    
    elif int(inputs[0]) == 2:
        country = input('Digite el pais del video que busca: ')
        video = controller.getVideoByTrendingAndCountry(catalog,country)
        printResults2(video[0])
        print("Tiempo [ms]: ", f"{video[1][0]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{video[1][1]:.3f}")

    elif int(inputs[0]) == 3:
        category = input('Digite la categoria del video que busca: ')
        video = controller.getVideoByTrendingAndCategory(catalog,category)
        printResults3(video[0])
        print("Tiempo [ms]: ", f"{video[1][0]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{video[1][1]:.3f}")
    
    elif int(inputs[0]) == 4:
        n = input('Indique numero de videos para listar: ')
        country = input('Indique el pais: ')
        tag = input('Indique el tag: ')
        videos = controller.getVideosByCountryAndTags(catalog,country,tag)
        printResults4(videos[0],int(n))
        print("Tiempo [ms]: ", f"{videos[1][0]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{videos[1][1]:.3f}")
    


    else:
        sys.exit(0)
sys.exit(0)
