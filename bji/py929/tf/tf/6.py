#使用循环嵌套打印正等腰三角形1,3,5,7,9
n=5
i=1
while i<=n:
    print(("*"*(2*i-1)).center(2*n-1))
    i+=1