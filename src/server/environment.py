import map as m
import numpy as np
import random
from PIL import Image
from os.path import exists


#TODO: Creer une SEED et methodes gerant meteo + carte

def checkimg(image):
	"""Cherche l'image image et retourne son chemin, None si introuvable"""

	if exists("../../Images/"+image):
		return "../../Images/"+image
	elif exists("Images/"+image):
		return "Images/"+image
	return None

class Environment:
    def __init__(self):
        '''
        topography  : se recree a partir de l'image,
            topography[x][y] donne la hauteur du point en  pos x,y
        materials    : {material: qteDispo} qteDispo diminue une fois recolte
        lootDict     : {pos: loot} se supprime une fois le loot recupere
        looted       : [pos] contient les pos d'endroits deja loot
        meteoDict    : {IdMeteo : type}
        endedMeteos  : compte le nombre de meteos finies depuis la creation d'environment
        currentMeteos: donnees des meteos actives { spawnDate:{IdMeteo:, pos:, radius:} }
        meteoMap     : contient toutes les meteos pour la duree de service demandee
         { spawnDate:{IdMeteo:, startPos:, radius:, progressionVector:, duration:} }
            spawnDate -> 1 seul meteo peut etre cree par serverTimer -> clef unique
            radius            -> entre 5% - 40% mapSize[1] (hauteur de la carte)
            duration          -> entre 10-40, 1 update de server = 1 duration
            progressionVector -> (x, y) entre -5% - 5% mapSize[]

        '''
        self.mapSize = (m.MAX_X, m.MAX_Y)
        #size = mapSize[1] * mapSize[0]
        self.topography  = np.zeros((m.MAX_X, m.MAX_Y), dtype = int)
        self.materials = {"mirabilite":50, "argile":200, "regolithe":600}
        self.lootDict = {} # repartit les loot sur la carte
        self.looted = [] # supprime les loot sur ces pos
        self.meteoDict = {0: "rien", 1: "tempete de sable", 2: "Vent violent"}
        self.currentMeteos = {} # meteos actives a la date serverTimer
        self.endedMeteos = 0; # compte le nombre de meteos terminees
        self.meteoMap = {} # se recree a partir de la seed


    def generate_topography(self):
        '''
        genere les hauteurs, TODO: rendre cela + accurate
        '''
        FILE = checkimg("map.jpg")
        im = Image.open(FILE, mode='r')
        colormap = list(im.getdata())
        (x, y) = self.mapSize
        for i in range(x):
            temp = i*y
            for j in range(y):
                (r, g, b) = colormap[temp+j]
                if b > r:
                    h = -b*20 - g * 8
                else:
                    h = r * 20 + g * 40
                self.topography[i, j] = h


    def addMeteo(self, spawnDate, pos, IdMeteo, radius, progressionVector, duration):
        self.meteoMap[spawnDate] = {'IdMeteo':IdMeteo, 'startPos':pos,
            'radius':radius, 'progressionVector':progressionVector, 'duration':duration}

    def generate_meteoMap(self, seed, serviceDuration):
        random.seed(seed)
        (max_X, max_Y) = self.mapSize
        minRad, maxRad = round(0.05*max_Y), round(0.4 * max_Y)
        progMinX, progMaxX = -round(0.05*max_X), round(0.05*max_X)
        progMinY, progMaxY = -minRad, minRad
        lastLoad = serviceDuration - 9 # pas besoin de charger les meteos apres
        nextMeteo = 0
        for i in range(self.endedMeteos):
            # recree les valeurs des meteos passees sans les attribuer
            dump = ( random.randint(0, max_X), random.randint(0, max_X) )
            dump = random.randint(0,2)
            dump = random.randint( minRad, maxRad)
            dump = ( random.randint(progMinX, progMaxX), random.randint(progMinY, progMaxY))
            dump = random.randint(10, 40)
            nextMeteo += random.randint(5, 20)
        while nextMeteo < lastLoad:
            startPos = ( random.randint(0, max_X), random.randint(0, max_X) )
            IdMeteo = random.randint(0,2)
            radius = random.randint( minRad, maxRad)
            progress = ( random.randint(progMinX, progMaxX), random.randint(progMinY, progMaxY))
            duration = random.randint(10, 40)
            self.addMeteo(nextMeteo, startPos, IdMeteo, radius, progress, duration )
            nextMeteo += random.randint(5, 20)

    def generate_loot(self, seed):
        random.seed(seed)


    def placeCurrentMeteos(self, serverTimer):
        meteos = self.meteoMap.keys()
        for i in range(serverTimer-40, serverTimer):
            if i in meteos:
                if (i + self.meteoMap[i]['duration']) > serverTimer:
                    (x,y) = self.meteoMap[i]['startPos']
                    (dx, dy) = self.meteoMap[i]['progressionVector']
                    x,y = x + (serverTimer - i) * dx, y + (serverTimer - i) * dy
                    self.currentMeteos[i] = {
                        'pos':(x,y),
                        'radius':self.meteoMap[i]['radius'],
                        'IdMeteo':self.meteoMap[i]['IdMeteo']}

    def updateMeteo(self, serverTimer):
        meteos = self.currentMeteos.keys()
        for k in meteos:
            if k+self.meteoMap[k]['duration'] < serverTimer:
                del self.currentMeteos[k]
            else:
                (x,y)   = self.currentMeteos[k]['pos']
                (dx,dy) = self.meteoMap[k]['progressionVector']
                self.currentMeteos[k]['pos'] = (x+dx, y+dy)
        if serverTimer in self.meteoMap.keys():
            self.currentMeteos[serverTimer] = {
                'pos':self.meteoMap[serverTimer]['startPos'],
                'radius':self.meteoMap[serverTimer]['radius'],
                'IdMeteo':self.meteoMap[serverTimer]['IdMeteo']
            }
    def __str__(self):
        return "c'est pas encore fait"



















'''
end of file
'''
