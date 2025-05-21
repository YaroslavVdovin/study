class StringVar:
    def __init__(self, strval=''):
        self.strval = strval
    def set(self, strval):
        self.strval = strval
        return strval
    def get(self):
        print(self.strval)
    def __repr__(self):
        return 'Строка содержит: ' + self.strval

firststring = StringVar()
firststring.get()
firststring.set('testing')
firststring.get()
print(firststring)