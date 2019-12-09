from NewUsers_info_class import *

# try:
#     names = NewUsers('names.txt')
#     with open(names.file_name, 'r') as file:
#         lines = file.readlines()
#         for line in lines:
#             print(line.strip('\n'))
# except FileNotFoundError as error:
#     print('Check your file')
#     print(error)
# finally:
#     print('Program ending')

try:
    names = NewUsers_info('names.txt', 'is fun')
    with open(names.file_name, 'a') as file_to_write:
        file_to_write.writelines(names.file_name + names.text + '\n')
except FileNotFoundError as error:
    print('Check your file')
    print(error)
finally:
    print('Program ending')

