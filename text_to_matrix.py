def text_to_matrix(text):
    arr = [[c for c in line.strip()] for line in text.split()]
    return arr


def text_file_to_matrix(filename):
    infile = open(filename)
    arr = [[c for c in line.strip()] for line in infile]
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
    arr = text_file_to_matrix(filename)
    for e in arr:
        print(e)
