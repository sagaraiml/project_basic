import random
print('guess the number game')
name = input('HI, plese give your name? > ')
SecretNumber = random.randint(1, 20)

for chance in range(1 ,7):
    number = input('guess the number between 1 and 20 > ')
    if int(number) > SecretNumber :
        print('number is too high')
    elif int(number) < SecretNumber :
        print('number is too low')
    else :
        break

if chance == 6 :
    print('exceeded 6 chances')
else :
    print(name + ' you guessed the right number :' + str(SecretNumber) + ' in ' + str(chance)+ ' chances')
