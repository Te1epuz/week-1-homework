def get_summ(num_one, num_two):
    try:
        return int(num_one) + int(num_two)
    except ValueError:
        return 'Smth went wrong'

one = '2.5'
two = 3

print(get_summ(one,two))