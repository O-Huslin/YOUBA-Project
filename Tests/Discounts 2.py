from Youba_queue import*
from Youba_adt import*
      

knownPassengers = {}


fare = 150

taxiLocations = [getlocation_AvailabilityQueue(x)\
                 for x in Routes if getlocation_AvailabilityQueue(x)\
                 in ["UWI", "Papine", "Liguanea", "Half Way Tree"]]


def calculateDiscount(PassengerTelephoneNumber, StartLocation, EndLocation):
    for location in Routes:
        if getlocation_AvailabilityQueue(location) == StartLocation\
           and getlocation_AvailabilityQueue(location) != EndLocation:
            PassengerTelephoneNumber = int(PassengerTelephoneNumber)
            if 'PassengerTelephoneNumber' in knownPassengers:
                if knownPassengers['PassengerTelephoneNumber'] == 1:
                    knownPassengers.update(PassengerTelephoneNumber = 0)
                    return 0.10
                else:
                    return 0
            else:
                knownPassengers.update(PassengerTelephoneNumber = 0)
                return 0
        else:
            if len(get_queuecontents(location)) >=1:
                PassengerTelephoneNumber = int(PassengerTelephoneNumber)
                if 'PassengerTelephoneNumber' in knownPassengers:
                    if knownPassengers['PassengerTelephoneNumber'] == 1:
                        knownPassengers.update(PassengerTelephoneNumber = 0)
                        return 0.10
                    else:
                        return 0
                else:
                    knownPassengers.update(PassengerTelephoneNumber = 0)
                    return 0
            else:
                knownPassengers.update(PassengerTelephoneNumber = 1)
                return "Sorry. There are no vehicles available."
    return "Invalid"


def moveTaxi(startLocation, Endlocation):
    for location in Routes:
        if getlocation_AvailabilityQueue(location) == startLocation:
            driver = front_ThingsQueue(location)
            AvailabilityQueue_enqueue(EndLocation)
            driver_increaseTripsCompleted(driver)
            AvailabilityQueue_dequeue(startLocation)
        elif len(get_queuecontents(location)) > 1:
            driver = front_ThingsQueue(location)
            AvailabilityQueue_enqueue(EndLocation)
            driver_increaseTripsCompleted(driver)
            AvailabilityQueue_dequeue(startLocation)
        else:
            return "N/A"
            
            
            
def requestTaxi(PassengerTelephoneNumber, PassengerLocation,\
                PassengerDestination):
    if PassengerLocation and PassengerDestination in taxiLocations:
        if PassengerLocation == PassengerDestination:
            return "Sorry. Destination and current location are the same."
        elif PassengerLocation != PassengerDestination:
            print("Your taxi fare is: ")
            print(fare * (1 - calculateDiscount(PassengerTelephoneNumber,\
                                                PassengerLocation, PassengerDestination)))
            print("Please confirm trip:")
            request = str(input("Y for yes or N for no:"))
            if request in ["Y", "y"]:
                dis = calculateDiscount(PassengerTelephoneNumber, PassengerLocation,\
                    PassengerDestination)
                for location in Routes:
                    if getlocation_AvailabilityQueue(location) == PassengerLocation\
                       and not isThingsQueue_Empty(location):
                        if type(dis) == int:
                            moveTaxi(PassengerLocation, PassengerDestination)
                            print("Your taxi fare is: ")
                            return (fare - (dis * fare))
                    elif getlocation_AvailabilityQueue(location) != PassengerLocation\
                       and not isThingsQueue_Empty(location):
                        if type(dis) == int:
                            moveTaxi(PassengerLocation, PassengerDestination)
                            print("Your taxi fare is: ")
                            return (fare - (dis * fare))
                    else:
                        knownPassengers.update(PassengerTelephoneNumber = 1)
                        print("Sorry. There are no available vehicles. Please try again later")
                        return "Plese try again."
            elif request in ["N", "n"]:
                return "Your trip has been cancelled"
            else:
                return "Invalid selection. Please try again."
    else:
        return 'Invalid request'

