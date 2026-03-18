def sf(s):
    try:return float(s),True
    except:return 0.0,False

def parse3(eq):
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
        rest=rest[yi+1:]
    else:
        b=0.0
    if"z"in rest:
        zi=rest.index("z")
        cp=rest[:zi]
        if cp in("","+"):cc=1.0
        elif cp=="-":cc=-1.0
        else:
            v,ok=sf(cp)
            cc=v if ok else 0.0
    else:
        cc=0.0
    return a,b,cc,c

def gauss(m):
    n=3
    for col in range(n):
        mx=abs(m[col][col])
        mr=col
        for row in range(col+1,n):
            if abs(m[row][col])>mx:
                mx=abs(m[row][col])
                mr=row
        m[col],m[mr]=m[mr],m[col]
        if abs(m[col][col])<1e-10:
            return None
        for row in range(col+1,n):
            f=m[row][col]/m[col][col]
            for k in range(col,n+1):
                m[row][k]-=f*m[col][k]
    x=[0.0]*n
    for i in range(n-1,-1,-1):
        x[i]=m[i][n]
        for j in range(i+1,n):
            x[i]-=m[i][j]*x[j]
        x[i]/=m[i][i]
    return x

def run(e1=None,e2=None,e3=None):
    print("\nSYSTEMS 3x3")
    print("-----------")
    if not e1:
        print("ax+by+cz=d")
        e1=input("Eq1: ")
        e2=input("Eq2: ")
        e3=input("Eq3: ")
    r1=parse3(e1)
    r2=parse3(e2)
    r3=parse3(e3)
    if not r1 or not r2 or not r3:
        print("Parse fail")
        print("Eq1:")
        a1=float(input("a= "))
        b1=float(input("b= "))
        c1=float(input("c= "))
        d1=float(input("d= "))
        print("Eq2:")
        a2=float(input("a= "))
        b2=float(input("b= "))
        c2=float(input("c= "))
        d2=float(input("d= "))
        print("Eq3:")
        a3=float(input("a= "))
        b3=float(input("b= "))
        c3=float(input("c= "))
        d3=float(input("d= "))
    else:
        a1,b1,c1,d1=r1
        a2,b2,c2,d2=r2
        a3,b3,c3,d3=r3

    print(e1 if e1 else"Eq1")
    print(e2 if e2 else"Eq2")
    print(e3 if e3 else"Eq3")
    input("[ENTER] next step")

    print("\nStep 1: Form matrix")
    print("[a  b  c  | d]")
    print("[{} {} {} | {}]".format(a1,b1,c1,d1))
    print("[{} {} {} | {}]".format(a2,b2,c2,d2))
    print("[{} {} {} | {}]".format(a3,b3,c3,d3))
    input("[ENTER] next step")

    print("\nStep 2: Row reduce")
    print("Eliminate x from")
    print("Eq2 and Eq3")
    print("")
    print("Then eliminate y")
    print("from Eq3")
    input("[ENTER] next step")

    m=[
        [a1,b1,c1,d1],
        [a2,b2,c2,d2],
        [a3,b3,c3,d3]
    ]
    sol=gauss(m)
    if not sol:
        print("\nNo unique solution")
        input("[ENTER]")
        return

    x,y,z=sol
    print("\nStep 3: Back substitute")
    print("Solve for z first")
    print("then y then x")
    input("[ENTER] next step")

    print("\nAnswer:")
    print("x={}".format(round(x,6)))
    print("y={}".format(round(y,6)))
    print("z={}".format(round(z,6)))
    input("[ENTER] next step")

    print("\nCheck:")
    print("Eq1:{}={}".format(
        round(a1*x+b1*y+c1*z,4),d1))
    print("Eq2:{}={}".format(
        round(a2*x+b2*y+c2*z,4),d2))
    print("Eq3:{}={}".format(
        round(a3*x+b3*y+c3*z,4),d3))
    input("[ENTER]")
