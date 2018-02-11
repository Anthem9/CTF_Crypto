# Transposition Cipher Encrypt/Decrypt File

import time, os, sys, transpositionEncrypt, transpositionDecrypt

def main():
    inputFilename = 'frankenstein.encrypted.txt'

    outputFilename = 'frankenstein.decrypted.txt'
    myKey = 10
    myMode = 'decrypt'

    if not os.path.exists(inputFilename):
        #使用os.path.exists()函数，我们可以检查某个文件名是否已经存在
        print('The file %s does not exist.Quitting...' %(inputFilename))
        sys.exit()

    else:
        print('This will overwrite the file %s. (C)ontinus or (Q)uit?'  %(outputFilename))
        response = input('>')
        if not response.lower().startswith('c'):
            #如果字符串参数可以在这个字符串开头找到，startswith()方法会返回True
            #同理还有endswith()方法
            sys.exit()
        '''
        fileObj = open(inputFilename)
        content = fileObj.read()
        fileObj.close()
        '''
        with open(inputFilename) as fileObj:
            #open()函数返回“文件对象”数据类型的值
            content = fileObj.read()
            #read()方法将返回一个字符串，包含这个文件里的所有文字

        print('%sing...' % (myMode.title()))
        #title()方法使每个单词首字母大写

        startTime = time.time()
        #time.time()函数会返回一个浮点值，表示自1970年1月1日起的秒数。
        #这个时间点被称为Unix Epoch

        if myMode == 'encrypt':
            translated = transpositionEncrypt.encryptMessage(myKey, content)
        elif myMode == 'decrypt':
            translated = transpositionDecrypt.decryptMessage(myKey, content)

        totalTime = round(time.time() - startTime, 2)
        #计算程序进行了多长时间
        print('%sion time: %s seconds' % (myMode.title(), totalTime))

        with open(outputFilename, 'w') as outputFileObj:
            outputFileObj.write(translated)

        print("Done %sing %s (%s characters)." % (myMode, inputFilename, len(content)))
        print('%sed file is %s.' % (myMode.title(), outputFilename))

if __name__ == '__main__':
    main()


