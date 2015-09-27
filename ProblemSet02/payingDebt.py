monthlyPayment = 10
monthlyInterestRate = annualInterestRate/12
newbalance = balance - 10
while newbalance > 0:
    monthlyPayment += 10
    newbalance = balance
    month = 0
    while month < 12 and newbalance > 0:
        month += 1
        newbalance -= monthlyPayment
        interest = monthlyInterestRate * newbalance
        newbalance += interest
    newbalance = round(newbalance,2)
print " Lowest Payment:", monthlyPayment