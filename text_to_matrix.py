def text_to_matrix(text):
    arr = [[c for c in line.strip()] for line in text.split()]
    return arr


def textfile_to_matrix(filename):
    infile = open(filename)
    arr = [[c for c in line.strip()] for line in infile]
    infile.close()
    return arr


# sample input for textfile_to_int_matrix
# 12345
# 23456
# 34567
def textfile_to_int_matrix(filename):
    infile = open(filename)
    arr = [[int(c) for c in line.strip()] for line in infile]
    infile.close()
    return arr


# sample input for textfile_to_int_matrix2
# 12345 456789 789456
# 23456 345678 456123
# 34567 456789 321654
def textfile_to_int_matrix2(filename):
    infile = open(filename)
    arr = [[int(c) for c in line.strip().split()] for line in infile]
    infile.close()
    return arr


if __name__ == '__main__':
    text = '''abcde 
              fghij
              klmno'''
    arr = text_to_matrix(text)
    for e in arr:
        print(e)

    print()

    filename = 'test1.txt'
    arr = textfile_to_matrix(filename)
    for e in arr:
        print(e)

    print()

    filename = 'test2.txt'
    arr = textfile_to_int_matrix(filename)
    for e in arr:
        print(e)

    print()

    filename = 'test3.txt'
    arr = textfile_to_int_matrix2(filename)
    for e in arr:
        print(e)
