﻿"""
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
 """

import config as cf
import model
import time
import tracemalloc
import csv
from DISClib.ADT import list as lt


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def initCatalog():
    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos
def loadData(catalog):
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    loadCategories(catalog)
    loadVideos(catalog)

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)

    return delta_time, delta_memory


def loadVideos(catalog):
    videosfile = cf.data_dir + 'Videos/videos-large.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        model.addCountry(catalog,video['country'],video)
        model.addVideo(catalog, video)


def loadCategories(catalog):
    categoryfile = cf.data_dir + 'Videos/category-id.csv'
    input_file = csv.DictReader(open(categoryfile, encoding='utf-8'),delimiter= '\t')
    for category in input_file:
        model.addCategories(catalog,category)
        model.addCategory(catalog,category)

# Funciones de ordenamiento

#Funciones para medir tiempo y memoria
def getTime():
    return float(time.perf_counter()*1000)

def getMemory():
    return tracemalloc.take_snapshot()

def deltaMemory(start_memory, stop_memory):
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory


# Funciones de consulta sobre el catálogo

def getVideosByCategory(catalog, category):
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    category_id = model.cmpVideosCategoryID(catalog,category)
    videos = model.getVideosByCategory(catalog,category_id)
    size = lt.size(videos)
    videos = model.sortVideos(videos,int(size))

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)
    delta = delta_time,delta_memory

    return videos,delta

def getVideosByCategoryAndCountry(catalog, category, country):
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    category_id = model.cmpVideosCategoryID(catalog, category)
    videos = model.getVideosByCountry(catalog, country)
    size = lt.size(videos)
    videos = model.getVideosByCategoryR1(videos, int(size),category_id)
    size2 = lt.size(videos)
    videos_sorted = model.sortVideosByViews(videos,int(size2))

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)
    delta = delta_time,delta_memory
    return videos_sorted,delta

def getVideoByTrendingAndCountry(catalog,country):
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    videos = model.getVideosByCountry(catalog,country)
    size = lt.size(videos)
    videos = model.sortVideosByID(videos,size)
    video = model.getNumByID(videos)

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)
    delta = delta_time,delta_memory
    return video,delta

def getVideoByTrendingAndCategory(catalog,category):
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    category_id = model.cmpVideosCategoryID(catalog,category)
    videos = model.getVideosByCategory(catalog,category_id)
    size = lt.size(videos)
    videos = model.sortVideosByID(videos,size)
    video = model.getNumByID(videos)

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)
    delta = delta_time,delta_memory

    return video,delta

def getVideosByCountryAndTags(catalog,country, tag):
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    videos = model.getVideosByCountry(catalog,country)
    size = lt.size(videos)
    videos = model.getVideosByTags(videos,tag, size)
    size = lt.size(videos)
    videos_sorted = model.sortVideos(videos,int(size))

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)
    delta = delta_time,delta_memory
    return videos_sorted,delta