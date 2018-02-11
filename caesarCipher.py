#Caesar Cipher

import pyperclip

#message = "This is my secret message."
message = "You are just too good to be true"
key = 13

mode = 'encrypt'

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#这组数据叫做加密程序的符号集
#这个变量名是全大写的，这是常量的编程约定

translated = ''

message = message.upper()

for symbol in message:
    if symbol in LETTERS:
        num = LETTERS.find(symbol)
        #.find()方法接受一个字符串参数，返回一个整数索引，表示那个字符串在方法的字符串里出现的位置
        #如果找不到这个字符串参数，find()方法会返回整数-1
        #你传给find()作为参数的字符串可以超过一个字符，find()返回的整数将会是这个参数所在的位置第一个字符的索引。
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)

        translated = translated + LETTERS[num]

    else:
        translated = translated + symbol

print(translated)

pyperclip.copy(translated)