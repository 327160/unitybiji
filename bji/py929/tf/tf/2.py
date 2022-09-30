#相亲时.聊到年龄问题..女孩允许男孩尝试猜3次..3次都没猜对的话...#就直接退出，如果猜对了，
#打印恭喜猜对了信息并退出。
import random
n=random.randint(18,25)
i=1
while i<=3:
      x=int(input("你"+("再" if i>1 else"")+"猜一猜我几岁:"))
      if x==n:
          print("哇,你好棒,猜对了!")
          break;
      i=i+1
if i>3:
      print("你好笨呢!")