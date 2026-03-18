def sf(s):
    try:return float(s),True
    except:return 0.0,False

def flip(op):
    if op==">":return"<"
    if op=="<":return">"
    if op==">=":return"<="
    if op=="<=":return">="
    return op

def parse(eq):
    op=""
    if">="in eq:op=">="
    elif"<="in eq:op="<="
    elif">"in eq:op=">"
    elif"<"in eq:op="<"
    else:return None
    l,r=eq.split(op,1)
    l=l.replace(" ","")
    r=r.replace(" ","")
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
    return a,b,c,op

def run(eq=None):
    print("\nINEQUALITY")
    print("----------")
    if not eq:
        print("ax+b > c")
        print("Use > < >= <=")
        eq=input("> ")
    r=parse(eq)
    if not r:
        print("Parse fail")
        print("Try: 3x+2>11")
        input("[ENTER]")
        return
    a,b,c,op=r
    if a==0:
        print("No x term")
        input("[ENTER]")
        return

    rhs=c-b
    val=rhs/a
    final_op=flip(op) if a<0 else op

    print(eq)
    input("[ENTER] next step")

    print("\nStep 1: Isolate x term")
    if b>0:
        print("Subtract {} both sides".format(b))
        print("{}x+{}-{} {} {}-{}".format(
            a,b,b,op,c,b))
    elif b<0:
        print("Add {} both sides".format(abs(b)))
        print("{}x{}-{} {} {}+{}".format(
            a,b,b,op,c,abs(b)))
    else:
        print("No constant to move")
    print("{}x {} {}".format(a,op,rhs))
    input("[ENTER] next step")

    print("\nStep 2: Solve for x")
    print("Divide both sides by {}".format(a))
    if a<0:
        print("a<0 so flip sign!")
        print("{} flips to {}".format(op,final_op))
    else:
        print("a>0: sign unchanged")
    print("{}x/{} {} {}/{}".format(
        a,a,final_op,rhs,a))
    input("[ENTER] next step")

    print("\nAnswer:")
    print("x {} {}".format(
        final_op,round(val,6)))
    print("")
    print("Number line:")
    if">"in final_op:
        print("---({})---->".format(round(val,2)))
        print("     open  inf")
    else:
        print("<----({})---".format(round(val,2)))
        print("inf  open")
    input("[ENTER]")
