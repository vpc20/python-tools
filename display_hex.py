def display_hex(s):
    # x = ''.join(f'{ord(c):02X} ' for c in s)
    x = ''.join(f'{hex(ord(c))} ' for c in s)
    print(x)


s = 'q \t\n'
display_hex(s)
