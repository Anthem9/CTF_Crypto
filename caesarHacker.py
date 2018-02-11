#Caecsar Cipher Hacker

message = 'FDXDGDADDG_FXXFAAXFAG_GDFXFFXFFXADXFDA_GDAD'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


for key in range(len(LETTERS)):
    #range（）也是从0开始，这里是0-25
    translated = ''
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num - key

            if num < 0:
                num = num + len(LETTERS)

            translated = translated + LETTERS[num]

        else:
            translated = translated + symbol

    print('Key #%s: %s' % (key,translated))