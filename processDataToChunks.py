#!/bin/python
import csv
depTime = []
flightLength = []
with open('outPlanesDepTimeAndFlightTimeOnlyGoodData.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        depTime.append(int(row[0]))
        flightLength.append(str(row[1]))
depTimeFlightLength = zip(depTime, flightLength)
depTimeFlightLength.sort()
for i in range(1,25):
    tempI = i*100
    sum = 0
    count = 1
    for j in range(0, len(depTimeFlightLength)):
        if depTimeFlightLength[j][0] > tempI-100 and depTimeFlightLength[j][0] < tempI:
            #then is in range
            with open(str(i-1)+"file.txt", "a") as file:
                file.write(str(depTimeFlightLength[j][0]) + "," + str(depTimeFlightLength[j][1]) + "\n")
            file.close()
            print depTimeFlightLength[j][1] + " written to " + str(i-1) + "file because it was " + str(depTimeFlightLength[j][0])
