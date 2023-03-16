#Collects desired file name to open as a text file and opens it to be read
myFileName = input("Please enter the name of the file you would like to open: ") 
myFileName += ".txt" 
readFile = open(myFileName, "r") 
#Collects desired file name to write to and opens it to be written to
newFileName = input("Please enter the name of the file you would like to create: ")
newFileName += ".txt"
writeFileName = open(newFileName, "w")
#imports module holding functions
import SupportMod

for line in readFile: 
    #Place contents of the file into a variable
    fileLine = line
    #Creates necessary variables
    commaPosition = fileLine.find(",")
    commaPosition2 = fileLine.find(",",commaPosition +1)
    commaPosition3 = fileLine.find(",",commaPosition2 +1)
    tripDate = fileLine[0:commaPosition]
    fuelUsed = float (fileLine[commaPosition +1:commaPosition2])
    milesTraveled = float (fileLine[commaPosition2 +1:commaPosition3])
    #Calls functions from the module to perform calculations and print results
    tripMileage = SupportMod.Mileage(milesTraveled, fuelUsed)
    SupportMod.DisplayItem(tripDate, fuelUsed, milesTraveled, tripMileage)
    #Writes data to new file that was previously named
    writeFileName.write (tripDate + ", " + str(fuelUsed) + ", " + str(milesTraveled) + ", " + str(tripMileage) + "\n")
#Closes open files
readFile.close ()
writeFileName.close ()