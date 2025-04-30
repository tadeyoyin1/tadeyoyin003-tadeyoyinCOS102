#PROGRAM FOR IZIFIN TECHNOLOGY
staff_name = input("What is your name?")
staff_age = int(input('how old are you?'))
working_years = int(input("How long have you been working for?"))
if staff_age > 25:
    if working_years >= 55:
        print('ANNUAL TAX INCOME IS $5,600,000')
    elif working_years > 20 and staff_age>= 45:
            print('ATR IS $4,480,000')
    elif working_years > 10 and staff_age >= 35:
         print('$1,500,000')
    elif staff_age < 10 and working_years >35:
             print('ATR $550,000')
    else:
        print('No Applicable tax category')






