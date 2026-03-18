import math

def run():
    print("\nSLOPE/MID/DIST")
    print("--------------")
    print("Enter 2 points")
    x1=float(input("x1= "))
    y1=float(input("y1= "))
    x2=float(input("x2= "))
    y2=float(input("y2= "))

    print("\nPoints:")
    print("({},{})".format(x1,y1))
    print("({},{})".format(x2,y2))
    input("[ENTER] next step")

    print("\nStep 1: Slope")
    print("m = (y2-y1)/(x2-x1)")
    if x2-x1==0:
        print("x2-x1=0: undefined")
        print("Vertical line")
        print("x={}".format(x1))
        input("[ENTER]")
        return
    m=(y2-y1)/(x2-x1)
    b=y1-m*x1
    print("m = ({}-{}) / ({}-{})".format(
        y2,y1,x2,x1))
    print("m = {} / {}".format(
        round(y2-y1,4),round(x2-x1,4)))
    print("m = {}".format(round(m,6)))
    input("[ENTER] next step")

    print("\nStep 2: Line equation")
    print("y = mx + b")
    print("b = y1 - m*x1")
    print("b = {}-{}*{}".format(
        y1,round(m,4),x1))
    print("b = {}".format(round(b,4)))
    print("")
    print("y={}x+{}".format(
        round(m,4),round(b,4)))
    if m!=0:
        print("Perp slope={}".format(
            round(-1/m,4)))
    input("[ENTER] next step")

    print("\nStep 3: Midpoint")
    print("M=((x1+x2)/2,(y1+y2)/2)")
    mx=(x1+x2)/2
    my=(y1+y2)/2
    print("M=(({}+{})/2,({}+{})/2)".format(
        x1,x2,y1,y2))
    print("M=({},{})".format(
        round(mx,4),round(my,4)))
    input("[ENTER] next step")

    print("\nStep 4: Distance")
    print("d=sqrt((x2-x1)^2+(y2-y1)^2)")
    dx=round((x2-x1)**2,4)
    dy=round((y2-y1)**2,4)
    d=math.sqrt((x2-x1)**2+(y2-y1)**2)
    print("d=sqrt({}+{})".format(dx,dy))
    print("d=sqrt({})".format(dx+dy))
    print("d={}".format(round(d,6)))
    input("[ENTER]")
