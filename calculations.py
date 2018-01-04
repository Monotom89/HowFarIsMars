
import numpy
import time
import collections
from skyfield.api import load

ts = load.timescale()
planets = load('de421.bsp')

#create dictionary with all data needed. (body, min distance, max distance)
#Planetary Information taken from Nasa Fact Sheets (https://nssdc.gsfc.nasa.gov/planetary/factsheet/)
celestialsDict = {
"Mercury": [planets["mercury"], 77342099, 221853642],
"Venus": [planets["venus"], 38297055, 260898687],
"Mars": [planets["mars"], 55650408, 401371087],
"Jupiter": [planets["JUPITER_BARYCENTER"], 588518023, 968047821],
"Saturn": [planets["SATURN_BARYCENTER"], 1195436585, 1658441995],
"Uranus": [planets["URANUS_BARYCENTER"], 2581909650, 3157263061],
"Neptune": [planets["NEPTUNE_BARYCENTER"], 4305875512, 4687350083],
"Pluto": [planets["PLUTO_BARYCENTER"], 4293758085, 7533299975],
"Moon": [planets["Moon"], 362102, 404694]
}

def DistanceToEarth(body):
    #return current distance to earth
    t = ts.now()
    astrometric = planets["earth"].at(t).observe(body)
    ra, dec, distance = astrometric.radec()
    return float("{:.2f}".format(distance.km))

def DistanceList():
    #returns a list of distances of the celestials
    DistanceList = []
    for body in collections.OrderedDict(sorted(celestialsDict.items(), key=lambda t: t[0])):
        DistanceList.append(DistanceToEarth(collections.OrderedDict(sorted(celestialsDict.items(), key=lambda t: t[0]))[body][0]))
    return DistanceList

def DistanceRelation(body):
#returns the relative position in percent (0% = closes to earth, 100% = farthest from earth)
  relativePosition = ((DistanceToEarth(celestialsDict[body][0]) - celestialsDict[body][1]) / (celestialsDict[body][2] - celestialsDict[body][1])) * 100
  return relativePosition

def DistanceRelationList():
    DistRelList = []
    for body in collections.OrderedDict(sorted(celestialsDict.items(), key=lambda t: t[0])):
        DistRelList.append(float("{:.2f}".format(DistanceRelation(body))))
    return DistRelList

#testfunctions
#print(DistanceToEarth(celestialsDict["Mars"][0]))
#print(celestialsDict)
#print(collections.OrderedDict(sorted(celestialsDict.items(), key=lambda t: t[0])))
#print(DistanceList())
#print(DistanceRelationList())
