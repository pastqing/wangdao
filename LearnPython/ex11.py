#-- coding:utf-8 --

#接受输入
print "How old are you?",
age = raw_input()
print "How tal are you?",
height = raw_input()
print "How much do u weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy" %(age, height, weight)

# 当输入为纯数字类型时，
# input返回的是数值类型， raw_input返回的是string类型
# 输入字符串为表达式，input会计算在字符串中的数字表达式，而raw_input不会

#输入字符串
myStr = raw_input("input your str "),
print myStr
# 输入整数
myNum = int(raw_input("input your num")),
print myNum;
# 输入浮点数
myFloat = float(raw_input("input your float")),
print myFloat
# 输入16进制数据
nHex = int(raw_input("input num like 0x20"), 16)
print 'nHex = %x' %(nHex)

