respond = { "как дела?" : "Хорошо!",
            "что делаешь?" : "Программирую",
            "когда?" : "Сегодня"}

while True:
    
    try:
        ask_user = input('Как дела? ')
    except KeyboardInterrupt:
        print()
        print('Пока!') #можно написать \n для новой строки
        break
    
    if ask_user == 'хорошо':
        break
    if respond.get(ask_user) != None:
        print(respond[ask_user])