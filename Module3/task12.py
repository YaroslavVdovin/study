import json

login_check = str(input("Login: "))
password_check = str(input("Password: "))

with open('auth.json', 'r') as current_list:
    current_passdata = json.load(current_list)
if login_check in current_passdata and current_passdata[login_check] == password_check:
    print('cool')