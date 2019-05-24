respond = { "как дела?" : "Хорошо!",
            "что делаешь?" : "Программирую",
            "когда?" : "Сегодня"}

while True:
    ask_user = input('Как дела? ')
    if ask_user == 'хорошо':
        break
    if respond.get(ask_user) != None:
        print(respond[ask_user])