SYMBOLS = 'AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŹŻaąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż0123456789,.?!@#$%^&*()_-+=\|{}[];:"/'
MAX_KEY_LENGTH = len(SYMBOLS)


def powitanie():
    print("Witam w programie Szyfru Cezara. Jest to prosty szyfr dzięki któremu możesz zaszyfrować, odszyfrować lub użyć metody siłowej. \nUżywa on 106 znakowego szyfrowania obejmującego znaki polskie, cyfry oraz znaki specjalne")


def pobierz_tryb():
    print("Co chcesz zrobić: zakodować, odkodować, brute (z, o, b): ")
    mode = input().lower()
    while mode not in ["z", "o", "b", "zakodować", "odkodować", "brute"]:
        print("Możesz tylko wybrać te opcje: (z, o, b) or (zakodować, odkodować, brute).")
        print("Wybierz ponownie: ")
        mode = input().lower()
    return mode


def pobierz_klucz():
    key = int(input(f'Wybierz klucz szyfrowania od 1 do {MAX_KEY_LENGTH}: '))
    while key < 0 or key > MAX_KEY_LENGTH:
        print(f"Możesz wybrać tylko liczbe od 1 do {MAX_KEY_LENGTH}.")
        key = int(input(f'Możesz wybrać tylko liczbe od 1 do {MAX_KEY_LENGTH}. Wybierz ponownie: '))
    return key


def pobierz_wiadomosc():
    message = input('Wpisz wiadomość do zakodowania lub odkodowania: ')
    return message


def przetworz(klucz, tryb, wiadomosc):
    if tryb[0] == "o":
        klucz = -klucz
    translation = ""

    for symbol in wiadomosc:
        symbolIndex = SYMBOLS.find(symbol)

        if symbolIndex == -1:
            translation += symbol
        else:
            symbolIndex += klucz

            if symbolIndex >= MAX_KEY_LENGTH:
                symbolIndex -= MAX_KEY_LENGTH
            elif symbolIndex < 0:
                symbolIndex += MAX_KEY_LENGTH

            translation += SYMBOLS[symbolIndex]

    return translation


powitanie()
tryb = pobierz_tryb()
wiadomosc = pobierz_wiadomosc()
if tryb[0] != "b":
    klucz = pobierz_klucz()
    print(przetworz(klucz, tryb, wiadomosc))
else:
    for klucz in range(MAX_KEY_LENGTH + 1):
        print(klucz, przetworz(klucz, "odkodować", wiadomosc))
