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
 """

import config as cf
import model
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
    loadCategories(catalog)
    loadCategory(catalog)
    loadVideos(catalog)


def loadVideos(catalog):
    videosfile = cf.data_dir + 'Videos/videos-large.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        model.addVideo(catalog, video)

def loadCategory(catalog):
    categoryfile = cf.data_dir +'Videos/category-id.csv'
    input_file = csv.DictReader(open(categoryfile, encoding='utf-8'),delimiter= '\t')
    for category in input_file:
        model.addCategory(catalog,category)

def loadCategories(catalog):
    categoryfile = cf.data_dir + 'Videos/category-id.csv'
    input_file = csv.DictReader(open(categoryfile, encoding='utf-8'),delimiter= '\t')
    for category in input_file:
        model.addCategories(catalog,category)

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

def getVideosByCategory(catalog, category):
    category_id = model.cmpVideosCategoryID(catalog,category)
    videos = model.getVideosByCategory(catalog,category_id)
    size = lt.size(videos)
    videos = model.sortVideos(videos,int(size))
    return videos