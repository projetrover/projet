import numpy as np

MAX_Y = 691#2 #  384 #(6912//18)
MAX_X = 1203#2 #668 #(12032//18)

class Map:
    '''
    matrice d'entiers pouvant indiquer differentes infos
    en fct de l'utilisation de la carte
    TODO: conversion depuis une BDD
    '''
    def __init__(self, height, width):
        #https://www.geeksforgeeks.org/initialize-matrix-in-python/
        size = height * width
        self.map = np.array([0]*size).reshape(height, width)
        #TODO: oui

    def __getitem__(self, coords):
        x, y = coords
        return self.map[x][y]

    def set(self, x, y, val):
        self.map[x][y] = val

    def print(self):
        print(self.map)
