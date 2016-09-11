from time import time
from collections import OrderedDict
t0 = time()
line_1 = OrderedDict((('A1', "Miyapur"), ('A2', "JNTU College"), ('A3', "KPHB Colony"),
                    ('A4', "Kukatpally"), ('A5', "Balanagar"), ('A6', "Moosapet"),
                    ('A7', "Bharat Nagar"), ('A8', "Erragadda"), ('A9', "ESI Hospital"),
                    ('A10', "S R Nagar"), ('X1', "Ameerpet"), ('A12', "Punjagutta"),
                    ('A13', "Irrum Manzil"), ('A14', "Khairatabad"), ('A15', "Lakdikapul"),
                    ('A16', "('Assembly"), ('A17', "Nampally"), ('A18', "Gandhi Bhavan"),
                    ('A19', "Osmania Medical College"), ('X2', "MG Bus station"), ('A21', "Malakpet"),
                    ('A22', "New Market"), ('A23', "Musarambagh"), ('A24', "Dilsukhnagar"),
                    ('A25', "Chaitanyapuri"), ('A26', "Victoria Memorial"), ('A27', "L B Nagar")))

line_2 = OrderedDict((('B1', "JBS"), ('X3', "Parade Grounds"), ('B3', "Secunderabad"),
                    ('B4', "Gandhi Hospital"), ('B5', "Musheerabad"), ('B6', "RTC Cross Roads"),
                    ('B7', "Chikkadpally"), ('B8', "Narayanguda"), ('B9', "Sultan ('Bazar"),
                    ('X2', "M G Bus Station"), ('B11', "Salarjung Museum"), ('B12', "Charminar"),
                    ('B13', "Shalibanda"), ('B14', "Shamsher Gunj"), ('B15', "Jungametta"),
                    ('B16', "Falaknuma")))

line_3 = OrderedDict((('C1', "Nagole"), ('C2', "Uppal"), ('C3', "Survey of India"),
                    ('C4', "NGRI"), ('C5', "Habsiguda"), ('C6', "Tarnaka"),
                    ('C7', "Mettuguda"), ('C8', "Secunderabad"), ('X3', "Parade Grounds"),
                    ('C10', "Paradise"), ('C11', "Rasool Pura"), ('C12', "Prakash Nagar"),
                    ('C13', "Begumpet"), ('X1', "Ameerpet"), ('C15', "Madhura Nagar"),
                    ('C16', "Yusuf Guda"), ('C17', "Road No 5 Jubilee Hills"), ('C18', "Jubilee Hills Check Post"),
                    ('C19', "Pedamma Temple"), ('C20', "Madhapur"), ('C21', "Durgam Chervu"),
                    ('C22', "HITEC City"), ('C23', "Shilparamam")))

def printData():
    source_station = str(input().strip())
    destination_station = str(input().strip())

    distance = (list(line_1.keys()).index(destination_station) - list(line_1.keys()).index(source_station))
    print(line_1[source_station])
    print(line_1[destination_station])
    print(distance)

    if (source_station.startswith("A")):
        print("The source is from Line 1")
    elif (source_station.startswith("B")):
        print("The source is from Line 2")
    elif (source_station.startswith("C")):
        print("The source is from Line 3")
    else:
        print("hi")

    if (destination_station.startswith("A")):
        print("The source is from Line 1")
    elif (destination_station.startswith("B")):
        print("The source is from Line 2")
    else:
        print("The source is from Line 3")

import itertools

#print(next(itertools.islice(line_1.values(), 1, 2)))
#print(line_3[source_station])
#printData()