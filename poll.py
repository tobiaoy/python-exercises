reason = ''
more_reasons = True
filename = 'programming_poll.txt'

while more_reasons == True:
    while reason == '':
        reason = input("Why do you like programming? \n")
        
    with open(filename, 'a') as file_object:
            file_object.write('{reason} \n'.format(reason=reason))
            reason = ''
    
    cont = ''
    while (cont != 'y') or (cont != 'n') or (cont == ''):
        cont = input("Do you want to add another reason? y/n \n")
        if cont == 'y':
            break
        elif cont == 'n':
            more_reasons = False
            break
            
        