from Youba_queue import*
from Youba_adt import*
      

knownPassengers = {}


fare = 150

taxiLocations = [getlocation_AvailabilityQueue(x)\
                 for x in Routes if getlocation_AvailabilityQueue(x)\
                 in ["UWI", "Papine", "Liguanea", "Half-Way-Tree"]]

knownPassengers = {}

#This one 
def calculateDiscount(key):
    key = int(key)
    if key in knownPassengers:
        knownPassengers.update(key = 0)
        return (knownPassengers[key] * 0.1)
    else:
        knownPassengers[key] = 1
        return 0
#this one
def calculateFare(StartLocation, EndLocation, PassengerTelephoneNumber):
    dis = calculateDiscount(PassengerTelephoneNumber)
    return float(fare - (fare * dis))

#Working on this now 
def moveTaxi(startLocation, Endlocation):
    for location in Routes:
        if getlocation_AvailabilityQueue(location) == startLocation:
            driver = front_AvailabilityQueue(location)
            AvailabilityQueue_enqueue(EndLocation)
            driver_increaseTripsCompleted(driver)
            AvailabilityQueue_dequeue(startLocation)
        elif len(aQueueContents(location)) > 1:
            driver = front_AvailabilityQueue(location)
            AvailabilityQueue_enqueue(EndLocation)
            driver_increaseTripsCompleted(driver)
            AvailabilityQueue_dequeue(startLocation)
        else:
            return "N/A"
            
            
            
def requestTaxi(PassengerTelephoneNumber, PassengerLocation,\
                PassengerDestination):
    dis = (calculateDiscount(PassengerTelephoneNumber,\
                                                PassengerLocation, PassengerDestination))
    if PassengerLocation and PassengerDestination in taxiLocations:
        if PassengerLocation == PassengerDestination:
            return "Sorry. Destination and current location are the same."
        elif PassengerLocation != PassengerDestination and type(dis) == int:
            print("Your taxi fare is: ")
            print(fare * (1 - (dis)))
            print("Please confirm trip:")
            request = str(input("Y for yes or \nN for no:"))
            if request in ["Y", "y"]:
                dis = calculateDiscount(PassengerTelephoneNumber, PassengerLocation,\
                    PassengerDestination)
                for location in Routes:
                    if getlocation_AvailabilityQueue(location) == PassengerLocation\
                     and not isAvailabilityQueue_Empty(location):
                        if type(dis) == int:
                            moveTaxi(PassengerLocation, PassengerDestination)
                            print("Your taxi fare is: ")
                            return (fare - (dis * fare))
                    elif getlocation_AvailabilityQueue(location) != PassengerLocation\
                       and not isAvailabilityQueue_Empty(location):
                        if type(dis) == int:
                            moveTaxi(PassengerLocation, PassengerDestination)
                            print("Your taxi fare is: ")
                            return (fare - (dis * fare))
                    else:
                        knownPassengers.update(PassengerTelephoneNumber = 1)
                        print("Sorry. There are no available taxi. Please try again later")
                        return "Plese try again."
            elif request in ["N", "n"]:
                return "Your trip has been cancelled"
            else:
                return "Invalid selection. Please try again."
        else:
            return "Sorry there are no available taxi. Please try again later"
    else:
        return 'Invalid request'
