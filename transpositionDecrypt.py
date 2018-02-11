#Transposition Cipher Decryption

import math, pyperclip

def main():
    myMessage = 'unrZk1_hxa!tz{v_fsPvt}'
    myKey = 2
    plaintext = decryptMessage(myKey, myMessage)

    print(plaintext + '|')

    pyperclip.copy(plaintext)

def decryptMessage(key, message):
    numOfColumns = math.ceil(len(message)/key)
    '''
    math.ceil()向上取整
    math.floor()向下取整
    round()四舍五入
    '''
    numOfRows = key
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    plaintext = [''] * numOfColumns

    col = 0
    row = 0

    for symbol in message:
        plaintext[col] += symbol
        col += 1

        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1

    return ''.join(plaintext)

if __name__ == '__main__':
    main()


