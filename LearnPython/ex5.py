# -- coding: utf-8 --

# 格式化字符串

my_name   = 'Zed A. Shaw' # ' '
my_age    =  35 # not a lie
my_height =  74
my_weight =  180
my_eyes   =  'Blue'
my_teeth  =  'White'
my_hair   =  'Brown'

print "Let's talk about %s." %my_name
print "He's %d inches tall" %my_height
print "He's %d pounds heavy" %my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair" %(my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee" %my_teeth

print "If I add %d, %d, and %d I get %d." %(my_age, my_height, my_weight, my_age + my_height + my_weight)

# 字符串格式化
#  字符串 %s
#  浮点数 %f %g %e
#  %r 无论什么都能打印出来
#  用*作为字段宽度或者精度 '%.*s' %(5, 'suqing')
#  装换标志
#  - 左对齐 '%-10.2f ' %pi
#  0 转换值若位数不够用0填充 ‘%010.2f’ %pi
#  + 在转换值之前加上正负号
#  字符串格式化范例
width = input("Please enter width:")
price_width = 10
item_width  = width - price_width
header_format = '%-*s%*s'
format = '%-*s%*.2f'
print '=' *width
print header_format %(item_width, 'Item', price_width, 'Price')

