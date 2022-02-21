
print('Welcome to the IT-school "U"!')
def account():
    acc = input('To run the program, please enter the account type'
                ' and your keyword: >>> Student,Teacher,Director\n').lower().strip()

    if acc == 'student':
        word = input('Enter the keyword: >>>')
        if word == 'study':
            import student
            return

    elif acc == 'teacher':
        word = input('Enter the keyword: >>>')
        if word == 'teaching':
            import teacher
            return

    elif acc == 'director':
        word = input('Enter the keyword: >>>')
        if word == 'admin':
            import director
            return

    else:
        print('This account type does not exist. Try again.')
        account()


account()
