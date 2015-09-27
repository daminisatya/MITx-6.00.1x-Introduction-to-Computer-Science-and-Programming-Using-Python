tot = 0.0
for month in range(1,13):
    print "Month:" + str(month)
    minpayamount = float(round(balance*monthlyPaymentRate,2))
    print 'Minimum monthly payment: ' +str(minpayamount)
    balance -= minpayamount
    interest = float(round(annualInterestRate/12*balance,2))
    balance += interest
    tot += minpayamount
    balance = float(round(balance,2))
    print 'Remaining Balance: ' + str(balance)
print 'Total paid:' + str(tot)
print 'Remaining Balance: ' + str(balance)