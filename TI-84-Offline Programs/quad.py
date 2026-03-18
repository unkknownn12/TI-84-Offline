import math

def sf(s):
    try:return float(s),True
    except:return 0.0,False

def parse(eq):
    eq=eq.replace(" ","").replace("x2","x^2")
    if"="not in eq:return None
    l,r=eq.split("=",1)
    rv,ok=sf(r)
    if not ok:return None
    if"x^2"not in l:return None
    parts=l.split("x^2")
    ap=parts[0]
    if ap in("","+"):a=1.0
    elif ap=="-":a=-1.0
    else:
        v,ok=sf(ap)
        a=v if ok else 1.0
    rest=parts[1] if len(parts)>1 else""
    if"x"in rest:
        xi=rest.index("x")
        bp=rest[:xi]
        if bp in("","+"):b=1.0
        elif bp=="-":b=-1.0
        else:
            v,ok=sf(bp)
            b=v if ok else 0.0
        cp=rest[xi+1:]
        v,ok=sf(cp)
        c=(v if ok else 0.0)-rv
    else:
        b=0.0
        v,ok=sf(rest)
        c=(v if ok else 0.0)-rv
    return a,b,c

def run(eq=None):
    print("\nQUADRATIC")
    print("---------")
    if not eq:
        print("ax^2+bx+c=0")
        eq=input("> ")
    r=parse(eq)
    if not r:
        print("Parse fail")
        print("a=?")
        a=float(input())
        print("b=?")
        b=float(input())
        print("c=?")
        c=float(input())
    else:
        a,b,c=r
    d=b**2-4*a*c

    print(eq)
    print("a={} b={} c={}".format(a,b,c))
    input("[ENTER] next step")

    print("\nStep 1: Discriminant")
    print("D = b^2 - 4ac")
    print("D = {}^2 - 4({})({})".format(b,a,c))
    print("D = {} - {}".format(
        round(b**2,4),round(4*a*c,4)))
    print("D = {}".format(round(d,4)))
    if d>0:print("D>0: 2 real roots")
    elif d==0:print("D=0: 1 repeated root")
    else:print("D<0: complex roots")
    input("[ENTER] next step")

    print("\nStep 2: Apply formula")
    print("x=(-b +/- sqrt(D))/2a")
    print("x=(-{} +/- sqrt({}))/{}".format(
        b,round(d,4),2*a))
    input("[ENTER] next step")

    if d>0:
        x1=(-b+math.sqrt(d))/(2*a)
        x2=(-b-math.sqrt(d))/(2*a)
        print("\nStep 3: Two solutions")
        print("x1=({} + {})/{}".format(
            -b,round(math.sqrt(d),4),2*a))
        print("x1={}".format(round(x1,6)))
        print("")
        print("x2=({} - {})/{}".format(
            -b,round(math.sqrt(d),4),2*a))
        print("x2={}".format(round(x2,6)))
        input("[ENTER] next step")

        print("\nStep 4: Verify")
        print("f(x1)={}".format(
            round(a*x1**2+b*x1+c,4)))
        print("f(x2)={}".format(
            round(a*x2**2+b*x2+c,4)))
        print("Both should = 0")

    elif d==0:
        x=-b/(2*a)
        print("\nStep 3: One solution")
        print("D=0: one repeated root")
        print("x = -b/2a")
        print("x = -{}/{}".format(b,2*a))
        print("x = {}".format(round(x,6)))
        input("[ENTER] next step")

        print("\nStep 4: Verify")
        print("f({})={}".format(
            round(x,4),round(a*x**2+b*x+c,4)))
        print("Should = 0")
    else:
        re_=round(-b/(2*a),4)
        im_=round(math.sqrt(-d)/(2*a),4)
        print("\nStep 3: Complex roots")
        print("D<0: no real solutions")
        print("x={}+{}i".format(re_,im_))
        print("x={}-{}i".format(re_,im_))
    input("[ENTER]")
