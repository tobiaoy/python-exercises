filename = 'programming.txt'

with open(filename, 'a') as file_object: #there's a w option so the file opens in write mode
    file_object.write('I also love finding meaning in large datasets. \n')
    file_object.write('I love creating apps that can run in a browser. \n')
    
# w - write mode
# r - read mode
# a - append mode
# r+ - read and write
# if you don't add a mode, it will open in read by default