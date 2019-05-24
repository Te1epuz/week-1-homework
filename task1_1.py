age_inp = input('Введите ваш возраст: ')
age_inp = int(age_inp)

def age_check(age):
    if age < 6:
        return 'В детсад'
    elif age < 18:
        return 'В школу'
    elif age < 24:
        return 'В универ'
    else:
        return 'Работать'

age_check_result = age_check(age_inp)

print(age_check_result)