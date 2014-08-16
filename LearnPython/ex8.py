#-- coding:utf-8 --

formatter = "%r %r %r %r"
print formatter %(1, 2 ,3 ,4)
print formatter %("one", "two", "three", "four")
print formatter %(True, False, False, True)
print formatter %(formatter, formatter, formatter, formatter)

print formatter %(
        "I had this thing",
        "That you could type up right",
        "But it didn't sing", #字符串中有单引号时，会用双引号输出
        "So I'said goodnight")
