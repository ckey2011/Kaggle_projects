from tkinter import *
from tkinter import filedialog
import os

from Exam2Module import *


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

receipt = SalesReceipt()
#Creates window of the main program and sizes it
DemoWindow = Tk()
DemoWindow.title("Exam 2")
DemoWindow.geometry("800x400")
#Create necessary labels for GUI and where they are located
lblList = Label (DemoWindow, text = "Please enter information to get started.", relief= SUNKEN, width = 20, height = 10, wraplength = 100, anchor= NW, justify = LEFT)
lblList.grid(column= 0, row = 10)
lblitemName = Label (DemoWindow, text = "Please enter the name of the item:", relief = SUNKEN, width = 36, justify = RIGHT)
lblitemName.grid(column = 0, row = 0)
lblitemQty = Label (DemoWindow, text = "Please enter the quantity of the item:", relief = SUNKEN, width = 36, justify = RIGHT)
lblitemQty.grid(column = 0, row = 1)
lblitemPrice = Label (DemoWindow, text = "Please enter the price of the item:", relief = SUNKEN, width = 36, justify = RIGHT)
lblitemPrice.grid(column = 0, row = 2)
#Creates text entry boxes for user to input information and then places them in the GUI
txtitemName = Entry(DemoWindow, width = 20)
txtitemQty = Entry(DemoWindow, width = 20)
txtitemPrice = Entry(DemoWindow, width = 20)
txtitemName.grid(column = 10, row = 0)
txtitemQty.grid(column = 10, row = 1)
txtitemPrice.grid(column = 10, row = 2)

btnCalc = Button(DemoWindow, text = "Gross Pay", command = SalesTax)
btnCalc.grid(column = 10, row = 5)
#Creates button the close the program
btnExit = Button(DemoWindow, text = "Exit Program", command = ExitProg)
btnExit.grid(column = 20, row = 40)
#Sets the focus point of the program
txtitemName.focus()
#Creates a file after opening program by using FileSave function
DemoWindow.after(1,FileSave)
DemoWindow.mainloop()

