# This is a financial calulator for home loan or investment

import math         # Imports all math funtions to be used in program

# User input,  chooose between a bond or investment calculator

fin_cal_type = input( """Choose either 'investment' or 'bond' from the menu below to proceed:
investment   - to calculate the amount ofinterest you'll earn on interst
bond         - to calculate the amount you'll have to pay on a home loan.\n""").lower()

# Determine the type of calculator required and routes to the relevant equation based on
# user input investment or bond

if fin_cal_type == "investment":                                                     
    dep_amount = float(input("Enter the amount you'd like to deposit: "))          # Define deposit amount variable 
    int_rate   = float(input("Enter the interest rate: "))                         # Define interest amount variable 
    period     = int(input("Enter number of years you'd like to invest: "))        # Define number of years variable 
    interest   = input('Enter type of interest, "simple" or "compound": ').lower()
    
    if interest == "simple":                                                        # Output if investment is simple interest type
        fut_val = dep_amount*(1 + int_rate/100)
        print("The future value of your investment is " + "R" + " " + str(round(fut_val, 2)))
    elif interest == "compound":                                                    # Output if investment is compound interest type
        fut_val =  dep_amount*math.pow(1 + int_rate/100, period)
        print("The future value of your investment is " + "R" + " " + str(round(fut_val, 2)))
    else:
        print("Enter a valid input! ")
        
# Output if user selected a bond as input type instead
# of bond
elif fin_cal_type == "bond":
    val_house = int(input("Enter the present value of the house: "))                # Define house value variable
    int_rate = float(input("Enter the interest rate: "))                            # Define interest rate variable
    period   = int(input("Enter the term in months of the loan: "))                 # Define term in months
    mnt_pay  = val_house*((int_rate/(12*100))*(1 + int_rate /(12*100))**period)/(((1 + int_rate /(12*100))**period)-1)
    print("Your monthly repayment amount is " + "R" + " " + str(round(mnt_pay, 2)))
else:
    print("You have entered an invalid input!")
        
                                                                                

                      
