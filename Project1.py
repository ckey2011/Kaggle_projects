# Chase Key IS 204-QL Intro to Business Programming

#Collects desired file name to open as a text file and opens it to be read
myFileName = input("Please enter the name of the file you would like to open: ") 
myFileName += ".txt" 
readFile = open(myFileName, "r") 
#Creates variable to written in new text file
completedCalculation = ""

#Read file line by line
for line in readFile: 
    #Place contents of the file into a variable
    fileLine = line
    #Creates necessary variables
    commaPosition = fileLine.find(",")
    commaPosition2 = fileLine.find(",",commaPosition +1)
    commaPosition3 = fileLine.find(",",commaPosition2 +1)
    tripDate = fileLine[0:commaPosition]
    fuelUsed = fileLine[commaPosition +1:commaPosition2]
    milesTraveled = fileLine[commaPosition2 +1:commaPosition3]
    #Calculates the fuel mileage and changes previous variables to floats for calculation and then prints it
    fuelMileage = float(milesTraveled)/float(fuelUsed)
    print(tripDate + ", " + fuelUsed + ", " + milesTraveled + ", " + str(fuelMileage)) 
    #Saves calculated data to previously created variable
    completedCalculation += (tripDate + ", " + (fuelUsed) + ", " + (milesTraveled) + ", " + str(fuelMileage) + "\n")
    
#collects desired file name to create as a text file, opens it to be written into, and writes in the calculated data 
newFileName = input("Please enter the name of the new file you would like the create: ") 
newFileName += ".txt" 
writeFile = open(newFileName, "w") 
writeFile.write (completedCalculation) 
readFile.close () 
writeFile.close () 

