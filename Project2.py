#Chase Key IS 204-QL Intro to Business Programming
#Create necessary variables
firstName = ""
lastName = ""
completeName = ""
fileName = ""

#Creates a list for the names to be entered into
nameList = [] 
def WholeName(fname, lname):
    newName = lname + "," + fname 
    return newName

#allows the user to enter a person's first and last name as many times as they want and the appends it to the list
looping = True
while(looping):
    firstName = input("Please enter the individual's first name:")
    lastName = input("Please enter the individual's last name:")
    completeName = WholeName(firstName, lastName)
    nameList.append(completeName)
    if (input("Would you like to enter another name? Enter yes or no:") == "no"):
        looping = False

#Sorts the names entered in the list alphabetically
nameList.sort()
#Allows the user to name the file they want the names to be written to and designates it as a text file
fileName = input("Please input the name of the file you would like to create:")
fileName += ".txt"
#Opens named file to be written into
writeFile = open(fileName, "w")
#Turns the list into a string that can be written onto the file and writes the list and then closes the file
writeFile.write ("\n".join(nameList))
writeFile.close ()
