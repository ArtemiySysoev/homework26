def kvadrat_chisla(x):
    return x**2

my_numbers = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

kvadraty = map(kvadrat_chisla, my_numbers)

def nechetnye_chisla(y):
    return y % 2

result = filter(nechetnye_chisla, kvadraty)
print(list(result))