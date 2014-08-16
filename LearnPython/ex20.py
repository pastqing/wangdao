
# -- coding:utf-8 --

from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

#seek 函数
#seek(offset[, whence]) offset 文件的读写指针位置
# whence 这是可选的，默认为0，意味着绝对的文件定位，值为1意味着当然的位置，值为2意味着移动到相对文章尾之后
# seek(p, 0)  seek(p, 1) seek(p, 2)
def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file\n"
print_all(current_file)

print "Now let's rewind, kind of like a type"
rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file),

current_line = current_line + 1 
print_a_line(current_line, current_file),

current_line = current_line + 1
print_a_line(current_line, current_file)


