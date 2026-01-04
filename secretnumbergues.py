import random

secret_number = random.randint(1,10)

print("privit! Ya zagadav chislo viiiiiiiiiiiiiiid 1 doooooooooooooo 10.")
print("Sprobouy vidgadatu yuogo!")

attemps = 0
guess = None

while guess != secret_number:
    guess = int(input("Vvvvvvvvedu sviu variantiche: "))
    attemps += 1

    if guess < secret_number:
        print("Zagadane chislo nuzge tvoigo hahaha🤣🤣🤣")
    elif guess > secret_number:
        print("Zagadane chislo meshe tvoigo blin!😭😭😭")
    else:
        print(f"WHAT YOU VGADAV CHISLO⚧️ '{secret_number}'")

while True:
    play_again = input("Chotesh znovu pograty? (tak/ni): ").lower()
    if play_again == "tak":
        secret_number = random.randint(1,10)
        attemps = 0
        guess = None
        print("Novoe chislo zagadano! Viddadys vid 1 do 10.")
        while guess != secret_number:
            guess = int(input("Vvvvvvvvedu sviu variantiche: "))
            attemps += 1

            if guess < secret_number:
                print("Zagadane chislo nuzge tvoigo hahaha")
            elif guess > secret_number:
                print("Zagadane chislo meshe tvoigo blin!")
            else:
                print(f"WHAT YOU VGADAV CHISLO '{secret_number}'")
        print("Vse idu gylaui")
    elif play_again == "ni":
        print("Dyakuyu za hru! Buv rad pobachyty vas znovu!")
        break
    else:
        print("Bud laska, vidpovidte 'tak' abo 'ni'.")