
A=3
B=2
C=1
D=0
while True:
    if D<20:
        D=D+A
        if D<20:
            D=D-B
            print("失败")
            C=C+1
    else:
        print("第",C,"天跳出水井")
        break

















