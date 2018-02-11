# Simple Substitution Cipher Hacker
#破译简单替代加密法的步骤：
#找出密文里的每个密词的单词模式
#找出每个密词可以解密成哪些英文单词
#使用密词的候选单词列表为每个密词创建一个密字映射。（密字映射只是一个字典值）
#计算所有密字映射的交集，得到一个交集密字映射。
#从交集密字映射移除任何已经破译的字母

#密文里的密词越多，我们可以用来计算交集的密字映射就越多。我们计算交集的密字映射越多，每个密字的潜在解密字母的数目越少。
#这意味着密文消息越长，我们就越可能破译和解密它。


import os, re, copy, pprint, pyperclip, simpleSubCipher, makeWordPatterns
#re模块是正则表达式模块

if not os.path.exists('wordPatterns.py'):
    makeWordPatterns.main() # create the wordPatterns.py file
import wordPatterns

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nonLettersOrSpacePattern = re.compile('[^A-Z\s]')
#使用正则表达式从字符串移除不是大写字母或空格的字符。

def main():
    message = 'Sy l nlx sr pyyacao l ylwj eiswi upar lulsxrj isr sxrjsxwjr, ia esmm rwctjsxsza sj wmpramh, lxo txmarr jia aqsoaxwa sr pqaceiamnsxu, ia esmm caytra jp famsaqa sj. Sy, px jia pjiac ilxo, ia sr pyyacao rpnajisxu eiswi lyypcor l calrpx ypc lwjsxu sx lwwpcolxwa jp isr sxrjsxwjr, ia esmm lwwabj sj aqax px jia rmsuijarj aqsoaxwa. Jia pcsusx py nhjir sr agbmlsxao sx jisr elh. -Facjclxo Ctrramm'

    print('Hacking...')
    letterMapping = hackSimpleSub(message)
    #得到用来解密的密字映射

    # 向用户展示结果
    print('Mapping:')
    pprint.pprint(letterMapping)
    print()
    print('Original ciphertext:')
    print(message)
    print()
    print('Copying hacked message to clipboard:')
    hackedMessage = decryptWithCipherletterMapping(message, letterMapping)
    pyperclip.copy(hackedMessage)
    print(hackedMessage)


def getBlankCipherletterMapping():
    # 创建空密字映射的函数
    return {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': [], 'I': [], 'J': [], 'K': [], 'L': [], 'M': [], 'N': [], 'O': [], 'P': [], 'Q': [], 'R': [], 'S': [], 'T': [], 'U': [], 'V': [], 'W': [], 'X': [], 'Y': [], 'Z': []}


def addLettersToMapping(letterMapping, cipherword, candidate):
    #这个函数检查candidate里的每个字母，如果letterMapping里没有的话，并把cipherword里的对应字母添加到letterMapping

    letterMapping = copy.deepcopy(letterMapping)
    #为了防止修改传给letterMapping参数原来的字典值，要复制letterMapping里的字典
    #并让这个副本成为letterMapping的新值。
    #因为传递过来的letterMapping是字典引用值的副本，而不是字典值的副本
    for i in range(len(cipherword)):
        if candidate[i] not in letterMapping[cipherword[i]]:
            letterMapping[cipherword[i]].append(candidate[i])
    return letterMapping


def intersectMappings(mapA, mapB):
    #计算两个密字映射的交集
    intersectedMapping = getBlankCipherletterMapping()
    for letter in LETTERS:

        # 一个空字典意味着密字可能解密成任何字母，所以直接复制另一个字典
        if mapA[letter] == []:
            intersectedMapping[letter] = copy.deepcopy(mapB[letter])
        elif mapB[letter] == []:
            intersectedMapping[letter] = copy.deepcopy(mapA[letter])
        else:
            # 如果一个字母既在映射A又在映射B，就把它添加到交集中
            for mappedLetter in mapA[letter]:
                if mappedLetter in mapB[letter]:
                    intersectedMapping[letter].append(mappedLetter)

    return intersectedMapping


def removeSolvedLettersFromMapping(letterMapping):
    # 查找letterMapping中已经被解密的密字。并把它从字母表中移除
    #这样能产生新的被解密的密字
    letterMapping = copy.deepcopy(letterMapping)
    #复制letterMapping里的密字映射，这样在函数里对它做的修改就不会影响到函数之外的字典值了
    loopAgain = True
    while loopAgain:
        # 先假设不会进行循环
        loopAgain = False

        # 创建一个列表储存已被解密的密字
        solvedLetters = []
        for cipherletter in LETTERS:
            if len(letterMapping[cipherletter]) == 1:
                solvedLetters.append(letterMapping[cipherletter][0])

        # 如果一个密字被解密了，它就不可能是其他字母对应的值了，所以我们要把它从其他字母对应的可能性中移除掉
        for cipherletter in LETTERS:
            for s in solvedLetters:
                if len(letterMapping[cipherletter]) != 1 and s in letterMapping[cipherletter]:
                    letterMapping[cipherletter].remove(s)
                    if len(letterMapping[cipherletter]) == 1:
                        # 如果移除已解密密字的过程中有新的字母被解密就进行循环
                        loopAgain = True
    return letterMapping


def hackSimpleSub(message):
    intersectedMap = getBlankCipherletterMapping()
    cipherwordList = nonLettersOrSpacePattern.sub('', message.upper()).split()
    #sub()正则方法会用第一个参数替换第二个参数里任何匹配这个字符串模式的地方
    #cipherwordList中储存了message里每个单词的大写形式
    for cipherword in cipherwordList:
        # 给每一个密字建立一个密字映射
        newMap = getBlankCipherletterMapping()

        wordPattern = makeWordPatterns.getWordPattern(cipherword)
        if wordPattern not in wordPatterns.allPatterns:
            continue # 如果单词不在我们的字典里就跳过

        # 用候选词里的字母更新newMap里的密字映射
        for candidate in wordPatterns.allPatterns[wordPattern]:
            newMap = addLettersToMapping(newMap, cipherword, candidate)

        # 将新的密字映射与旧的交集取交集
        intersectedMap = intersectMappings(intersectedMap, newMap)

    # 从其他列表中移除已经被解密的字母
    return removeSolvedLettersFromMapping(intersectedMap)


def decryptWithCipherletterMapping(ciphertext, letterMapping):
    # 返回一个字符串作为密钥，里面包括已经被解密的密字，未解密的密字用下划线替代

    # First create a simple sub key from the letterMapping mapping.
    key = ['x'] * len(LETTERS)
    for cipherletter in LETTERS:
        if len(letterMapping[cipherletter]) == 1:
            # If there's only one letter, add it to the key.
            keyIndex = LETTERS.find(letterMapping[cipherletter][0])
            key[keyIndex] = cipherletter
        else:
            ciphertext = ciphertext.replace(cipherletter.lower(), '_')
            ciphertext = ciphertext.replace(cipherletter.upper(), '_')
    key = ''.join(key)

    # With the key we've created, decrypt the ciphertext.
    return simpleSubCipher.decryptMessage(key, ciphertext)


if __name__ == '__main__':
    main()