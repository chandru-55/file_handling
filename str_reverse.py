def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
s = "chandru shanmugam"
print("the original string is:",s)
print("reversed string is:")
print(reverse(s))
