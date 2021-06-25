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

Routes = [availabilityQueue_UWI, availabilityQueue_Papine, \
          availabilityQueue_Liguanea, availabilityQueue_HalfWayTree]


    
