def text_to_matrix(text):
    arr = [[c for c in line.strip()] for line in text.split()]
    return arr


def textfile_to_matrix(filename):
    infile = open(filename)
    arr = [[c for c in line.strip()] for line in infile]
    infile.close()
    return arr


def textfile_to_int_matrix(filename):
    infile = open(filename)
    arr = [[int(c) for c in line.strip()] for line in infile]
    infile.close()
    return arr


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
