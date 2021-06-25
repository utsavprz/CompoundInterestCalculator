print("--------------------------------------------------------------")
print("\nWelcome to Compound interest calculator\nThis program calculates your potential returns when you invest\n")
print("--------------------------------------------------------------")


principalAmount = float(input("Enter the principal amount:"))
rate = float(input("Enter the rate:"))
time = int(input("Enter the number of years:"))
compound = int(input("Enter the number of times the interest is compound per year:"))

print("")
print(" Year   StartingBlc    Interest     EndingBlc")
print("----------------------------------------------")

Amount = principalAmount
newBlc = 0

for year in range(time):
    for period in range(compound):
        
        oldBlc = Amount + newBlc
        formattedOldBlc = "{:.2f}".format(oldBlc)

        Amount = oldBlc * (rate / (100 * compound))
        formattedAmt = "{:.2f}".format(Amount)

        newBlc = oldBlc + Amount
        formattedNewBlc = "{:.2f}".format(newBlc)

        if period == 0:
            print(year + 1, '  ', period + 1, '  ', formattedOldBlc, '     ', formattedAmt, '      ', formattedNewBlc)
        else:
            print('  ', ' ', period + 1, '  ', formattedOldBlc, '     ', formattedAmt, '      ', formattedNewBlc)

        Amount = 0
    Amount = 0

print(f"\n${principalAmount} invested at {rate}% for {time} years compounded {compound} times per year is: ${formattedNewBlc}")

