print("\nEnter two numbers and I'll add em up")
print("Enter q to quit")

while True:
    first_num = input('\nFirst num: ')
    if first_num == 'q':
        break
    second_num = input('\nSecond num: ')
    if second_num == 'q':
        break 
    
    try:
        answer = int(first_num) + int(second_num)
    except ValueError:
        print('\nAn entry was invalid')
    else:
        print(f"\nYour answer: {answer}")