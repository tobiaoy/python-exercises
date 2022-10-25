import datetime
time = datetime.datetime.now()

new_guest = ''
while new_guest == '': 
    new_guest = input("Please enter your name: ")

filename = 'guest_book.txt'

with open(filename, 'a') as file_obj:
    file_obj.write('{new_guest} - signed in at: {time} \n'.format(new_guest=new_guest, time = time))
    print("Hey {name}, you've been added to the guest list.".format(name=new_guest))