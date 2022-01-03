import random
import sys
upper = 1000

print(f'Hallo ich bin Fred und habe mir eine Zahl zwischen 1 und {upper} gemerkt.\nDu musst diese raten. Aber lass uns um Geld spielen, das ist viel cooler, \n\n')
number = random.randint(1, 1000)
print(number)
for trial in range(1, 11):
    guess_str = input(f'Dein {trial}. Versuch: ')
    if not guess_str.isnumeric():
        print('Du Trottel. Du muss eine Zahl eingeben. Nächster Versuch')
        continue
    guess = int(guess_str)
    if guess > number:
        print('Deine Zahl ist zu groß')
    elif guess < number:
        print('Deine Zahl ist zu klein')
    else:
        print(f'Bingo. Du hast die Zahl in {trial} Versuchen erraten. Klicke auf den Link um dein PreisGeld abzuheben')
        break
else:
    print(f'Leider verloren. Die korrekte Zahl war {number}. Du schuldest mir nun 25 Euro. Bitte überweise sie an die Sparkasse Lübeck')
    sys.exit(1)




