def sf(s):
    try:return float(s),True
    except:return 0.0,False

def parse(eq):
    eq=eq.replace(" ","")
    if"="not in eq:return None
    l,r=eq.split("=",1)
    c,ok=sf(r)
    if not ok:return None
    if"x"in l:
        xi=l.index("x")
        ap=l[:xi]
        if ap in("","+"):a=1.0
        elif ap=="-":a=-1.0
        else:
            v,ok=sf(ap)
            a=v if ok else 0.0
        rest=l[xi+1:]
    else:
        a=0.0
        rest=l
    if"y"in rest:
        yi=rest.index("y")
        bp=rest[:yi]
        if bp in("","+"):b=1.0
        elif bp=="-":b=-1.0
        else:
            v,ok=sf(bp)
            b=v if ok else 0.0
    else:
        b=0.0
    return a,b,c

def run(e1=None,e2=None):
    print("\nSYSTEMS 2x2")
    print("-----------")
    if not e1:
        print("ax+by=c")
        e1=input("Eq1: ")
        e2=input("Eq2: ")
    r1=parse(e1)
    r2=parse(e2)
    if not r1 or not r2:
        print("Parse fail")
        a=float(input("a1= "))
        b=float(input("b1= "))
        c=float(input("c1= "))
        d=float(input("a2= "))
        e=float(input("b2= "))
        f=float(input("c2= "))
    else:
        a,b,c=r1
        d,e,f=r2

    det=a*e-b*d

    print(e1)
    print(e2)
    input("[ENTER] next step")

    print("\nStep 1: Determinant")
    print("det = ae - bd")
    print("det = ({})({}) - ({})({})".format(
        a,e,b,d))
    print("det = {} - {}".format(
        round(a*e,4),round(b*d,4)))
    print("det = {}".format(round(det,4)))
    input("[ENTER] next step")

    if det==0:
        print("\ndet=0")
        print("No unique solution")
        print("Lines are parallel")
        print("or identical")
        input("[ENTER]")
        return

    x=(c*e-b*f)/det
    y=(a*f-c*d)/det

    print("\nStep 2: Solve for x")
    print("x = (ce-bf) / det")
    print("x = ({}*{}-{}*{}) / {}".format(
        c,e,b,f,round(det,4)))
    print("x = {}".format(round(x,6)))
    input("[ENTER] next step")

    print("\nStep 3: Solve for y")
    print("y = (af-cd) / det")
    print("y = ({}*{}-{}*{}) / {}".format(
        a,f,c,d,round(det,4)))
    print("y = {}".format(round(y,6)))
    input("[ENTER] next step")

    print("\nAnswer:")
    print("x={}".format(round(x,6)))
    print("y={}".format(round(y,6)))
    print("")
    print("Check:")
    print("Eq1:{}={}".format(
        round(a*x+b*y,4),c))
    print("Eq2:{}={}".format(
        round(d*x+e*y,4),f))
    input("[ENTER]")
