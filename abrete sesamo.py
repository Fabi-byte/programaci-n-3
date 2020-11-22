n = 0
a = "abrete sesamo"
while n < 10:
    print('\nCual es la palabra Magica?:')
    x = input()
    if x==a:
        print('\nLa puerta se abre')
        exit ()
    else:
        print('Incorrecto')
        n = n + 1
exit ()
