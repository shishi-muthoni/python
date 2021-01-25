print("welcome to the tip calculator")
bill = float(input("what was the total bill? "))
tip = float(input("what percentage tip would you like to pay? 10, 12 or 15: "))
no_of_people = float(input("How many people to split the bill? "))

amount= bill + ((tip/100)*bill)
per_person = amount/no_of_people
amount_per_person = round(per_person, 2)
amount_per_person2 = "{:.2f}".format(amount_per_person)
print(f"Each person should pay: {amount_per_person}")

print(f"Each person should pay: USD {amount_per_person2} when rounded to 2 d.p")
