#Transposition Cipher Encryption

import pyperclip

def main():
    myMessage = 'Common sense is not so commen.'
    myKey = 8

    ciphertext = encryptMessage(myKey, myMessage)

    print(ciphertext + '|')

    pyperclip.copy(ciphertext)
    #把加密之后的文字复制到剪贴板

def encryptMessage(key, message):

    ciphertext = [''] * key
    #有多少列就创建多少个空字符串

    for col in range(key):
        #遍历原来的message变量，把每隔key个字符挑出来
        pointer = col

        while pointer < len(message):
            ciphertext[col] += message[pointer]

            pointer += key

    return ''.join(ciphertext)
#join（）方法接受一个字符串列表，并返回一个字符串。
#这个字符串包含了列表里的所有字符串，连接起来。
#调用join（）方法的字符串会放在列表里的字符串之间

if __name__ == '__main__':
    main()
'''
当一个Python程序运行时，在程序的第一行代码运行前，有一个特殊的变量叫做__name__会被赋值为字符串值'__main__'
而当一个Python程序被导入时，__name__变量会设为“.py”之前的文件名部分，然后运行这个程序
使用这个条件判断，就可以让程序既可以作为一个程序单独运行，也可以作为一个模块导入另一个程序
'''