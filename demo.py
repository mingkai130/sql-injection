
def cut(obj, sec):
    return [obj[i:i+sec] for i in range(0, len(obj), sec)]


#a = input("请输入需要解密的字符：")
a = "25105261592612620975"
b = cut(a, 5)

for i in range(len(b)):
    print(chr(int(b[i])), end="")

print("\n")
#a = input("请输入需要加密的汉字：")
a = "我是明凯"
b = cut(a, 1)
for i in range(len(b)):
    print(ord(b[i]), end="")

