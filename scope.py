#1.在所有函数以外的变量总是全局变量。
#2.如果函数里的变量从未在赋值语句里使用，那么它是全局变量。
#3.如果函数里的变量未在global语句里使用，但在赋值语句里使用，那么它是本地变量。
#4.如果函数里的变量在global语句里使用，那么当它在那个函数里使用时，它是全局变量。

spam = 42

def eggs():
    spam = 99
    print('In eggs():',spam)

def ham():
    print('In ham():',spam)

def bacon():
    global spam
    print('In bacon():',spam)
    spam = 0

def CRASH():
    print(spam)
    spam = 0

print(spam)
eggs()
print(spam)
ham()
print(spam)
bacon()
print(spam)
CRASH()