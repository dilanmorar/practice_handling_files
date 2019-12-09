from NewUsers_class import *

try:
    with open(file_name, 'r')
        file_to_write.write(item + '\n')
except FileNotFoundError as error:
    print('Check your file/path')
    print(error)
finally:
    print('Program ending')