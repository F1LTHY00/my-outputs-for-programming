temp = eval(input("What is the temp right now: "))

if temp >= 1 and temp <= 15:
    print ("Temp is considered as extremely cold")
elif temp >= 16 and temp <= 30:
    print ("Cold temperatures")
elif temp >= 31 and temp <= 38:
    print ("Lukewarm temperatures")
elif temp >= 39 and temp <= 42:
    print ("Warm temperatures")
elif temp >= 43 and temp <= 50:
    print ("Hot temperatures")
elif temp >= 51 and temp <= 60:
    print ("Extremely hot temperatures")
elif temp >= 61:
    print ("Burning temperatures")

else: 
    print ("Invalid temperatures")