files = ['cats.txt', 'dogs.txt']

def read_file(filename):
    try:
        with open(filename) as f:
            content = f.read()
    except FileNotFoundError:
        pass
    else:
        print(content)
        
for file in files:
    read_file(file)