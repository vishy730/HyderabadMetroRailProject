from HydMetro.Input.inputData import *

def getLineofStation(source_station):
    if (source_station in line_1):
        lineNumber = line_1
        return line_1[source_station], lineNumber
    elif (source_station in line_2):
        lineNumber = line_2
        return  line_2[source_station], lineNumber
    elif (source_station in line_3):
        lineNumber = line_3
        return line_3[source_station], lineNumber
    else:
        print("Not present")

def getJunctionsInLine(line):
    junctionsList = []
    for station in line.keys():
        if (station.startswith("X")):
            junctionsList.append((list(line.keys()).index(station)))

    return junctionsList



def getNearestJunction(sourceSt, JunList):
    distList = []
    srcName,linenum = getLineofStation(sourceSt)
    stationIndex = (list(linenum.keys()).index(sourceSt))
    for junIndex in JunList:
        dist = getDistance(stationIndex, junIndex)
        distList.append(dist)
    print("source station:")
    print(sourceSt)
    print("Junction List:")
    print(JunList)
    print("Distance is:")
    print(dist)

    return (stationIndex+min(distList))


def getDistance(stnIndex,stnJnIndex):

    return (abs(stnIndex - stnJnIndex))





