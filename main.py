print("\nWelcome to Compound interest calculator\nThis program calculates your potential returns when you invest\n")


principalAmount = float(input("Enter the principal amount:"))
rate = float(input("Enter the rate:"))
time = int(input("Enter the number of years:"))
compound = int(input("Enter the number of times the interest is compound per year:"))

# SI = (principalAmount * time * rate) / 100
CI = principalAmount * pow((1 + (rate/100) / compound), compound * time)
formatCI = "{:.2f}".format(CI)

# print(f"\nSimple Interest is ${SI}")


list = []

for year2 in range(1, time + 1):
    amount2 = principalAmount * (1.0 + (rate / 100)) ** year2
    formatAmt2 = "{:.2f}".format(amount2)
    list.append(formatAmt2)

count =[]
for countYear in range(1,time+1):
    count.append(countYear)

print("")
print(" Year   StartingBlc    Interest     EndingBlc")
print("----------------------------------------------")
for year in range(time+1):
    try:
        amount = principalAmount * (1.0 + (rate/100)) ** year
        formatAmt = "{:.2f}".format(amount)
        interestAmt = amount * (rate / 100)
        formatInterestAmt = "{:.2f}".format(interestAmt)
        print(f"  {count[year]}      {formatAmt}        {formatInterestAmt}        {list[year]}")
    except:
        pass
print(f"\n${principalAmount} invested at {rate}% for {time} years compounded {compound} times per year is: ${formatCI}")

