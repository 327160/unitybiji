#1.九九乘法表
m=1;
n=1;
while n<=9:
      m=1
      while m<=n:
            print(f"{m}X{n}={m*n}",end="\t\t")
            m+=1
      print("")
      n=n+1