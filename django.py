import json

from warrior_within import Warmonger

class Model:
    @staticmethod
    def saving(new_class):
        """Функция сохранения атрибутов класса в JSON"""
        attrs = [i for i in dir(new_class) if i[0] != '_'] # генератор списков + все атрибуты, которые не начинаются с _
        with open("%s_attr_list.txt" % (new_class.__name__), "w") as f_class_attr: # создаем файл/перезаписываем всё содержание файла с шаблонным названием
            f_class_attr.write(json.dumps(attrs))

Model.saving(Warmonger)
