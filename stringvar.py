class StringVar:
    def __init__(self, strval=''):
        self.strval = strval
    def set(self, strval):
        self.strval = strval
    def get(self):
        return self.strval
    def __repr__(self):
        return 'Строка содержит: ' + self.strval

firststring = StringVar()
print(firststring.get())
firststring.set('testing')
print(firststring.get())
print(firststring)
