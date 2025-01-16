password = input("Введите пароль (больше 8 символов, включает и прописные и заглавные буквы):")
accepted = True
while not password.isalpha() or len(password) < 8 or password.islower() or password.isnumeric():
    print("Недопустимый пароль. Пароль должен содержать только заглавные и прописные буквы и содержать более 8 символов")
    accepted = False
    break
if accepted:
    print("Успех")
