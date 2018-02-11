#Transposition Cipher Test

import random, sys, transpositionEncrypt, transpositionDecrypt

def main():

    random.seed(42)
    #伪随机数生成算法从一个叫做种子的初始数字开始
    #从一个种子产生的所有随机数字都是可预测的。
    #你可以通过调用random.seed()函数重设Python的随机种子

    #Python只有在random首次导入时才会产生‘不可预测’的随机数字，
    #因为这个种子被设为计算机的当前时钟的时间
    #（具体来说就是自1970年1月1日起的秒数）

    for i in range(20):
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)
        #random.randint()函数接受两个整数参数，返回那两个整数之间（包括那两个整数本身）的一个随机整数

        message = list(message)
        random.shuffle(message)
        #random.shuffle()函数接受一个列表参数，接着随机重新排列这个列表里的项。
        #shuffle()不返回列表值，就地修改列表值
        message = ''.join(message)

        print('Test #%s: "%s..."' %(i+1, message[:50]))

        for key in range(1, len(message)):
            encrypted = transpositionEncrypt.encryptMessage(key, message)
            decrypted = transpositionDecrypt.decryptMessage(key, encrypted)

            if message != decrypted:
                print('Mismatch with key %s and message %s.' %(key, message))
                print(decrypted)
                sys.exit()

    print('Transposition cipher test passed.')

if __name__ == '__main__':
    main()


