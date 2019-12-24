"""
Перетворення звичайного цілого чисоа у римське
"""
Number = int(input("Enter the number:"))
def M():
    Step1 = Number // 1000
    print("M" * Step1, end="")
def D():
    Step2 = Left1 // 500
    print("D" * Step2, end="")
def C():
    Step3 = Left2 // 100
    print("C" * Step3, end="")
def L():
    Step4 = Left3 // 50
    print("L" * Step4, end="")
def X():
    Step5 = Left4 // 10
    print("X" * Step5, end="")
def V():
    Step6 = Left5 // 5
    print("V" * Step6, end="")
def I():
    Step7 = Left6 // 1
    print("I" * Step7, end="")

while True:
    if Number < 4000:
        Left1 = Number % 1000
        M()
        Left2 = Left1 % 500
        D()
        Left3 = Left2 % 100
        C()
        Left4 = Left3 % 50
        L()
        Left5 = Left4 % 10
        X()
        Left6 = Left5 % 5
        V()
        Left7 = Left6 % 1
        I()
        break
    else :
        print("Error")
        break