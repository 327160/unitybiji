
#猜数字游戏，系统随机生成一个1～10之间的数字，
#用户一共有3次机会，如果用户猜测的数字大于系统给出的数字，
#打印“too big";如果用户猜测的数字小于系统给出的数字，
#打印"too small" ;如果用户猜测的数字等于系统给出的数字，
#打印"恭喜"，并且退出循环;
import random
n=random.randint(1,10)
i=1
while i<=3:
    x=int(input("请输入你要猜的数:"))
    if x>n:
        print("太大了，再猜!")
    if x<n:
        print("太小了，再猜!")
    if x==n:
        print("恭喜你，猜对了")
        break;
    i+=1
if i>3:
    print("你没有猜对,game over！")
