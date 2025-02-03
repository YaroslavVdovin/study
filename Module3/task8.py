import re

s = '''Плыли мы по морю - ветер мачту рвал,
Капитан предатель с корабля сбежал.
Я стоял на лодке и держал весло - 
Чем-то ушатало и меня снесло'''

def splitter(s):
    s = s.replace(',' and '\n', ' ')
    print(s)
    s = s.split(' ')
    s = [i for i in s if len(i) <= 5 and i.isalpha() or len(i) <= 6 and re.search(r'\w-\w', i) != None]
    return s

print(splitter(s))