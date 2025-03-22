#PROGRAM TO CALCULATE SIMPLE INTEREST
principal = float(input("what is your principal?"))
rate = float(input("What is your rate?"))
Time = float(input("What is your time?"))

A  = principal * (1 + (rate/100)*Time)
print ("Total amount:", A)
#PROGRAM TO CALCULATE COMPOUND INTEREST
P = float(input("What is your principal?"))
R = float(input("What is your rate ?"))
n = float(input("what is your number of years?"))
t = float(input("what is your time?"))

A = P*(1+(R/n)**n*t)
print("Total amount:", A)

#PROGRAM FOR CALCULATING ANNUITY PLAN
PMT = float(input("What is your periodic payment amount?"))
R = float(input("What is your rate ?"))
t = float(input("what is your time?"))
n = float(input("what is your number of years?"))
A = PMT * ((1+R/n)**n/t -1  / (R/n))
print ("Total amount:" , A)














