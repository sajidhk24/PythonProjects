# BMI calculator
Height = float(input("Enter your height in CM: "))
Weight = float(input("Enter your weight in KG: "))
Height = Height/100
BMI = (Weight/(Height*Height))
if BMI < 0:
    print("You are severely under weight")
elif BMI <= 18.5:
    print("You are under weight")
elif BMI <= 25:
    print("You are healthy")
elif BMI <= 30:
    print("You are over-weight")
else:
    print("You are severely over-weight")