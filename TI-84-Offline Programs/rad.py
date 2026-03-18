import math

def simplify_sqrt(n):
    if n<0:return None,None
    if n==0:return 0,1
    outside=1
    inside=n
    i=2
    while i*i<=inside:
        while inside%(i*i)==0:
            inside//=(i*i)
            outside*=i
        i+=1
    return outside,inside

def run(eq=None):
    print("\nRADICALS")
    print("--------")
    print("1 Simplify sqrt(n)")
    print("2 Solve sqrt(x)=n")
    print("3 nth root of n")
    print("4 Rationalize 1/sqrt(n)")
    c=input("> ")
    print("")

    if c=="1":
        n=int(input("n= "))
        if n<0:
            print("Step 1: n<0")
            print("Factor out -1")
            print("sqrt({})=sqrt(-1*{})".format(
                n,abs(n)))
            print("= {}i".format(
                round(math.sqrt(-n),4)))
        else:
            o,i=simplify_sqrt(n)
            dec=math.sqrt(n)
            print("Step 1: Find perfect")
            print("square factors of",n)
            print("")
            print("Step 2: Pull out")
            print("perfect squares")
            if i==1:
                print("sqrt({}) = {}".format(n,o))
            else:
                print("sqrt({}) = {}*sqrt({})".format(
                    n,o,i))
            print("")
            print("Decimal: {}".format(round(dec,6)))

    elif c=="2":
        n=float(input("sqrt(x)= "))
        if n<0:
            print("Step 1: Check if valid")
            print("sqrt cant equal negative")
            print("No real solution")
        else:
            x=n**2
            print("Step 1: Square both sides")
            print("(sqrt(x))^2 = {}^2".format(n))
            print("x = {}".format(x))
            print("")
            print("Step 2: Verify")
            print("sqrt({}) = {}".format(
                x,round(math.sqrt(x),4)))

    elif c=="3":
        n=float(input("root= "))
        x=float(input("of x= "))
        if x<0 and n%2==0:
            print("Even root of negative")
            print("= complex result")
        else:
            result=abs(x)**(1/n)
            if x<0:result=-result
            print("Step 1: Apply formula")
            print("{}rt({}) = {}^(1/{})".format(
                int(n),x,x,int(n)))
            print("")
            print("Answer: {}".format(
                round(result,6)))

    elif c=="4":
        n=float(input("n= "))
        if n<=0:
            print("n must be positive")
        else:
            print("Step 1: Multiply by")
            print("sqrt({})/sqrt({})".format(n,n))
            print("")
            print("1/sqrt({})".format(n))
            print("= 1*sqrt({}) / sqrt({})*sqrt({})".format(n,n,n))
            print("= sqrt({}) / {}".format(n,n))
            print("")
            print("Decimal: {}".format(
                round(1/math.sqrt(n),6)))

    input("[ENTER]")
