#6
 availabilityQueue_LIST = [availabilityQueue_UWI, availabilityQueue_Papine, availabilityQueue_Liguanea, \
                              availabilityQueue_HalfWayTree]
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
    for n in range(no_of_passengers):
        passenger = passenger_list[n].split()
        startLocation = passenger[1]
        endLocation = passenger[2]
        moveTaxi(startLocation, endLocation)
    for availabilityQueue in availabilityQueue_LIST:
        for driver in aQueueContents(availabilityQueue):
            print(availabilityQueue_getLocationName(availabilityQueue) + ' - ' + \
                  driver_getFirstName(driver) + ' ' + driver_getLastName(driver) + ' ' + \
                  str(driver_getNumberOfTripsCompleted(driver)))


#7
 availabilityQueue_LIST = [availabilityQueue_UWI, availabilityQueue_Papine, availabilityQueue_Liguanea, \
                              availabilityQueue_HalfWayTree]
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
    for n in range(no_of_passengers):
        passenger = passenger_list[n].split()
        startLocation = passenger[1]
        endLocation = passenger[2]
        moveTaxi(startLocation, endLocation)
    for availabilityQueue in availabilityQueue_LIST:
        for driver in aQueueContents(availabilityQueue):
            print(availabilityQueue_getLocationName(availabilityQueue) + ' - ' + \
                  driver_getFirstName(driver) + ' ' + driver_getLastName(driver) + ' ' + \
                  str(driver_getNumberOfTripsCompleted(driver)))
