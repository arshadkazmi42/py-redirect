import sys


class Arguments:

    def __init__(self):
        
        self.args = sys.argv


    def get_filename(self):

        if len(self.args) < 2:
            return False

        return self.args[1]
