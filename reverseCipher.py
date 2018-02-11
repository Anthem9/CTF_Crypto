#Reverse Cipher

message = 'Three can keep a secret, if two of them are dead.'
translated = ''
#在程序里，一个常见的做法是用空字符串作为一个变量的初始值，然后把字符和它连接，知道它‘增长’成最终希望得到的字符串

i = len(message) - 1
while i >= 0:
    translated = translated + message[i]
    i = i - 1

print(translated)