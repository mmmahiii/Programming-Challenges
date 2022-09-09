def convertJoules(richter):
    energyReleased = 10**((1.5*richter)+4.8)
    return energyReleased

def convertTons(joules):
    tonsReleased = joules/(4.184*(10**9))
    return tonsReleased

def earthquakes():
    print ("Richter     Joules                     TNT")
    print (f"1          {convertJoules(1.0)}         {convertTons(convertJoules(1.0))}")
    print (f"5          {convertJoules(5.0)}         {convertTons(convertJoules(5.0))}")
    print (f"9.1        {convertJoules(9.1)}      {convertTons(convertJoules(9.1))}")
    print (f"9.2        {convertJoules(9.2)}      {convertTons(convertJoules(9.2))}")
    print (f"9.5        {convertJoules(9.5)}     {convertTons(convertJoules(9.5))}")
    print ("\n")
    
def userInput():
    richterValue = float(input("Please enter a Richter scale value: "))
    print (f"Richter value: {richterValue}")
    return richterValue

def main():
    earthquakes()
    userValue = userInput()
    numOfJoules = (convertJoules(userValue))
    numOfTNT = (convertTons(numOfJoules))
    print (f"Equivalence in joules: {numOfJoules}")
    print (f"Equivalence in tons of TNT: {numOfTNT}")

main()
