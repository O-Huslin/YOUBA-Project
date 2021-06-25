
def driver_make(firstname, lastname, carMakeAndModel):
    #Makes the driver
    return ('Driver', [firstname, lastname, carMakeAndModel,\
                       0])
def getDriverInfo(Driver):
    return Driver[1]

def driver_getFirstName(Driver):
    #returns the first name of driver 
    return Driver[1][0]

def driver_getLastName(Driver):
    #returns the last name of the driver 
    return Driver[1][1]

def driver_getCarMakeAndModel(Driver):
    #returns the car make and model of driver 
    return Driver[1][2]

def driver_getNumberOfTripsCompleted(Driver):
    #returns the amount of completed trips made by driver 
    return Driver[1][3]

def driver_increaseTripsCompleted(Driver):
    #increases the number of trips completed
    Driver[1][3] = driver_getNumberOfTripsCompleted(Driver) + 1
    
def is_driver(obj):
    #This function checks to see if any input for driver and if the Driver is valid"""
    return type(obj) == type(()) and obj[0] == 'driver' and type(obj[1]) == type([])

def driver_isNewDriver(Driver):
    #returns True if the driver has made any trips 
    if not is_driver(Driver):
        if driver_getNumberOfTripsCompleted (driver) == 0:
            return True
    return False

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

availabilityQueue_Half= availabilityQueue_make("Half-Way-Tree")

Routes = [availabilityQueue_UWI, availabilityQueue_Papine, \
          availabilityQueue_Liguanea, availabilityQueue_Half]


def calculateDiscount(key):
    key = int(key)
    if key in knownPassengers:
        knownPassengers.update(key = 0)
        return (knownPassengers[key] * 0.10)
    else:
        knownPassengers[key] = 1
        return 0

def calculateFare(StartLocation, EndLocation, PassengerTelephoneNumber):
    dis = calculateDiscount(PassengerTelephoneNumber)
    return float(fare - (fare * dis))


def moveTaxi(startLocation, endLocation):
    end= getAvailabilityQueue(endLocation)
    start= getAvailabilityQueue(startLocation)
    if not isAvailabilityQueue_Empty(start):
            Driver=availabilityQueue_front(start)
            driver_increaseTripsCompleted(Driver)
            availabilityQueue_enqueue(end,Driver)
            availabilityQueue_dequeue(start)
    else:
        if startLocation==endLocation:
            return "The start and end locations are the same"

        
        
        
def requestTaxi(PassengerTelePhoneNumber,PassengerLocation,PassengerDestination):
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
    return AvailabilityQueue[2]

def getAvailabilityQueue(LocationName):
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
        if not isAvailabilityQueue_Empty(availabilityQueue):
            driver = availabilityQueue_front(availabilityQueue)
            print(availabilityQueue_getLocationName(availabilityQueue) + ' - ' + driver_getFirstName(driver) + ' ' + \
                  driver_getLastName(driver) + ' ' + driver_getCarMakeAndModel(driver))

availabilityQueue_LIST = [availabilityQueue_UWI, availabilityQueue_Papine, availabilityQueue_Liguanea, \
                              availabilityQueue_Half]
