from NewUsers_class import *

class NewUsers_info(NewUsers):
    def __init__(self, file_name, text):
        super(). __init__(file_name)
        self.text = text