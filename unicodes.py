# Return the Unicode code point for a one-character string
print(f'Unicode code point of char ø is {ord("ø")}')
print(f'Unicode code point of char ø in hex is {hex(ord("ø"))}')

print('-' * 32)

# print ø
print('\u00f8')
print(chr(0xf8))
print(chr(248))

# print 🙂
print('🙂')
print(chr(0x1f642))
print(chr(128578))

# chess pieces
for i in range(9812, 9824):
    print(chr(i), end=' ')
print('')

# card suits
for i in range(9824, 9832):
    print(chr(i), end=' ')
print('')

# music symbols
for i in range(9833, 9840):
    print(chr(i), end=' ')
print('')
for i in range(0x1f3b5, 0x1f3bd):
    print(chr(i) + ' ', end='')
print('')

# emojis
for i in range(128512, 128591):
    print(chr(i), end='')
print('')

for i in range(945, 970):  # Greek lower case
    print(chr(i) + ' ', end='')
print('')
for i in range(913, 938):  # Greek upper case
    print(chr(i) + ' ', end='')
print('')

for i in range(8592, 8704):  # arrows
    print(chr(i) + ' ', end='')
print('')

for i in range(8704, 8866):  # math symbols
    print(chr(i) + ' ', end='')
print('')

for i in range(9312, 9472):
    print(chr(i) + ' ', end='')
print('')

for i in range(8304, 8349):
    print(chr(i) + ' ', end='')
print('')

# print(0x266c)
# print(0x2190)
print(ord('ₜ'))
print(ord('ₛ'))

print("\ue73c")
