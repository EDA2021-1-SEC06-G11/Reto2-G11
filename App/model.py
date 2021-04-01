"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.Algorithms.Sorting import mergesort as mer
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    catalog = {
        'videos': None,
        'category': None,
        'categories': None}

    catalog['videos'] = lt.newList('ARRAY_LIST')

    catalog['category'] = mp.newMap(50,
                                    maptype='CHAINING'
                                    ,loadfactor=6.0,
                                    comparefunction=cmpCategoryNames)
    
    catalog['categories'] = lt.newList('ARRAY_LIST')
    
    return catalog

# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):
    lt.addLast(catalog['videos'], video)
    entry = mp.get(catalog['category'],video['category_id'])
    if entry:
        lt.addLast(entry['value']['videos'], video)

def addCategories(catalog,category):
    t = newCategoryID(category['name'], category['id'])
    lt.addLast(catalog['categories'],t)

def newCategoryID(name,id):
    category = {'name':'','id':''}
    category['name'] = name
    category['id'] = id
    return category

def addCategory(catalog, category):
    newCategory = newVideoCategory(category['id'],category['name'])
    mp.put(catalog['category'],category['id'],newCategory)
    
def newVideoCategory(id,name):
    category = {'name': '',
                'category_id': '',
                'videos': None,
                }
    category['name'] = name
    category['category_id'] = id
    category['videos'] = lt.newList('ARRAY_LIST')
    return category


# Funciones para creacion de datos

# Funciones de consulta

def getVideosByCategory(catalog, category):

    video = mp.get(catalog['category'],category)
    if video:
        return me.getValue(video)['videos']
    return None



# Funciones utilizadas para comparar elementos dentro de una lista

def cmpVideosCategoryID(catalog, category):
    size = lt.size(catalog['categories'])
    i = 0 
    centinela = False
    while i <= size and centinela == False:
        cat = lt.getElement(catalog['categories'],i)
        if cat['name'].lower() == (' '+category):
            respuesta = cat['id']
            centinela = True
        i += 1
    return respuesta

def cmpCategoryNames(name, category):
    categoryEntry = me.getKey(category)
    if (name == categoryEntry):
        return 0
    elif (name > categoryEntry):
        return 1
    else:
        return -1

def cmpVideosByLikes(video1,video2):
    if float(video1['likes']) > float(video2['likes']):
        return True
    else:
        return False
# Funciones de ordenamiento

def sortVideos(catalog,size):
    sub_list = lt.subList(catalog, 0, size)
    sub_list = sub_list.copy()
    sorted_list = mer.sort(sub_list, cmpVideosByLikes)
    return sorted_list