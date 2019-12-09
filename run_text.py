from NewUsers_class import *

try:
    names = NewUsers('names.txt')
    with open(names.file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip('\n'))
    names.file_name
except FileNotFoundError as error:
    print('Check your file')
    print(error)
finally:
    print('Program ending')

try:
    names = NewUsers('names.txt')
    with open(names.file_name, 'a') as file_to_write:
        file_to_write.write(item + '\n')
except FileNotFoundError as error:
    print('Check your file')
    print(error)
finally:
    print('Program ending')

