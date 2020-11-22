n = 0
a = "abrete sesamo"
print('Cual es tu nombre?')
nom = input ()
while n < 10:
    print('\nCual es la palabra Magica?:')
    x = input()
    if x==a:
        print( '\n' + nom + ' ,la puerta se abre ')
        exit ()
    else:
        print(' \nIncorrecto ' + nom )
        n = n + 1
exit ()
