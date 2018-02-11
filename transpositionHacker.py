#Transposition Cipher Hacker

import pyperclip, detectEnglish, transpositionDecrypt

def main():
    # You might want to copy & paste this text from the source code at
    # http://invpy.com/transpositionHacker.py
    myMessage = """unrZk1_hxa!tz{v_fsPvt}"""
    hackedMessage = hackTransposition(myMessage)

    if hackedMessage == None:
        print('Failed to hack encryption.')
    else:
        print('Copying hacked message to clipboard:')
        print(hackedMessage)
        pyperclip.copy(hackedMessage)


def hackTransposition(message):
    print('Hacking...')

    # Python programs can be stopped at any time by pressing Ctrl-C (on
    # Windows) or Ctrl-D (on Mac and Linux)
    print('(Press Ctrl-C or Ctrl-D to quit at any time.)')

    # brute-force by looping through every possible key
    for key in range(1, len(message)):
        print('Trying key #%s...' % (key))

        decryptedText = transpositionDecrypt.decryptMessage(key, message)

        if detectEnglish.isEnglish(decryptedText):
            # Check with user to see if the decrypted key has been found.
            print()
            print('Possible encryption hack:')
            print('Key %s: %s' % (key, decryptedText[:100]))
            print()
            print('Enter D for done, or just press Enter to continue hacking:')
            response = input('> ')

            if response.strip().upper().startswith('D'):
                #strip()字符串方法返回字符串首尾空白去掉后的版本
                #也可以给strip()方法传递一个字符串参数，告诉它应该从字符串首尾去掉哪些字符而不是移除空白
                return decryptedText

    return None

if __name__ == '__main__':
    main()