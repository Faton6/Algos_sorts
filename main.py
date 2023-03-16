# Выполнение основной логики программы: генерация данных, выполнение сортировок,
# подсчет времени, запись результатов и вывод результируещего графика

import copy
import time
import pandas as pd
import matplotlib.pyplot as plt
import datetime

from Brak import Brak
from Generation import generation
from Sortes import selection_sort
from Sortes import quick_sort
from Sortes import shaker_sort

# Задание величины генерируемых массивов
size = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

# Генерация браков (объектов типа Brak) и запись в файл Marrigies.xlsx
with pd.ExcelWriter("./Marrigies.xlsx") as writer:
    for i in size:
        pd.DataFrame(generation(i)).to_excel(writer, sheet_name=f"{i}", index=False)

marrigies = {}
for i in size:
    c = pd.read_excel('./Marrigies.xlsx', sheet_name=f'{i}').to_dict('records')
    marrige = []
    for empl in c:
        marrige.append(
            Brak(empl['ФИО_жениха'], empl['Д/р_жениха'], empl['ФИО_невесты'], empl['Д/р_невесты'], empl['Дата_брака'],
                 empl['ЗАГС'])
        )
    marrigies[i] = marrige

# массивы с временем сортировки каждой выборки
time_sel = []
time_fast = []
time_shaker = []

""" сортировка данных, считанных из файла .xlsx"""
for j in size:
    sorted_arrays = []

    """ Сортировка выбором """
    sorted_arr_sel = copy.deepcopy(marrigies[j])
    start = time.time()
    selection_sort(sorted_arr_sel)
    end = time.time()
    time_sel.append(end - start)
    sorted_arrays.append(sorted_arr_sel)

    """ Шэйкер сортировка """
    sorted_arr_shaker = copy.deepcopy(marrigies[j])
    start = time.time()
    shaker_sort(sorted_arr_shaker)
    end = time.time()
    time_shaker.append(end - start)
    sorted_arrays.append(sorted_arr_shaker)

    """ Быстрая сортировка """
    sorted_arr_fast = copy.deepcopy(marrigies[j])
    start = time.time()
    quick_sort(sorted_arr_fast)
    end = time.time()
    time_fast.append(end - start)
    sorted_arrays.append(sorted_arr_fast)

    for i in range(len(sorted_arrays)):
        dictionary = {}
        full_name_hus = []  # ФИО жениха
        b_data_hus = []  # Д/р жениха

        full_name_wife = []  # ФИО невесты
        b_data_wife = []  # Д/р невесты

        mar_date = []  # Дата бракосочетания
        num_zags = []  # Номер ЗАГСа

        for _ in sorted_arrays[i]:
            full_name_hus.append(_.fio_hus)
            b_data_hus.append(f'{datetime.datetime.fromtimestamp(_.bd_hus):%d/%m/%Y}')

            full_name_wife.append(_.fio_wife)
            b_data_wife.append(f'{datetime.datetime.fromtimestamp(_.bd_wife):%d/%m/%Y}')

            mar_date.append(f'{datetime.datetime.fromtimestamp(_.mar_date):%d/%m/%Y}')
            num_zags.append(_.num_zags)

        dictionary['ФИО_жениха'] = full_name_hus
        dictionary['ФИО_невесты'] = full_name_wife
        dictionary['Д/р_жениха'] = b_data_hus
        dictionary['Д/р_невесты'] = b_data_wife
        dictionary['Дата_брака'] = mar_date
        dictionary['ЗАГС'] = num_zags

        # Запись результатов сортировки
        if i == 0:
            file_name = "./Marrigies_sorted_insert.xlsx"
        elif i == 1:
            file_name = "./Marrigies_sorted_merge.xlsx"
        else:
            file_name = "./Marrigies_sorted_shaker.xlsx"

        # Если файла нет, режим записи, иначе - добавления
        if j == size[0]:
            mode = 'w'
        else:
            mode = 'a'
        with pd.ExcelWriter(file_name, engine="openpyxl", mode=mode) as writer:
            pd.DataFrame(dictionary).to_excel(writer, sheet_name=f"{j}", index=False)

print(f'Сортировка выбором: {time_sel}')
print(f'Шейкер сортировка: {time_shaker}')
print(f'Быстрая сортировка: {time_fast}')

x1 = [i*100 for i in time_sel]
x2 = [i*100 for i in time_shaker]
x3 = [i*100 for i in time_fast]

plt.style.use('ggplot')
plt.title('График времени сортировки')
plt.ylabel('Время умноженное на 100',color='gray')
plt.text(0.01, 9, 'Красная линия')
plt.text(0.01, 8, '- сортировка выбором')

plt.text(0.01, 6, 'Зеленая линия')
plt.text(0.01, 5, '- Шейкер сортировка')

plt.text(0.01, 3, 'Синия линия')
plt.text(0.01, 2, '- быстрая сортировка')
x = [i/10 for i in range(len(size))]
plt.plot(x, x1, 'r-', x, x2, 'g-', x, x3, 'b-')
plt.show()
