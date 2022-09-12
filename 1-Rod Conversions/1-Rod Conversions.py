def userInput():
    numOfRods = float(input("Input rods: "))
    print(f"You input {numOfRods} rods.")
    print("")
    return numOfRods

def meters(rods):
    return rods*5.0292

def feet(meters):
    return meters/0.3048

def miles(meters):
    return meters/1609.34

def furlongs(rods):
    return rods/40

def minsToWalk(miles):
    return miles/(3.1/60)

rod = userInput()
print (f"Meters: {meters(rod)}")
print (f"Feet: {feet(meters(rod))}")
print (f"Miles: {miles(meters(rod))}")
print (f"Furlongs: {furlongs(rod)}")
print (f"Minutes to walk {rod} Rods: {minsToWalk(miles(meters(rod)))}")
