# Import Tkinter Module - Used to create GUI 
from tkinter import *  # (*) Imports whole module

# Create a user defined clas named: LoanCalculator which holds its own data members and member functions

class LoanCalculator:
    def __init__(self):      # Special method in Python Class - Constructor of a python class
        window = Tk()        # Creates a window to house the calculator bits
        window.title("Loan Calculator")              # sets the title
        window.configure(background = "RoyalBlue1")  # seta the bg color for window

        # Creates input boxes: Label function creates a display noc to take input
        # The grid methofs gives it a table like structure 
        # Widgets are centered by default, Use sticky arguments to change: N S E W

        Label(window, font = "Helvetica 12 bold", background = "RoyalBlue1",
        text = "Annual Interest Rate").grid(row = 1, column = 1 , sticky= W)

        Label(window, font = "Helvetica 12 bold", background = "RoyalBlue1",
        text = "Number of Years").grid(row = 2, column = 1 , sticky= W)

        Label(window, font = "Helvetica 12 bold", background = "RoyalBlue1",
        text = "Loan Amount").grid(row = 3, column = 1 , sticky= W)

        Label(window, font = "Helvetica 12 bold", background = "RoyalBlue1",
        text = "Annual Interest R").grid(row = 4, column = 1 , sticky= W)

        Label(window, font = "Helvetica 12 bold", background = "RoyalBlue1",
        text = "Total Payment").grid(row = 5, column = 1 , sticky= W)
        
        # Create objects: first 3 objects to take inputs using the entry() function

        self.annualInterestRateVar = StringVar()
        Entry(window, textvariable = self.annualInterestRateVar, justify = RIGHT).grid(row = 1, column = 2)

        self.numberOfYearsVar = StringVar()
        Entry(window, textvariable = self.numberOfYearsVar, justify = RIGHT).grid(row = 2, column = 2)

        self.loanAmountVar = StringVar()
        Entry(window, textvariable = self.loanAmountVar, justify = RIGHT).grid(row = 3, column = 2)

        self.monthlyPaymentVar = StringVar()
        lblMonthlyPayment = Label(window, font = "Helvetica 12 bold", background = "RoyalBlue1",
        textvariable = self.monthlyPaymentVar) .grid(row = 4, column = 2, sticky = E)

        self.totalPaymentVar = StringVar()
        lbltotalPayment = Label(window, font = "Helvetica 12 bold", background = "RoyalBlue1",
        textvariable = self.totalPaymentVar) .grid(row = 5, column = 2, sticky = E)
        
        # Creayte button to calculate payment, when button is clicked it will call the calculate payment function

        btcComputePayment = Button(window, text = "Compute Payment", background = "blue",
        font ="Helvetica 12 bold", command = self.computePayment).grid(row =6, column = 2, sticky = E)

        btcClear = Button(window, text = "Clear", background = "red",
        font ="Helvetica 12 bold", command = self.delete_all).grid(row =6, column = 8, padx=20, pady=20, sticky = E)

        window.mainloop()  # The mainlop () function is used to run thr application program

    # Create function to compute the total payment
    def computePayment(self):
        monthlyPayment = self.getMonthlyPayment(
            float(self.loanAmountVar.get()),
            float(self.annualInterestRateVar.get()) / 1200,
            int(self.numberOfYearsVar.get())
        )

        self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))
        totalPayment = float(self.monthlyPaymentVar.get()) * 12 * int(self.numberOfYearsVar.get())

        self.totalPaymentVar.set(format(totalPayment,'10.2f'))

    def getMonthlyPayment(self,loanAmount,monthlyInterestRate,numberOfYears):
        monthlyPayment = loanAmount * monthlyInterestRate / (1-1/(1 + monthlyInterestRate)** (numberOfYears * 12))
        return monthlyPayment

    def delete_all(self):
        self.monthlyPaymentVar.set("")
        self.loanAmountVar.set("")
        self.annualInterestRateVar.set("")
        self.numberOfYearsVar.set("")
        self.totalPaymentVar.set("")

# Call the class to run the program

LoanCalculator()