studentName= input("Whst is your name?: ")
weight= int(input("How much do you weigh?: "))

if weight < 0:
    print("You did not fill in this field") 
elif weight == 0:
    print("You tried and you are on probation")
else:
    print("You are qualified")

