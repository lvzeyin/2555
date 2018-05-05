# 二分法找方程根的通用函数，加到大家的软件包里去。能够处理单调递增和递减的情况。

import numpy as np
a=float(input('请输入a:'))
b=float(input('请输入b:'))
e=float(input('请输入精确度e:'))
k=0
tr=0
if a>b:
    c=b
    b=a
    a=c
def f(x):
    f=x**2-6*x+4
    return f
while tr==0:
    if f(a)*f(b)>0:
        pass
    elif f(a)*f(b)==0:
        if f(a)==0:
            print(a)
            tr=1
        else:
            print(b)
            tr = 1
    else:
        m=0.5*(a+b)
        if (b-a)<e:
            print(m)
            tr = 1
        else:
            if f(a)*f(m)>0:
                a=m
            else:
                b=m
    k = k + 1
print("近似次数",k)