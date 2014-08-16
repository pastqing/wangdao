# -- coding:utf-8 --

the_count = [1, 2, 3, 4, 5]
fruits = ['apple', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list

for number in the_count:
    print "This is count %d " %number

# same as above

for fruit in fruits:
    print "A fruit of type : %s " % fruit

# also we can go through mixed lists too
# notice we have use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []
# 注意这里添加了6个元素
for i in range(0, 6):
    print "Adding %d to the list." % i
    elements.append(i)

#now we can print them out too
for i in elements:
    print "Element was: %d " % i

# range 用法
# range(1, 5) 代表从1 到 5
suqing = []
for i in range(1, 5):
    suqing.append(i)
print suqing

# range(1, 5, 2)代表从1 到 5 ，间隔2 不包含5

suqing2 = []
for i in range(1, 5, 2):
    suqing2.append(i)
print suqing2

# range(5) 代表从0 到 5（不包含5）

array = [1, 2, 5, 3, 6, 8, 4]
print array[0:] # 列出0以后的

print array[4:] # 列出1以后的

print array[ 3 : -3]











