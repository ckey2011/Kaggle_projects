#Chase Key IS 204-QL Intro to Business Programming
#Imports tkinter module in python
from tkinter import *
from tkinter import filedialog
import os
#Creates function to collect information, calculate gross pay, and save it to a file
def hourlyRate ():
    firstName = txtFname.get()
    lastName = txtLname.get()
    hoursWorked = float(txtHworked.get())
    hourlyWage = float(txtHwage.get())
    grossPay= (hoursWorked*hourlyWage)
    overTimeCalc = ((hoursWorked - 40) * (1.5 * hourlyWage)) + (40 * hourlyWage)
    overTimePay = overTimeCalc if hoursWorked >= 40 else grossPay
    lblList.configure(text = format(grossPay, ".1f"))
    lblList.configure(text=format(overTimePay, ".1f"))
    newFile.write(firstName + ", " +  lastName + ", " + str(hoursWorked) + ", " + str(hourlyWage) + ", " + str(overTimePay) + "\n")
    txtFname.delete(0, END)
    txtLname.delete(0, END)
    txtHworked.delete(0, END)
    txtHwage.delete(0,END)
    txtFname.focus()
#Creates function to create a file to save information to
def FileSave():
    DemoWindow.filename = filedialog.asksaveasfilename(parent=DemoWindow, 
                                                    initialdir=os.getcwd(), 
                                                    title="Please create a filename for your new file.", 
                                                    filetypes = (("text Files", "*.txt"), ("All Files", "*.*")))
    filecontents = DemoWindow.filename + ".txt"
    global newFile
    newFile = open(filecontents, "w")
#Creates function to close the program
def ExitProg():
    newFile.close()
    DemoWindow.destroy()
#Creates window of the main program and sizes it
DemoWindow = Tk()
DemoWindow.title("Assignment 6")
DemoWindow.geometry("800x400")
#Create necessary labels for GUI and where they are located
lblList = Label (DemoWindow, text = "Please enter information to get started.", relief= SUNKEN, width = 20, height = 10, wraplength = 100, anchor= NW, justify = LEFT)
lblList.grid(column= 0, row = 10)
lblFname = Label (DemoWindow, text = "Please enter the first name of the employee:", relief = SUNKEN, width = 36, justify = RIGHT)
lblFname.grid(column = 0, row = 0)
lblLname = Label (DemoWindow, text = "Please enter the last name of the employee:", relief = SUNKEN, width = 36, justify = RIGHT)
lblLname.grid(column = 0, row = 1)
lblHworked = Label (DemoWindow, text = "Please enter the hours worked by the employee:", relief = SUNKEN, width = 36, justify = RIGHT)
lblHworked.grid(column = 0, row = 2)
lblHwage = Label (DemoWindow, text = "Please enter the hourly pay of the employee:", relief = SUNKEN, width = 36, justify = RIGHT)
lblHwage.grid(column = 0, row = 3)
#Creates text entry boxes for user to input information and then places them in the GUI
txtFname = Entry(DemoWindow, width = 20)
txtLname = Entry(DemoWindow, width = 20)
txtHworked = Entry(DemoWindow, width = 20)
txtHwage = Entry(DemoWindow, width= 20)
txtFname.grid(column = 10, row = 0)
txtLname.grid(column = 10, row = 1)
txtHworked.grid(column = 10, row = 2)
txtHwage.grid(column = 10, row = 3)
#Creates button to calculate the gross pay
btngrossPay = Button(DemoWindow, text = "Gross Pay", command = hourlyRate)
btngrossPay.grid(column = 10, row = 5)
#Creates button the close the program
btnExit = Button(DemoWindow, text = "Exit Program", command = ExitProg)
btnExit.grid(column = 20, row = 40)
#Sets the focus point of the program
txtFname.focus()
#Creates a file after opening program by using FileSave function
DemoWindow.after(1,FileSave)
DemoWindow.mainloop()