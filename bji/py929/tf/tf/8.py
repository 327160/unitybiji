#for版九九口诀表
for n in range(1,10):
    for m in range(1,n+1):
        print(f"{m}X{n}={m*n}",end=" ")
    print("")