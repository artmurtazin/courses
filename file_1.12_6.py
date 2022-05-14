while True:
    n = int(input())
    n_char = str(n)

    if n == 1:
        print(n, 'программист')
        break

    if n < 10 and (n_char[-1] == '2' or n_char[-1] == '3' or n_char[-1] == '4'):
        print(n, 'программиста')
        break

    if n_char[-1] == '0' or n_char[-1] == '5' or n_char[-1] == '6' or n_char[-1] == '7' or n_char[-1] == '8' or n_char[-1] == '9'\
            or n_char[-2] == '1':
        print(n, 'программистов')
        break

    if n_char[-2] != '1' and n_char[-1] == '1':
        print(n, 'программист')
        break

    if n_char[-2] != '1' and (n_char[-1] == '2' or n_char[-1] == '3' or n_char[-1] == '4'):
        print(n, 'программиста')
        break