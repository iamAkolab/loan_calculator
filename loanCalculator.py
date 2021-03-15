from tkinter import * 

class LoanCalculator:
    def __init__(self):
        window = Tk()
        window.title("Loan Calculator")
        window.configure(background = "RoyalBlue1")

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
        
        self.annualInterestRateVar = StringVar()
        Entry(window, textvariable = self.annualInterestRateVar, justify = RIGHT).grid(row = 1, column = 2)

        self.numberOfYearsVar = StringVar()
        Entry(window, textvariable = self.numberOfYears, justify = RIGHT).grid(row = 2, column = 2)

        self.loanAmountVar = StringVar()
        Entry(window, textvariable = self.loanAmountVar, justify = RIGHT).grid(row = 3, column = 2)

        self.monthlyPaymentVar = StringVar()
        lblMonthlyPayment = Label(window, font = "Helvetica 12 bold", background = "RoyalBlue1",
        textvariable = self.monthlyPaymentVar) .grid(row = 4, column = 2, sticky = E)

        self.totalPaymentVar = StringVar()
        lblMonthlyPayment = Label(window, font = "Helvetica 12 bold", background = "RoyalBlue1",
        textvariable = self.totalPaymentVar) .grid(row = 5, column = 2, sticky = E)

        btcComputePayment = Button(window, text = "Compute Payment", background = "blue",
        font ="Helvetica 12 bold", command = self.computePayment).grid(row =6, column = 2, sticky = E)

        btcClear = Button(window, text = "Clear", background = "red",
        font ="Helvetica 12 bold", command = self.delete_all).grid(row =6, column = 8, padx=20, pady=20, sticky = E)