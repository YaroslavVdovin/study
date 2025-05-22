import json

from warrior_within import Warmonger

class Model:
    @classmethod
    def save(cls):
        """Функция сохранения атрибутов класса в JSON"""
        attrs = [i for i in dir(cls) if i[0] != '_'] # генератор списков + все атрибуты, которые не начинаются с _
        with open("%s_attr_list.txt" % (cls.__name__), "w") as f_class_attr: # создаем файл/перезаписываем всё содержание файла с шаблонным названием
            f_class_attr.write(json.dumps(attrs))

class WarmongerUPD(Warmonger, Model):
    pass

WarmongerUPD.save()
