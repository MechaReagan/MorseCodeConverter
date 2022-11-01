MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ',':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


translate = True
while translate:
    entry = input("What would you like to translate into morse code?\n")
    entry = entry.upper()

    translated = ""
    for letter in entry:
        if letter in MORSE_CODE_DICT:
            converted = MORSE_CODE_DICT[letter]
            translated += converted
            translated += " "
        elif letter == " ":
            translated += "/ "

    print(f"Your translated phrase is as follows: \n{translated}\n")
    while True:
        go_again = input("Would you like to convert another phrase? (Y/N)\n")
        if go_again.lower() == "y":
            break
        elif go_again.lower() == "n":
            translate = False
            break
        else:
            print("I didn't recognize that.\n\n")