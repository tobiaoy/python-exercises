filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

learn = ''
for line in lines:
    learn += line

learn = learn.replace('python', 'javascript')

print(learn)