print("Welcome to the tip Calculator.")

total_bill  = float(input("What was the total bill? $"))

tip_percentage = int(input("What percentage of tip would you like to give? 10, 12 or 15? "))

total_persons = int(input("How many people to split the bill? "))

individual_bill = (total_bill*(100+tip_percentage)/100)/total_persons

print(f"Each person should pay: ${round(individual_bill,2)}")