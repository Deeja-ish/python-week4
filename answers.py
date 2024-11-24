import os

# opening file in read mode
file = open('input.txt', 'r')
openFile = file.read()
print(openFile)

# write mode
file2 = open('output.txt', 'w')
writeFile = file2.write('Hello python')
print(writeFile)

def read_file(filename):
    try:
        with open(filename, 'r') as filename:
             print(filename.read())
    except FileNotFoundError :
        print(f"Error: File {filename}")
    finally:
        print('Any statement')
if __name__ == '__main__':
    filename = input('Enter a filename: ')
    filecontents = read_file(filename)
    print(filecontents)
