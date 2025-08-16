n1 = eval(input("Type the desired amount of the deposit --> "))

print ("Here is a breakdown of the deposited amount")

m = n1

a = m // 1000
m = m % 1000
n = m // 500
m = m % 500
g = m // 200
m = m % 200
e = m // 100
m = m % 100
l = m // 50
m = m % 50
d = m // 20
m = m % 20
l = m // 10
m = n1 % 10
c = m // 5
m = m % 5
r = m // 1
m = m % 1


print ("1000 : ",a)
print ("500 : ",n)
print ("200 : ",g)
print ("100 : ",e)
print ("50 : ",l)
print ("20 : ",d)
print ("10 : ",l)
print ("5 : ",c)
print ("1 : ",r)
