def convertTemp(air_temp,air_speed):
    tempIndex = 35.74 + 0.6215 * air_temp - 35.75 * air_speed**0.16 + 0.4275 * air_temp * air_speed**0.16
    return tempIndex

def setTemps():
    print (f"Temperature of 10 and speed of 15 gives windchill of: {convertTemp(10,15)}")

setTemps()


