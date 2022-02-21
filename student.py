import pandas as pd


df1 = pd.read_csv('exam.csv', delimiter=',')
df2 = pd.read_csv('pass.csv', delimiter=',')
df = pd.read_csv('subjects.csv', delimiter=',')
df1.index += 1
df2.index += 1
df.index += 1


def back():
    question = input('Хотите ли вы вернуться в меню?---->y/n\n')
    if question == 'y':
        student()
    elif question == 'n':
        return
    else:
        print('Try again')
        back()


print('''Приветствую дорогой, Студент Адэля!
Пожалуйста наберите номер меню для работы с программой, если закончили, то наберите 8:''')


def student():
    a = input('''
1.	Показать список предметов (Показывает список предметов на котором учится студент)
2.	Показать список оценки (Показывает предмет и оценки по тем или иным предметам)
3.	Показать список заданий (Показывает список домашних работ по тем или иным предметам)
4.	Показать список экзаменов (Показывает список экзаменов по тем или иным предметам с датами)
5.	Показать список зачетов (Показывает список зачетов по тем или иным предметам с датами)
6.	Показать мой максимальный бал (Показывает сумму максимального бала за тот или иной предмет)
7.	Показать мой минимальный бал. (Показывает сумму минимального бала за тот или иной предмет)
8.  Расписание
9.	Выход (Выходит из программы\n''')

    if a == '1':
        print(df[['Subjects']])
        back()
    elif a == '2':
        print(df[['Subjects', 'Сolloquium1', 'Сolloquium2', 'Сolloquium3']])
        back()
    elif a == '3':
        print(df[['Subjects', 'Tasks']])
        back()
    elif a == '4':
        print(df1)
        back()
    elif a == '5':
        print(df2)
        back()
    elif a == '6':
        b = df[df['Mid value'] == df['Mid value'].max()]
        c = b[['Subjects','Mid value']]
        print(c)
        back()
    elif a == '7':
        b = df[df['Mid value'] == df['Mid value'].min()]
        c = b[['Subjects', 'Mid value']]
        print(c)
        back()

    elif a == '8':
        df3 = pd.read_csv('raspisanie.csv',delimiter=',')
        df3.index += 1
        print(df3)
        back()

    elif a == '9':
        print('Завершается программа')
        return
    else:
        print('Try again')
        student()


student()
