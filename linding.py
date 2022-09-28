print("SUBLI Lending Incorporated.")
amount = float(input("Enter Amount :"))
terms = int(input("Terms : "))
if (amount >= 10) and (amount <= 10000):
    interestrate = 0.02
elif (amount > 10000) and (amount <= 30000):
    interestrate = 0.03
elif (amount > 30000) and (amount <= 50000):
    interestrate = 0.05
elif (amount > 50000) and (amount <= 100000):
    interestrate = 0.07
elif (amount > 100000):
    interestrate = 0.08
total_interest = 0
total = 0
principal = amount / terms
Q = 1
original = amount
interest = total 
print("MONTHS     BALANCE         PRINCIPAL    RATE     INTEREST     AMORTIZATION")
for W in range (1, terms+1):
    interest = round(amount * interestrate,2)
    total_interest += interest
    if terms == W:
        t = round(principal,2) * terms
        sobra = original - t
        principal += sobra
    monthly_amortzation = round(interest + principal,2)
    MonthlyAmortization = round(interest + principal,2)
    print("{0:3d}".format(Q),end="  ")
    print("{0:15,.2f}".format(amount),end="  ")
    print("{0:13,.2f}".format (principal),end="")
    print("{0:6,.0f}".format(interestrate * 100),"%",end="")
    print("    ""{0:10,.2f}".format(interest), end="")
    print("{0:13,.2f}".format(MonthlyAmortization),end="")
    amount = amount - round (principal,2)
    Q = Q + 1
    interest += interest
    total += MonthlyAmortization
    print()
print()
print("Total : {0:42,.2f}".format(total_interest),end= " ")
print("{0:12,.2f}".format(total))
