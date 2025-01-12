#for this project we had to create a tip calculator.
#with this project/lesson we covered:
    # primitive data types
    # type errors/checking/conversion
    # mathematical operations in python
    # number manipulation and f strings

#greeting for the user
print("Welcome to the tip calculator!")

#converts the users input from a string to a decimal/floating point and saves the input as a variable labeld 'bill'
bill = float(input("What was the total bill? $"))

#converts the users input from a string to an integer and saves the input as a variable labeled 'tip'
tip = int(input("What percentage tip would you like to give? 10 12 15 no need for the percent sign."))

#converts the users input from a string to an integer and saves the input as the variable 'people'
people = int(input("How many people to split the bill? "))

#divides the value of the tip by 100 to convert the percentage into a decimal
tip_as_percent = tip / 100

#Multiplies the total bill amount (bill) by the decimal representation of the tip percentage (tip_as_percent)
total_tip_amount = bill * tip_as_percent

#Adds the original bill amount (bill) to the tip amount (total_tip_amount).This gives the final total bill that includes both the base cost and the tip.
total_bill = bill + total_tip_amount

#divides the total amount of the bill by the number of people
bill_per_person = total_bill / people

#this is the total amount that each person must pay, rounded to 2 decimal places i.e $00.00
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")