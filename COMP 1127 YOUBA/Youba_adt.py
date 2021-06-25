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
