utang = eval(input("Enter utang amount ===>  "))
tagal_ng_utang = eval(input("Enter kung gaano katagal in years ===>  "))

months = tagal_ng_utang *12
principal = utang / months
balance = utang
print ("Months\t|\tPrincipal Payment\t|\tRemaining balance\t|\tInterest\t")

for i in range (1, months+1, 1):
    balance -= principal
    interest = balance * 0.03
    months = principal + interest
    print (f"{i}\t|\t{round(principal, 2)}\t\t|\t{round(balance, 2)}\t\t|\t{round(interest, 2)}\t\t|\t{round(months, 2)}")