import json

def new_user():
    login = str(input("Enter your login: "))
    password = str(input("Enter your password: "))

    with open('auth.json', 'r') as loadout:
        current_list = json.load(loadout)

    if not login in current_list:
        current_list[login] = password
        with open('auth.json', 'w') as upload:
            json.dump(current_list, upload)
        print('Вы успешно зарегистрированы!')
    else: print('Пользователь с таким логином уже имеется!')

def sign_in():
    with open('auth.json', 'r') as current_list:
        current_passdata = json.load(current_list)
    tryouts = 0
    for i in range(3):
        login_check = str(input("Login: "))
        password_check = str(input("Password: "))
        if login_check in current_passdata and current_passdata[login_check] == password_check:
            print('Вы вошли в систему!')
            break
        elif tryouts == 2:
            print('Вы исчерпали попытки входа!')
            break
        else:
            print('Неправильно введён логин или пароль! Попробуйте снова')
            tryouts += 1

choice = input('Вы хотите зайти или зарегистрироваться?')

if choice == 'зайти':
    sign_in()

if choice == 'зарегистрироваться':
    new_user()