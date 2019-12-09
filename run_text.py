from NewUsers_info_class import *

try:
    names = NewUsers('names.txt')
    with open(names.file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip('\n'))
except FileNotFoundError as error:
    print('Check your file')
    print(error)
finally:
    print('Program ending')

try:
    names = NewUsers_info('names.txt', 'is funny')
    with open(names.file_name, 'a') as file_to_write:
        file_to_write.writelines(lines[0] + ' ' + names.text + '\n')
        names = NewUsers_info('names.txt', 'is boring')
        file_to_write.writelines(lines[1] + ' ' + names.text + '\n')
        names = NewUsers_info('names.txt', 'is happy')
        file_to_write.writelines(lines[2] + ' ' + names.text + '\n')
        names = NewUsers_info('names.txt', 'is silly')
        file_to_write.writelines(lines[3] + ' ' + names.text + '\n')
        names = NewUsers_info('names.txt', 'is sporty')
        file_to_write.writelines(lines[4] + ' ' + names.text + '\n')
        names = NewUsers_info('names.txt', 'is sleepy')
        file_to_write.writelines(lines[5] + ' ' + names.text + '\n')
        names = NewUsers_info('names.txt', 'is angry')
        file_to_write.writelines(lines[6] + ' ' + names.text + '\n')
        names = NewUsers_info('names.txt', 'is annoying')
        file_to_write.writelines(lines[7] + ' ' + names.text + '\n')
        names = NewUsers_info('names.txt', 'is hungry')
        file_to_write.writelines(lines[8] + ' ' + names.text + '\n')
        names = NewUsers_info('names.txt', 'is smart')
        file_to_write.writelines(lines[9] + ' ' + names.text + '\n')
        names = NewUsers_info('names.txt', 'is funny')
except FileNotFoundError as error:
    print('Check your file')
    print(error)
finally:
    print('Program ending')

