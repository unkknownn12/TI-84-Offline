import ti_system

def has_nums(q):
    for c in q:
        if c.isdigit():return True
    return False

def route(q):
    ql=q.lower().replace(" ","")
    ec=q.count("=")
    if">="in q or"<="in q or">"in q or"<"in q:
        if"x"in ql:return"ineq"
    if ec>=2 and"x"in ql and"y"in ql and"z"in ql:return"sys3"
    if ec>=2 and"x"in ql and"y"in ql:return"sys"
    if("x^2"in ql or"x2"in ql)and ec>=1:return"quad"
    if ec==1 and"x"in ql and"y"not in ql:return"lin"
    if has_nums(q):return"stat"
    return"menu"

while True:
    print("\nTI-84 OFFLINE v1.0")
    print("Problem or ENTER=menu")
    q=input("> ")
    if q.strip()=="":
        print("\n1 Linear")
        print("2 Quadratic")
        print("3 Systems 2x2")
        print("4 Systems 3x3")
        print("5 Inequality")
        print("6 Slope/Mid/Dist")
        print("7 Radicals")
        print("8 Statistics")
        c=input("> ")
        if c=="1":
            import lin
            lin.run()
            del lin
        elif c=="2":
            import quad
            quad.run()
            del quad
        elif c=="3":
            import sys_
            sys_.run()
            del sys_
        elif c=="4":
            import sys3
            sys3.run()
            del sys3
        elif c=="5":
            import ineq
            ineq.run()
            del ineq
        elif c=="6":
            import slope
            slope.run()
            del slope
        elif c=="7":
            import rad
            rad.run()
            del rad
        elif c=="8":
            import stat
            stat.run()
            del stat
        continue
    t=route(q)
    if t=="lin":
        import lin
        lin.run(q)
        del lin
    elif t=="quad":
        import quad
        quad.run(q)
        del quad
    elif t=="sys":
        ls=q.strip().split("\n")
        import sys_
        sys_.run(ls[0],ls[1] if len(ls)>=2 else None)
        del sys_
    elif t=="sys3":
        ls=q.strip().split("\n")
        import sys3
        sys3.run(ls[0] if len(ls)>0 else None,
                 ls[1] if len(ls)>1 else None,
                 ls[2] if len(ls)>2 else None)
        del sys3
    elif t=="ineq":
        import ineq
        ineq.run(q)
        del ineq
    elif t=="stat":
        import stat
        stat.run(q)
        del stat
    else:
        print("Use menu")
        print("ENTER=menu")
