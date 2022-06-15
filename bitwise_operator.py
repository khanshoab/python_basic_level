# It gives the value using truth table.
x = 10
y = 8
print(bin(x))
print(bin(y))

print(x & y)
print(bin(x & y))
# 0b1010
# 0b1000
# 8

print(x | y)
print(bin(x | y))
# 0b1010
# 0b1000
# 0b1000
# 10

print(x ^ y)
print(bin(x ^ y))
# 0b1010
# 0b1000
# 2
# 0b10
