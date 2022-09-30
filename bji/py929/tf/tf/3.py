#相亲时，聊到年龄问题.女孩允许男孩尝试猜3次，3次都没猜对的话.
# #就直接退出，如果猜对了，
# 打印恭喜猜对了信息并退出
s="China"
i=0
x=""
while i<len(s):
      x=x+chr(ord(s[i])+4)
      i=i+1
print(s)
print(x)
