bill = float(input("What's the bill amount? "))

tax = float(input("What's the sales tax? (percentage) "))

tip = float(input("What's the tip ? (percentage) "))


taxamount = (bill * tax) / 100
bilandtax = bill + taxamount

tipamount = (bilandtax * tip) / 100
total = bilandtax + tipamount

total = round(total, 2)

print("The total bill is $", total, sep ='' )

