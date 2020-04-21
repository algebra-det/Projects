import hashlib

user = b"GeeksforGeeks"     # Here b is used for encoding it in bytes

# We can also use encode()
# like string.encode()
# OR
# user = "Akash".encode()

# unicode string
string = 'pythön!'

# print string
print('The string is:', string)

# ignore error
print('The encoded version (with ignore) is:', string.encode("ascii", "ignore"))

# replace error
print('The encoded version (with replace) is:', string.encode("ascii", "replace"))

# default encoding to utf-8
string_utf = string.encode()

# print result
print('The encoded version is:', string_utf)

result = hashlib.md5(user)

print("They byte equivalent of hash is : ", result.digest())
