# --coding:utf-8 --

from sys import argv

script, filename = argv;

print "Opening file..."
target = open(filename)
print target.read()

target.close()
