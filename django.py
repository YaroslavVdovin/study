import json

from warrior_within import Warmonger

class Model:
    @classmethod
    def __get_attributes(cls):
        return [i for i in dir(cls) if i[0] != '_']  # генератор списков + все атрибуты
    @classmethod
    def save(cls):
        """Функция сохранения атрибутов класса в JSON"""
        class_name = cls.__name__
        attr_list = cls._Model__get_attributes()
        with open(f"{class_name}_attr_list.txt", "w") as f_class_attr: # создаем файл/перезаписываем всё содержание файла с шаблонным названием
            f_class_attr.write(json.dumps(attr_list))

class WarmongerUPD(Warmonger, Model):
    pass

WarmongerUPD.save()
