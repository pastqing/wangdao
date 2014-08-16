
# -- coding: utf-8 -


# +   plus
# -   minus
# /   slash
# *   asterisk
# %   percent
# <   less-than
# >   greater-than
# <=  less-than-equal
# >=  greater-than-equal

print "I will now count my chickens:"
# count The Hens nums
print "Hens", 25 + 30.0 / 6
# count The Roosters nums
print "Roosters", 100 - 25 *3 % 4

print "Now I will count the eggs:"
print 3 + 2 + 1 - 5 + 4 % 2 - 1.0 / 4 + 6 # 9
#浮点数的输出
print 1.0 / 4 
print "Is it true that 3 + 2 < 5 - 7?" # not true
print 3 + 2 < 5 - 7 #False
print "What is 3 + 2?", 3 + 2 # 5 
print "What is 5 - 7?", 5 - 7 # -2
print "Oh, that's why it's False."

print "How about some more."
print "Is it greater?", 5 > -2
print "Is it greater or equal", 5 >= -2
# 浮点数的格式化输出
print ('%.3e %.3f %.3g' %(0.00033333, 0.00033333, 0.00033333))

# e/f/g都指定了精度为3, e输出了4位有效数字（包括3位小数），f输出了3位小数， g输出了3位有效数字


























