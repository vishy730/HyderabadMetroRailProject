from HydMetro.DerivedInput.derivedInputData import *
from time import time
def printTicket():
    sourceStation = str(input().strip())
    destination_station = str(input().strip())
    t0 = time()
    # distance = (list(line_1.keys()).index(destination_station) - list(line_1.keys()).index(sourceStation))
    # print(line_1[sourceStation])
    # print(line_1[destination_station])
    # print(distance)
    sourceStationName,sourceLine = getLineofStation(sourceStation)
    destinationStationName,destinationLine = getLineofStation(destination_station)

    if (sourceLine != destinationLine):
        # get junctions in each line for source and destination
        sourceJunction = getJunctionsInLine(sourceLine)
        destJunction = getJunctionsInLine(destinationLine)
        # get nearest junction to source and destination
        NearestSourceJunction = getNearestJunction(sourceStation, sourceJunction)
        print("Nearest Source Junction is :" )
        print(NearestSourceJunction)
        NearestDestJunction = getNearestJunction(destination_station, destJunction)
        print("Nearest destination Junction is :")
        print(NearestDestJunction)
        # total distance is the number of stations between source and destination
        #totalDistance = getDistance(sourceStation, NearestSourceJunction) + getDistance(destination_station, NearestDestJunction) + \
                        #getDistance(NearestSourceJunction, NearestDestJunction)

        #calculateTicket(totalDistance, lineNumber)

    else:
        print("hi")

    print("******************************************************")
    print("source station is:", sourceStationName)
    print("destination station is:", destinationStationName)

    print("******************************************************")



printTicket()
print("elapsed time:", round(time()-t0, 3), "s")