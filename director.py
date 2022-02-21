import pandas as pd
import csv

df = pd.read_csv('students.csv', delimiter=',')
df1 = pd.read_csv('teachers.csv', delimiter=',')
df2 = pd.read_csv('all_students.csv', delimiter=',')
df.index += 1
df1.index += 1
df2.index += 1


def ask_question():
    ask = input('If tou want to return to the menu "y", "n" program exit').lower()
    if ask == 'y':
        director()
    elif ask == 'n':
        return
    else:
        print('There is no such value, try again')
        ask_question()


def adding():
    name = input('Enter the name of teacher:').strip()
    subject = input('Enter the subject:')
    save = name, subject
    with open('teachers.csv', 'a', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(save)
    print('Teacher', name, 'was added')


def adding_students():
    name = input('Enter the name of student:').strip()
    specialty = input('Enter the specialty')
    save = name, specialty
    with open('all_students.csv', 'a', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(save)
    print('Student ', name, 'was added')


print('Hello, dear Director!')


def director():
    a = input('''
Please, dial the menu number to work with the program, if you have finished, then dial 11:
1. Show list of subjects (Shows the list of subjects that are available in the education center)
2. Show number of students (Shows the number of students for each subject)
3.	Show Teacher List (Shows the number of teachers and the subject they teach)
4.	Add teacher
5.	Delete teacher
6.  See all students that are in the school
7.  Add a student
8.  Delete a student
9.  Search for students
10. Search faculty
11.  Exit the program
''')

    if a == '1':
        print(df[['Subjects']])
        ask_question()

    elif a == '2':
        print(df)
        ask_question()

    elif a == '3':
        g = pd.read_csv('teachers.csv', delimiter=',', encoding='utf-8')
        c = g.sort_values(['Teacher'], ascending=True)
        b = c.reset_index(drop=True)
        b.index += 1
        print(b)
        ask_question()

    elif a == '4':
        adding()
        ask_question()

    elif a == '5':
        g = pd.read_csv('teachers.csv', delimiter=',', encoding='utf-8')
        c = g.sort_values(['Teacher'], ascending=True)
        b = c.reset_index(drop=True)
        b.index += 1
        print(b)
        teacher = input('Enter the name: ').strip()
        with open('teachers.csv', 'r', encoding='utf-8') as f:
            teachers = f.readlines()
        teacher_found = [x for x in teachers if x.split(',')[0].lower() == teacher.lower()]
        if teacher_found:
            print('The teacher deleted: {}'.format(teacher))
            teachers.remove(teacher_found[0])
            with open('teachers.csv', 'w', encoding='utf-8') as f:
                f.write(''.join(teachers))
        else:
            print('Sorry! The teacher "{}" was not found.'.format(teacher))
        ask_question()

    elif a == '6':
        df3 = pd.read_csv('all_students.csv', delimiter=',', encoding='utf-8')
        c = df3.sort_values(['All students'], ascending=True)
        b = c.reset_index(drop=True)
        b.index += 1
        print(b)
        ask_question()

    elif a == '7':
        adding_students()
        ask_question()

    elif a == '8':
        g = pd.read_csv('all_students.csv', delimiter=',', encoding='utf-8')
        c = g.sort_values(['All students'], ascending=True)
        b = c.reset_index(drop=True)
        b.index += 1
        print(b)
        student = input('Введите фамилию и имя: ')
        with open('all_students.csv', 'r', encoding='utf-8') as f:
            students = f.readlines()
        student_found = [x for x in students if x.split(',')[0].lower() == student.lower().strip()]
        if student_found:
            print('Студент был удален: {}'.format(student))
            students.remove(student_found[0])
            with open('all_students.csv', 'w', encoding='utf-8') as f:
                f.write(''.join(students))
        else:
            print('Извините! Студент "{}" не был найден.'.format(student))
        ask_question()

    elif a == '9':
        g = pd.read_csv('all_students.csv', delimiter=',', encoding='utf-8')
        c = g.sort_values(['All students'], ascending=True)
        b = c.reset_index(drop=True)
        b.index += 1
        print(b)
        search = input('Введите фамилию и имя')
        a = b['All students'].isin([search])
        print(b[a])
        ask_question()

    elif a == '10':
        g = pd.read_csv('teachers.csv', delimiter=',', encoding='utf-8')
        c = g.sort_values(['Teacher'], ascending=True)
        b = c.reset_index(drop=True)
        b.index += 1
        print(b)
        search = input('Введите фамилию и имя')
        a = b['Teacher'].isin([search])
        print(b[a])
        ask_question()

    elif a == '11':
        print('Завершается программа')
        return

    else:
        print('Try again')
        director()


director()
