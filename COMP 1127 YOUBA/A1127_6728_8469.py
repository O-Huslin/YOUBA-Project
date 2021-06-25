"""
Group information:

Member 1: 620118469
Member 2: 620106728

"""

# Global Variables
availabilityQueue_UWI = None
availabilityQueue_Papine = None
availabilityQueue_Liguanea = None
availabilityQueue_HalfWayTree = None

#!/bin/python3

import math
import os
import random
import re
import sys

#
# INCLUDE all functions for PROBLEMS 1 to 8 below.
#
#
def driver_make(firstname, lastname, carMakeAndModel):
    #Makes the driver
    return ('Driver', [firstname, lastname, carMakeAndModel,\
                       0])
def getDriverInfo(driver):
    return driver[1]

def driver_getFirstName(driver):
    #returns the first name of driver 
    return getDriverInfo(driver)[0]

def driver_getLastName(driver):
    #returns the last name of the driver 
    return getDriverInfo(driver)[1]

def driver_getCarMakeAndModel(driver):
    #returns the car make and model of driver 
    return getDriverInfo(driver)[2]

def driver_getNumberOfTripsCompleted(driver):
    #returns the amount of completed trips made by driver 
    return getDriverInfo(driver)[3]

def driver_increaseTripsCompleted(driver):
    #increases the number of trips completed
    getDriverInfo(driver)[3] = driver_getNumberOfTripsCompleted(driver) + 1
    
def driver_isNewDriver(driver):
    #returns True if the driver has made any trips 
    return driver_getNumberOfTripsCompleted(driver) == 0

def availabilityQueue_make(locationName):
    #checks if any drivers available for that location 
    return ("AvailabiltyQueue",locationName,[])


def isAvailabilityQueue(obj):
    #checks if object is a queue
    return type(obj)==type(()) and \
           obj[0] =="AvailabiltyQueue"

def availabilityQueue_getLocationName(AvailabilityQueue):
    #returns the location of a queue
    return str(AvailabilityQueue[1])

def aQueueContents(AvailabilityQueue):
    #returns driver information 
    return AvailabilityQueue[2]

def availabilityQueue_front(AvailabilityQueue):
    #returns the first driver in the queue
    if isAvailabilityQueue(AvailabilityQueue):
        return aQueueContents(AvailabilityQueue)[0]
    else:
        raise TypeError("dequeue: Not A Valid Queue")

def availabilityQueue_enqueue(AvailabilityQueue, driver):
    #adds a driver to the queue
    if isAvailabilityQueue(AvailabilityQueue):
        aQueueContents(AvailabilityQueue).append(driver)
    else:
        raise TypeError ("AvailabilityQueue, enqueue: Not A Valid Queue")

def availabilityQueue_dequeue(AvailabilityQueue):
    #remvoes a driver from the queue
    aQueueContents(AvailabilityQueue).remove(availabilityQueue_front(AvailabilityQueue))

def availabilityQueue_isEmpty(AvailabilityQueue):
    #checks if the queue is empty 
    if isAvailabilityQueue(AvailabilityQueue)== True:
        if aQueueContents(AvailabilityQueue)== []:
            return True
        return False
    else:
        raise TypeError ("Must Be A Valid Queue")

def isAvailabilityQueue_Empty(AvailabilityQueue):
    #checks if the queue is empty 
    if isAvailabilityQueue(AvailabilityQueue)== True:
        if aQueueContents(AvailabilityQueue)== []:
            return True
        return False
    else:
        raise TypeError ("Must Be A Valid Queue")

availabilityQueue_UWI= availabilityQueue_make("UWI")

availabilityQueue_Papine= availabilityQueue_make("Papine")

availabilityQueue_Liguanea= availabilityQueue_make("Liguanea")

availabilityQueue_HalfWayTree= availabilityQueue_make("Half-Way-Tree")


knownPassengers = {4444444: 1}

#fare = 150

def calculateDiscount(key):
    #Calculates the discount for the passenger
    key = int(key)
    if key in knownPassengers:
        knownPassengers.update(key = 0)
        return (knownPassengers[key] * 0.1)
    else:
        knownPassengers[key] = 1
        return 0

def calculateFare(StartLocation, EndLocation, PassengerTelephoneNumber):
    #Calculates the fare of each passenger 
    dis = calculateDiscount(PassengerTelephoneNumber)
    return float(fare - (fare * dis))

def moveTaxi(StartLocation, EndLocation):
    #This moves the taxis from their pick up location to their destination queue
    end = getAvailabilityQueue(EndLocation)
    start = getAvailabilityQueue(StartLocation)
    if not availabilityQueue_isEmpty(start):
        driver = availabilityQueue_front(start)
        driver_increaseTripsCompleted(driver)
        availabilityQueue_enqueue(end, driver)
        availabilityQueue_dequeue(start)
    else:
        if StartLocation == EndLocation:
            return "Start and end locations are the same!"

def getAvailabilityQueue(LocationName):
    #Retrieves the first available driver for a specific location 
    for availabilityQueue in  availabilityQueue_LIST:
        if availabilityQueue_getLocationName(availabilityQueue) == LocationName:
            return availabilityQueue

def requestTaxi(PassengerTelePhoneNumber,PassengerLocation,PassengerDestination):
    #This is to retrieve a taxi for the passenger and showing them their fare for transport
    new_fare=calculateFare(PassengerLocation,PassengerDestination,PassengerTelePhoneNumber)
    if PassengerLocation==PassengerDestination:
        print("Start and end locations are the same!")
        return
    else:
        print(new_fare)
        confirm = str(input('Enter "Y" to confirm the trip or "N" to cancel -'))
        if confirm in ["Y", "y"]:
            if isAvailabilityQueue_Empty(getAvailabilityQueue(PassengerLocation)):
                print("No driver available")
                if PassengerTelePhoneNumber in knownPassengers:
                    knownPassengers[PassengerTelePhoneNumber]+=1
                else:
                    knownPassengers[PassengerTelePhoneNumber]=1
            else:
                knownPassengers.update({PassengerTelePhoneNumber : 0})
                moveTaxi(PassengerLocation,PassengerDestination)   
        else:
            return

def aQueueContents(AvailabilityQueue):
    #returns all the drivers available for a given location queue
    return AvailabilityQueue[2]

def getAvailabilityQueue(LocationName):
    #Retrieves the first available driver for a specific location 
    for availabilityQueue in  availabilityQueue_LIST:
        if availabilityQueue_getLocationName(availabilityQueue) == LocationName:
            return availabilityQueue

def youba_main():
    request = input()
    n = -1
    while (request == 'Y'):
        n += 1
        passenger = passenger_list[n].split()
        PassengerTelephoneNumber = int(passenger[0])
        PassengerLocation = passenger[1]
        PassengerDestination = passenger[2]
        requestTaxi(PassengerTelephoneNumber, PassengerLocation, PassengerDestination)
        request = input()
                         
    print()
    print()
    print('List of Drivers and Number of Jobs Completed :')
    for availabilityQueue in availabilityQueue_LIST:
        for driver in aQueueContents(availabilityQueue):
            print(driver_getFirstName(driver) + ' ' + driver_getLastName(driver) + ' ' + \
                  str(driver_getNumberOfTripsCompleted(driver)))
    print()
    print('List of Locations and Priority Driver :')
    for availabilityQueue in availabilityQueue_LIST:
        if not availabilityQueue_isEmpty(availabilityQueue):
            driver = availabilityQueue_front(availabilityQueue)
            print(availabilityQueue_getLocationName(availabilityQueue) + ' - ' + driver_getFirstName(driver) + ' ' + \
                  driver_getLastName(driver) + ' ' + driver_getCarMakeAndModel(driver))

availabilityQueue_LIST = [availabilityQueue_UWI, availabilityQueue_Papine, availabilityQueue_Liguanea, \
                              availabilityQueue_HalfWayTree]
if __name__ == '__main__':
    no_of_drivers = int(input())
    for i in range(no_of_drivers):
        driver_info = input().strip().split(',')
        driver = driver_make(driver_info[0], driver_info[1], driver_info[2])
        availabilityQueue_enqueue(getAvailabilityQueue(driver_info[3]), driver)
    no_of_passengers = int(input())
    passenger_list = []
    for i in range(no_of_passengers):
        passenger = input()
        passenger_list += [passenger]
    no_of_knownpassengers = int(input())
    knownPassengers = {}
    for i in range(no_of_knownpassengers):
        knownpassenger = list(map(int, input().strip().split()))
        key = knownpassenger[0]
        value = knownpassenger[1]
        knownPassengers[key] = value
    fare = int(input())
    youba_main()
