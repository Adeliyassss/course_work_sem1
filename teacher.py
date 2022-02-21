import pandas as pd

df = pd.read_csv('students_algorythm.csv', delimiter=',')
df.index += 1


def back():
    question = input('Хотите ли вы вернуться в меню?---->y/n\n')
    if question == 'y':
        teacher()
    elif question == 'n':
        return
    else:
        print('Try again')
        back()

print('Hello, dear Teacher!')


def teacher():

    a = input('''Пожалуйста наберите номер меню для работы с программой, если закончили, то наберите 9:

1.	Показать список предметов (Показывает список предметов, которую ведет учитель)
2.	Показать список оценок (Показывает список студентов - предмет на который они были записаны, показывает оценки каждого из студентов)
•	Напишите название предмета: >>>(После того как здесь будет написана название предмета выведутся оценки для всех студентов, которые зарегистрированы на тот или иной предмет)
3.	Показать количество студентов (Показывает количество студентов для каждого предмета)
4.	Показать список экзаменов (Показывает список экзаменов по, которым ведет этот студент)
5.	Показать список зачетов (Показывает список зачетов по, которым ведет этот студент)
6.	Показать максимальный бал (Показывает сумму максимального бала того или иного студента за определенный предмет)
•	Наберите название предмета для, которого вы бы хотели посмотреть бал: >>>(После того как здесь будет написана название предмета выведется максимальная оценка и имя студента с максимальной оценкой)
7.	Показать мой минимальный бал. (Показывает сумму минимального бала того или иного студента за определенный предмет)
•	Наберите название предмета для, которого вы бы хотели посмотреть бал: >>>(После того как здесь будет написана название предмета выведется минимальная оценка и имя студента с максимальной оценкой)
8.  Поиск студента по имени и фамилии
9.  Выход из программы''')

    if a == '1':
        print('Algorythm')
        back()

    elif a == '2':
        g = pd.read_csv('students_algorythm.csv', delimiter=',')
        c = g.sort_values(['Algorythm'], ascending=True)
        b = c.reset_index(drop=True)
        b.index += 1
        print(b)
        back()

    elif a == '3':
        print('На предмете алгоритм обучаются', len(df), 'студентов')
        back()
    elif a == '4':
        df3 = pd.read_csv('exam.csv', delimiter=',')
        df3.index += 1
        print(df3)
        back()

    elif a == '5':
        df1 = pd.read_csv('exam.csv', delimiter=',')
        b = df1['Exam'].isin(['Algorythm'])
        print(df1[b])
        back()

    elif a == '6':
        print(df[df['Mid value'] == df['Mid value'].max()])
        back()

    elif a == '7':
        print(df[df['Mid value'] == df['Mid value'].min()])
        back()
    elif a == '8':

        g = pd.read_csv('students_algorythm.csv', delimiter=',')
        c = g.sort_values(['Algorythm'], ascending=True)
        b = c.reset_index(drop=True)
        b.index += 1
        print(b['Algorythm'])
        search = input('Введите фамилию и имя')
        a = g['Algorythm'].isin([search])
        searching = g[a]
        print(searching['Algorythm'])
        back()

    elif a == '9':
        print('The program is finished')
        return

    else:
        print('Try again')
        teacher()


teacher()
