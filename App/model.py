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
def newCatalog(mptype,ldfactor):
    catalog = {
        'videos': None,
        'country': None,
        'category': None,
        'categories': None}

    catalog['videos'] = lt.newList('ARRAY_LIST')

    catalog['category'] = mp.newMap(50,
                                    maptype=mptype
                                    ,loadfactor=ldfactor,
                                    comparefunction=cmpCategoryNames)
    catalog['country'] = mp.newMap(10,
                                    maptype='PROBING',
                                    loadfactor=0.5,
                                    comparefunction= cmpVideosCountry)
    
    catalog['categories'] = lt.newList('ARRAY_LIST')
    
    return catalog

# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):
    lt.addLast(catalog['videos'], video)
    entry = mp.get(catalog['category'],video['category_id'])
    if entry:
        lt.addLast(entry['value']['videos'], video)
   

def addCountry(catalog,country, video):
   
    countries = catalog['country']
    existcountry = mp.contains(countries, country)
    if existcountry:
        entry = mp.get(countries, country)
        country1 = me.getValue(entry)
    else:
        country1 = newVideoCountry(country)
        mp.put(countries, country, country1)
    lt.addLast(country1['videos'],video)
    

def addCategories(catalog,category):
    t = newCategoryID(category['name'], category['id'])
    lt.addLast(catalog['categories'],t)

def addCategory(catalog, category):
    newCategory = newVideoCategory(category['id'],category['name'])
    mp.put(catalog['category'],category['id'],newCategory)

# Funciones para creacion de datos
def newCategoryID(name,id):
    category = {'name':'','id':''}
    category['name'] = name
    category['id'] = id
    return category

def newVideoCountry(pais):
    country = {'videos': None}
    country['country'] = pais
    country['videos'] = lt.newList('ARRAY_LIST')
    return country

def newVideoCategory(id,name):
    category = {'name': '',
                'category_id': '',
                'videos': None,
                }
    category['name'] = name
    category['category_id'] = id
    category['videos'] = lt.newList('ARRAY_LIST')
    return category
# Funciones de consulta

def getVideosByCategory(catalog, category):

    video = mp.get(catalog['category'],category)
    if video:
        return me.getValue(video)['videos']
    return None

def getVideosByCountry(catalog, country):
    video = mp.get(catalog['country'],country)
    if video:
        return me.getValue(video)['videos']
    return None

def getVideosByCategoryR1(videos,size, category_id):
    BestVideos = newCatalog()
    for pos in range(0, int(lt.size(videos))):
        element = lt.getElement(videos,pos)
        if element['category_id'] == category_id:
            lt.addLast(BestVideos['videos'],element)
    return BestVideos['videos']

def getNumByID(catalog):
    bestvideo = None
    bestreps = 0
    cmpvideo = None
    cmpreps = 0
    pos = 1
    while pos <= lt.size(catalog):
        cmpvideo = lt.getElement(catalog, pos)
        cmpreps = repForID(catalog, cmpvideo['video_id'], pos)
        if cmpreps > bestreps:
            bestvideo = lt.getElement(catalog, pos)
            bestreps = cmpreps
        pos += cmpreps
    return (bestvideo,bestreps)

def repForID(catalog, video, firstpos):
    reps = 0
    pos = firstpos
    while pos <= lt.size(catalog):
        cmpvideo = lt.getElement(catalog, pos)
        if cmpvideo['video_id'] == video:
            reps += 1
        else:
            break
        pos += 1
    return reps

def getVideosByTags(catalog,tag,size):
    BestVideos = newCatalog()
    for pos in range(0, int(lt.size(catalog))):
        element = lt.getElement(catalog, pos)
        if cmpVideosTags(catalog,element,tag) == True:
            lt.addLast(BestVideos['videos'],element)
    return BestVideos['videos']

# Funciones utilizadas para comparar elementos dentro de una lista
def cmpVideosTags(catalog,element, tag):
    respuesta = False
    taglist = element['tags'].split('|')
    i = 0
    while i < len(taglist) and respuesta == False:
        t = taglist[i].find(tag)
        if t != (-1):
            respuesta = True
        i += 1
    return respuesta

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

def cmpVideosCountry(name, country):
    countryEntry = me.getKey(country)
    if name == countryEntry:
        return 0
    elif name > countryEntry:
        return 1
    else:
        return -1

def cmpVideosByLikes(video1,video2):
    if float(video1['likes']) > float(video2['likes']):
        return True
    else:
        return False

def cmpVideosByViews(video1,video2):
    if float(video1['views']) > float(video2['views']):
        return True
    else:
        return False

def cmpVideosByID(video1,video2):
    if (video1['video_id']) < (video2['video_id']):
        return True
    else:
        return False


# Funciones de ordenamiento

def sortVideos(catalog,size):
    sub_list = lt.subList(catalog, 0, size)
    sub_list = sub_list.copy()
    sorted_list = mer.sort(sub_list, cmpVideosByLikes)
    return sorted_list

def sortVideosByViews(catalog,size):
    sub_list = lt.subList(catalog, 0, size)
    sub_list = sub_list.copy()
    sorted_list = mer.sort(sub_list, cmpVideosByViews)
    return sorted_list

def sortVideosByID(catalog,size):
    sub_list = lt.subList(catalog, 0, size)
    sub_list = sub_list.copy()
    sorted_list = mer.sort(sub_list, cmpVideosByID)
    return sorted_list