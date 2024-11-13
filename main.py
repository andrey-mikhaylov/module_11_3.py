import inspect
from pprint import pprint


def introspection_info(obj):
    result = {'type': type(obj).__name__}
    fields = []
    methods = []
    for attr in dir(obj):
        if callable(getattr(obj, attr)):
            methods.append(attr)
        else:
            fields.append(attr)
    result['attributes'] = fields
    result['methods'] = methods
    module = inspect.getmodule(obj)
    result['module'] = module.__name__ if module else '__main__'
    return result


def test():
    print(introspection_info(42))
    print(introspection_info(introspection_info))
    print(introspection_info(inspect))
    print(introspection_info(inspect.getmodule))
    print(introspection_info(print))
    print(introspection_info(pprint))
    """
    Вывод на консоль:
    {'type': 'int', 'attributes': [...], 'methods': ['__abs__', '__add__', ...], 'module': '__main__'}
    """


if __name__ == '__main__':
    test()


"""
2023/12/26 00:00|Домашнее задание по теме "Интроспекция"
Цель задания:

Закрепить знания об интроспекции в Python.
Создать персональную функции для подробной интроспекции объекта.

Задание:
Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента и проводит интроспекцию этого объекта, чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.

1. Создайте функцию introspection_info(obj), которая принимает объект obj.
2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
  - Тип объекта.
  - Атрибуты объекта.
  - Методы объекта.
  - Модуль, к которому объект принадлежит.
  - Другие интересные свойства объекта, учитывая его тип (по желанию).


Пример работы:
number_info = introspection_info(42)
print(number_info)

Вывод на консоль:
{'type': 'int', 'attributes': [...], 'methods': ['__abs__', '__add__', ...], 'module': '__main__'}

Рекомендуется создавать свой класс и объект для лучшего понимания

Файл с кодом прикрепите к домашнему заданию.
"""
