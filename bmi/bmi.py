# ввод данных
height = float(input('Ваш рост в сантиметрах: ')) / 100
weight = float(input('Ваш вес в килограммах: '))
# расчет
bmi = weight / height**2
# для красоты можно сделать round(bmi)
#print('Ваш индекс массы тела:', round(bmi))
# распишем состояние
if bmi < 16:
   print('Ваш индекс массы тела:', round(bmi), 'Выраженный дефицит массы тела')
elif bmi >= 16 and bmi < 18.5:
   print('Ваш индекс массы тела:', round(bmi), 'Недостаточная (дефицит) масса тела')
elif bmi >= 18.5 and bmi < 25:
   print('Ваш индекс массы тела:', round(bmi), 'Норма')
elif bmi >= 25 and bmi < 30:
   print('Ваш индекс массы тела:', round(bmi), 'Избыточная масса тела (предожирение)')
elif bmi >= 30 and bmi < 35:
   print('Ваш индекс массы тела:', round(bmi), 'Ожирение')
elif bmi >= 35 and bmi < 40:
   print('Ваш индекс массы тела:', round(bmi), 'Ожирение резкое')
elif bmi >= 40:
   print('Ваш индекс массы тела:', round(bmi), 'Очень резкое ожирение')
# Строим график от 0 до 100, теоретически такое может быть.
first = round(bmi)
second = 100 - first
scale = '0' + '=' * (first - 1) + str(first) + '=' * (second - 1) + '100'
# Тут красивее именно так '=' * (first - 1) и '=' * (second - 1)
print('График (0 - 100): \n', scale)
"""
В целом можно предусмотреть вывод относительной шкалы,
но нужно предусмотреть крайние точки и шаг.
Лучшее враг хорошего ;)
"""
print('Построим шаговую шкалу')
step_beg = int(input('Начало шкалы: '))
step_end = int(input('Конец шкалы: '))
step = int(input('Шаг шкалы: '))
first = round(bmi) - step_beg
second = step_end - round(bmi)
scale = str(step_beg) + '=' * (round(first / step) - 1) + str(round(bmi)) + '=' * round((second / step) - 1) + str(step_end)
print('График: \n', scale)