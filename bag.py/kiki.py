# welcome message  
def announcement(fnname):
    print("you are welcome: ")
# greeting
def greet(name):
    print("how are you today!")
# compute course work
def cw(test1:int,test2:int,test3:int) -> int:
    cwmrk = (test1+test2+test3)/3
    return cwmrk
# compute exam
def ex(pr:int,th:int) -> int:
    exmrk = pr+th
    return exmrk

print("welcome to the results app")
stname = input("please enter your name")
greet(stname)
test1 = int("enter score for test1")
test2 = int("enter score for test2")
test3 = int("enter score for test3")
coursework =cw(test1, test2, test3)

