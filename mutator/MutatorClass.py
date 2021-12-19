import re
import string

class Mutator:

    def __init__(self, look, change, name):
        self.look_for = look
        self.change_to = change
        self.name = name

    def mutate(self, str):
        return re.sub(self.look_for, self.change_to, str) ##Uses regex substitution

    def get_name(self) -> str:
        return self.name
    
    def get_regex(self):
        return self.look_for
    
