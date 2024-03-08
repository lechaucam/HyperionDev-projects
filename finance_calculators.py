import math

print ("investment - to calculate the amount of interest you'll earn on your investment")
print ("bond - to calculate the amount you'll have to pay on a home loan")
print ("")

# user needs to choose an investment calculator by entering 'investment'
# or home loan repayment calculator by entering 'bond'
calculator = input ("Please enter investment or bond: " )

# if user chooses investment then use simple or compound interest calculator
if calculator in ["investment" , "Investment" , "INVESTMENT"]:
    deposit = float(input("Please enter deposit amount: " ))
    interest_rate = float(input("Please enter interest rate: " ))
    investment_years = float(input("Please investment duration in years: "))
    interest = input("Please choose simple or compound interest: ")
    
# user needs to choose simple or compound interest and calculation result will be printed
    if interest == "simple":
        simple_interest = deposit * (1 + (interest_rate/100) * investment_years)
        print ("Your total investment will be worth " + str(round(simple_interest)))

    elif interest == "compound":
        compound_interest = deposit * math.pow((1+(interest_rate/100)),investment_years)
        print  ("Your total investment will be worth " + str(round(compound_interest)))
    
    else:
        print ("Your input is incorrect, please try again.")

# if user chooses bond then use repayment calculator and monthly repayment will be printed   
elif calculator in ["bond" , "Bond" , "BOND"]:
    present_value_house = float(input("Please enter present value of house: "))
    yearly_interest = float(input("Please enter interest rate: " ))
    repayment_months = float(input("Please repayment duration in months: "))

    monthly_interest = (yearly_interest/100)/12
    repayment = ((monthly_interest) * present_value_house)/(1-(1+monthly_interest)**(-repayment_months))
    print ("Your monthly repayment will be " + str(round(repayment)))

else:
    print ("Your input is incorrect, please try again.")