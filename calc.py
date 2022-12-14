def add():
    def goof(b,c):
        return(b + c)
    b = int(input("first number?: ")); c = int(input("second number?: ")); e = str(input("do u need a third?: "))
    if (e) == "yes":
        d = int(input("what is ur third number?: "))
        print(f"{b} + {c} + {d} is {b + c + d}")
    elif (e) == "no":
        print(f"{b} + {c} is {goof(b,c)}")
#divide for the operators because it hurts my eyes---------------------------------------------------------------------------------------------------------------------
def subtract():
    def moof(f,g):
        return(f - g)
    f = int(input("first number?: ")); g = int(input("second number?: ")); h = str(input("do u need a third?: "))
    if (h) == "yes":
        i = int(input("what is ur third number?: "))
        print(f"{f} - {g} - {i} is {f - g - i}")
    elif (h) == "no":
        print(f"{f} - {g} is {moof(f,g)}")
#divide for the operators because it hurts my eyes---------------------------------------------------------------------------------------------------------------------
def multiply():
    def loof(j,k):
        return(j * k)
    j = int(input("first number?: ")); k = int(input("second number?: ")); l = str(input("do u need a third?: "))
    if (l) == "yes":
        m = int(input("what is ur third number?: "))
        print(f"{j} * {k} * {m} is {j * k * m}")
    elif (l) == "no":
        print(f"{j} * {k} is {loof(j,k)}")
#divide for the operators because it hurts my eyes---------------------------------------------------------------------------------------------------------------------
def divide():
    def joof(n,o):
        return(n / o)
    n = int(input("first number?: ")); o = int(input("second number?: ")); p = str(input("do u need a third?: "))
    if (p) == "yes":
        q = int(input("what is ur third number?: "))
        print(f"{n} / {o} / {q} is {n / o / q}")
    elif (p) == "no":
        print(f"{n} / {o} is {joof(n,o)}")
#divide for the operators because it hurts my eyes---------------------------------------------------------------------------------------------------------------------
def percentages():
    def furry(r,s):
        return(r/s*100)
    r = int(input("first number?: ")); s = int(input("second number?: "))
    print(f"The percentage is: {furry(r,s)}%")
#divide for the operators because it hurts my eyes---------------------------------------------------------------------------------------------------------------------
a = str(input("u wanna add, subtract, divide, multiply, or calculate percentages? (percent): "))
if (a) == "add":
    add()
elif (a) == "subtract":
    subtract()
elif (a) == "multiply":
    multiply()
elif (a) == "divide":
    divide()
elif a == "percent":
    percentages()