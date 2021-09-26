class File:

    def __init__(self, filename):

        self.filename = filename

    
    def get_lines(self):

        fyle = open(self.filename, 'r')
        file_lines = fyle.read().splitlines()

        return file_lines
