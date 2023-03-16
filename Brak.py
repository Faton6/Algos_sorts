import datetime
import time

class Brak:
    def __init__(self, fio_hus, bd_hus, fio_wife, bd_wife, mar_date, num_zags):
        # Конструктор класса
        self.fio_hus = fio_hus  # ФИО жениха
        self.bd_hus = time.mktime(datetime.datetime.strptime(bd_hus, "%d/%m/%Y").timetuple())  # Д/р жениха
        print()
        self.fio_wife = fio_wife  # ФИО невесты
        self.bd_wife = time.mktime(datetime.datetime.strptime(bd_wife, "%d/%m/%Y").timetuple())  # Д/р невесты
        self.mar_date = time.mktime(datetime.datetime.strptime(mar_date, "%d/%m/%Y").timetuple())  # Дата бракосочетания
        self.num_zags = num_zags  # Номер ЗАГСа
    def __lt__(self, other):
        # Сравнение по полям – номер ЗАГСа, дата  бракосочетания, ФИО жениха
        # Перегрузка оператора <

        if self.num_zags != other.num_zags:
            return self.num_zags < other.num_zags
        if self.mar_date != other.mar_date:
            return self.mar_date < other.mar_date
        return self.fio_hus < other.fio_hus

    def __le__(self, other):
        # Перегрузка оператора <=
        if self.num_zags <= other.num_zags:
            return self.num_zags <= other.num_zags
        if self.mar_date <= other.mar_date:
            return self.mar_date <= other.mar_date
        return self.fio_hus < other.fio_hus

    def __gt__(self, other):
        # Перегрузка оператора >
        if self.num_zags != other.num_zags:
            return self.num_zags > other.num_zags
        if self.mar_date != other.mar_date:
            return self.mar_date > other.mar_date
        return self.fio_hus > other.fio_hus

    def __ge__(self, other):
        # Перегрузка оператора >=
        if self.num_zags >= other.num_zags:
            return self.num_zags >= other.num_zags
        if self.mar_date >= other.mar_date:
            return self.mar_date >= other.mar_date
        return self.fio_hus >= other.fio_hus
