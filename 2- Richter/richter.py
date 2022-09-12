def convertJoules(richter):
    energyReleased = 10**((1.5*richter)+4.8)
    return energyReleased

def convertTons(joules):
    tonsReleased = joules/(4.184*(10**9))
    return tonsReleased

def earthquakes():
    print ("Richter     Joules                     TNT")
    print (f"{1:<10}{convertJoules(1.0):<30}{convertTons(convertJoules(1.0)):<30}")
    print (f"{5:<10}{convertJoules(5.0):<30}{convertTons(convertJoules(5.0)):<30}")
    print (f"{9.1:<10}{convertJoules(9.1):<30}{convertTons(convertJoules(9.1)):<30}")
    print (f"{9.2:<10}{convertJoules(9.2):<30}{convertTons(convertJoules(9.2)):<30}")
    print (f"{9.5:<10}{convertJoules(9.5):<30}{convertTons(convertJoules(9.5)):<30}")
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

if __name__ == "__main__":
    main() 
