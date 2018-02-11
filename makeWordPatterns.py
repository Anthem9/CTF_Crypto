# Makes the wordPatterns.py File
# http://inventwithpython.com/hacking (BSD Licensed)

# Creates wordPatterns.py based on the words in our dictionary
# text file, dictionary.txt. (Download this file from
# http://invpy.com/dictionary.txt)

import pprint
#pprint模块包含美化输出（pretty print）值的函数它们对于在屏幕上输出字典和列表值很有用。
#pprint模块有一个函数叫pprint()。传出pprint.pprint()的值会“美化输出”到屏幕上。
#如果希望把这种“经过美化的”文字保存成字符串而不是显示在屏幕上，你可以用pprint.pformat()

def getWordPattern(word):
    # Returns a string of the pattern form of the given word.
    # e.g. '0.1.2.3.4.1.2.3.5.6' for 'DUSTBUSTER'
    word = word.upper()
    nextNum = 0
    #单词模型的数字
    letterNums = {}
    #保存一个字典，它的键是单个字母的字符串，它的值是那个字母的整数数字。随着我们在单词里找到新单词，这个字母和它的数字会保存在letterNums里。
    wordPattern = []

    for letter in word:
        if letter not in letterNums:
            letterNums[letter] = str(nextNum)
            nextNum += 1
        wordPattern.append(letterNums[letter])
        #使用列表-追加-连接流程来创建字符串
    return '.'.join(wordPattern)
#在'.'上调用join()方法会得到'0.1.2.2.3.3.4'


def main():
    allPatterns = {}
    '''
    fo = open('dictionary.txt')
    wordList = fo.read().split('\n')
    fo.close()
    '''
    with open('dictionary.txt') as fo:
        wordList = fo.read().split('\n')

    for word in wordList:
        # Get the pattern for each string in wordList.
        pattern = getWordPattern(word)

        if pattern not in allPatterns:
            allPatterns[pattern] = [word]
        else:
            allPatterns[pattern].append(word)

    # This is code that writes code. The wordPatterns.py file contains
    # one very, very large assignment statement.
    '''
    fo = open('wordPatterns.py', 'w')
    fo.write('allPatterns = ')
    fo.write(pprint.pformat(allPatterns))
    fo.close()
    '''
    with open('wordPatterns.py', 'w') as fo:
        fo.write('allPatterns = ')
        fo.write(pprint.pformat(allPatterns))

if __name__ == '__main__':
    main()