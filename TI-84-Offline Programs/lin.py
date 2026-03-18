def sf(s):
    try:return float(s),True
    except:return 0.0,False

def parse(eq):
    eq=eq.replace(" ","")
    if"="not in eq:return None
    l,r=eq.split("=",1)
    c,ok=sf(r)
    if not ok:return None
    if"x"not in l:return None
    xi=l.index("x")
    ap=l[:xi]
    if ap in("","+"):a=1.0
    elif ap=="-":a=-1.0
    else:
        v,ok=sf(ap)
        if not ok:return None
        a=v
    rest=l[xi+1:]
    if rest=="":b=0.0
    else:
        v,ok=sf(rest)
        if not ok:return None
        b=v
    return a,b,c

def run(eq=None):
    print("\nLINEAR")
    print("------")
    if not eq:
        print("ax+b=c")
        eq=input("> ")
    r=parse(eq)
    if not r:
        print("Parse fail")
        print("Try: 3x+2=11")
        input("[ENTER]")
        return
    a,b,c=r
    if a==0:
        print("No x term")
        input("[ENTER]")
        return
    x=(c-b)/a

    print(eq)
    print("")
    print("Step 1: Isolate x term")
    if b>0:
        print("Subtract {} both sides".format(b))
        print("{}x+{}-{} = {}-{}".format(a,b,b,c,b))
    elif b<0:
        print("Add {} both sides".format(abs(b)))
        print("{}x{}-{} = {}+{}".format(a,b,b,c,abs(b)))
    else:
        print("No constant to move")
    print("{}x = {}".format(a,c-b))
    input("[ENTER] next step")

    print("\nStep 2: Solve for x")
    print("Divide both sides by {}".format(a))
    print("{}x/{} = {}/{}".format(a,a,c-b,a))
    print("")
    print("Answer: x={}".format(round(x,6)))
    input("[ENTER] next step")

    print("\nStep 3: Verify")
    print("Sub x={} into eq".format(round(x,4)))
    print("{}({})".format(a,round(x,4)),end="")
    if b>=0:print("+{}".format(b))
    else:print("{}".format(b))
    print("= {}".format(round(a*x+b,4)))
    print("Expected: {}".format(c))
    if round(a*x+b,4)==round(c,4):
        print("Correct!")
    input("[ENTER]")
