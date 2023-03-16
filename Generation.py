""" Модуль для генерации объектов типа Brak: (Массив данных ЗАГСа)
  ФИО жениха, дата рождения жениха,
  ФИО невесты, дата рождения невесты,
  дата бракосочетания,  номер ЗАГСа
  (сравнение по полям – номер ЗАГСа, дата  бракосочетания, ФИО жениха)
"""

from russian_names import RussianNames  # RussianNames имеет метод get_person(), возвращающий случайное ФИО
import time
import random

def str_time_prop(start, end, time_format, prop):
    # Генерирует случайную дату между двумя датами

    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%d/%m/%Y', prop)

def generation(n):
    """ Генерирует словарь длины n с полями:
    ФИО жениха, дата рождения жениха,
    ФИО невесты, дата рождения невесты,
    дата бракосочетания,  номер ЗАГСа."""

    dictionary = {}
    full_name_hus = []  # ФИО жениха
    b_data_hus = []  # Д/р жениха

    full_name_wife = []  # ФИО невесты
    b_data_wife = []  # Д/р невесты

    mar_date = []  # Дата бракосочетания
    num_zags = []  # Номер ЗАГСа

    for i in range(n):
        full_name_hus.append(RussianNames().get_person(gender=1))
        b_data_hus.append(random_date("1/1/1990", "1/1/2002", random.random()))

        full_name_wife.append(RussianNames().get_person(gender=0))
        b_data_wife.append(random_date("1/1/1990", "1/1/2002", random.random()))

        mar_date.append(random_date("1/1/2020", "1/1/2023", random.random()))
        num_zags.append(random.randrange(1, 6))

    dictionary['ФИО_жениха'] = full_name_hus
    dictionary['ФИО_невесты'] = full_name_wife
    dictionary['Д/р_жениха'] = b_data_hus
    dictionary['Д/р_невесты'] = b_data_wife
    dictionary['Дата_брака'] = mar_date
    dictionary['ЗАГС'] = num_zags
    return dictionary




