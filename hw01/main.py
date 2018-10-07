#正向九九乘法表

for i in range(10):
    for j in range(1,i):
        print("{}x{}={:2}".format(i,j,i*j),"",end="")
    print()
    
#左倒置九九乘法表
#（一）
for i in range(9,0,-1):
    for j in range(i,0,-1):
        print("{}x{}={:2}".format(i,j,i*j),"",end="")
    print()
#（二）
for i in range(9,0,-1):
    for j in range(i,0,-1):
        print("{}x{}={:2}".format((10-i),(10-j),(10-i)*(10-j)),"",end="")
    print()

#右倒置九九乘法表
#（一）
for i in range(1,10):
    for m in range(1,i):
        print(end='        ')
    for j in range(i,10):
        print("{}x{}={:2}\t".format(i,j,i*j),end="")
    print()
#（二）
for i in range(9,0,-1):
    for m in range(1,10-i):
        print(end='        ')
    for j in range(i,0,-1):
        print("{}x{}={:2}\t".format(i,j,i*j),end="")
    print()
