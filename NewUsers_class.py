class NewUsers():
    def __init__(self,file_name):
        self.file_name = file_name
        try:
            with open(file_name, 'r')
                file_to_write.write(item + '\n')
        except FileNotFoundError as error:
            print('Check your file/path')
            print(error)
        finally:
            print('Program ending')