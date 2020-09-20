# ввод данных
person_quant = int(input('Сколько человек? '))
d = {}
for i in range(person_quant):
    name = input('Ваше имя: ')
    d[name] = {'Пол': input('Ваш пол (муж/жен): '),
               'Возраст': int(input('Ваш возраст (полных лет): ')),
               'Рост': float(input('Ваш рост в сантиметрах: ')),
               'Вес': float(input('Ваш вес в килограммах: '))
               }
    d[name]['Индекс'] = bmi = d[name]['Вес'] / (d[name]['Рост'] / 100) ** 2
    print('Ваш индекс массы тела:', round(bmi))
    # Дикое ветвление от условий
    if d[name]['Пол'] == 'муж':
        if d[name]['Возраст'] <= 14:
            if bmi <= 19:
                print(name, 'кушай кашу!')
            elif bmi > 19 and bmi <= 30:
                print(name, 'всё норм парень!')
            elif bmi > 30:
                print(name, 'не налегай на конфеты!')
            else:
                pass
        if d[name]['Возраст'] > 14 and d[name]['Возраст'] <= 40:
            if bmi <= 19:
                print(name, 'ешь мясо, пей пиво!')
            elif bmi > 19 and bmi <= 30:
                print(name, 'всё норм, мужик!')
            elif bmi > 30:
                print(name, 'не налегай на жирное!')
            else:
                pass
        if d[name]['Возраст'] > 40:
            if bmi <= 19:
                print(name, 'ешь мясо, пей пиво!')
            elif bmi > 19 and bmi <= 30:
                print(name, 'всё норм дядя!')
            elif bmi > 30:
                print(name, 'не налегай на жирное!')
            else:
                pass
    elif d[name]['Пол'] == 'жен':
        if d[name]['Возраст'] <= 14:
            if bmi <= 19:
                print(name, 'кушай кашу!')
            elif bmi > 19 and bmi <= 30:
                print(name, 'всё норм девочка!')
            elif bmi > 30:
                print(name, 'не налегай на конфеты!')
            else:
                pass
        if d[name]['Возраст'] > 14 and d[name]['Возраст'] <= 40:
            if bmi <= 19:
                print(name, 'ешь мясо, пей пиво!')
            elif bmi > 19 and bmi <= 30:
                print(name, 'всё норм, женщина!')
            elif bmi > 30:
                print(name, 'не налегай на жирное!')
            else:
                pass
        if d[name]['Возраст'] > 40:
            if bmi <= 19:
                print(name, 'ешь мясо, пей пиво!')
            elif bmi > 19 and bmi <= 30:
                print(name, 'всё норм тётя!')
            elif bmi > 30:
                print(name, 'не налегай на жирное!')
            else:
                pass
    else:
        print(name, ', что ты такое????')
        pass
    # Считаем и выводим шкалу
    print('Построим шаговую шкалу')
    step_beg = int(input('Начало шкалы: '))
    step_end = int(input('Конец шкалы: '))
    step = int(input('Шаг шкалы: '))
    first = round(bmi) - step_beg
    second = step_end - round(bmi)
    d[name]['Шкала'] = scale = str(step_beg) + '=' * (round(first / step) - 1) + \
        str(round(bmi)) + '=' * round((second / step) - 1) + str(step_end)
    print('Шкала: \n', scale)
print(d)
