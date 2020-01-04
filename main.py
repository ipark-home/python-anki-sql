import numpy as np


def writeComments(idText):
    from sqliteWord import sqliteWord
    sqlWord = sqliteWord()

    if idText is None:
        text = 'AnkiEnglishDict4000words'
        idtext = sqlWord.appendText(text)

    typeword = 1
    sqlWord.writeComments(idText)


def appendWordComment():
    from readAnkiExportFile import readAnkiExportFile
    ankiExp = readAnkiExportFile('ankiExport.txt')
    ankiExp.readFile()
    # ankiExp.getWords()
    from sqliteWord import sqliteWord
    sqlWord = sqliteWord()
    idtext = 2  # sqlWord.appendText(text)
    typeword = 1
    for word in ankiExp.getWords():
        sqlWord.appendLinkIdTextWord(idtext, word, typeword)
        # print('save...'+word)
        # sqlWord.appendWordComment(word,comment)
    for comment in ankiExp.getComments():
        # sqlWord.appendLinkIdTextWord(idtext, word, typeword)
        for comm in comment:
            print('getComments() ... ' + comm)
        sqlWord.appendWordComment(comment[0], comment[1])

    # sqlWord.writeComments()


def mainOld():
    from readAnkiExportFile import readAnkiExportFile

    ankiExp = readAnkiExportFile('ankiExport.txt')
    ankiExp.readFile()
    # ankiExp.getWords()

    from sqliteWord import sqliteWord

    sqlWord = sqliteWord()
    text = 'AnkiEnglishDict4000words'
    idtext = sqlWord.appendText(text)
    typeword = 1
    # for word in ankiExp.getWords():
    # sqlWord.appendLinkIdTextWord(idtext, word, typeword)
    # print('save...'+word)
    # sqlWord.appendWordComment(word,comment)
    # for comment in ankiExp.getComments():
    # sqlWord.appendLinkIdTextWord(idtext, word, typeword)
    # for comm in comment:
    #     print('getComments() ... ' + comm)
    # sqlWord.appendWordComment(comment[0], comment[1])

    sqlWord.writeComments()


def readAWSlist():
    print('readAWSlist()')
    lines = []
    with open('awsList.txt', 'rb') as fh:
        while True:
            line = fh.readline().decode("UTF-8")
            # print(line)
            if not line:
                break  # you may also want to remove whitespace characters like `\n` at the end of each line
            lineRepl = line.replace('\n', '')
            if lineRepl != '':
                lines.append(lineRepl)
    print(lines)
    with open('awsListNew.txt', 'w', encoding="utf-8") as fh:
        i = 1
        for item in lines:
            if i == 1:
                lineNew = item
                i = i+1
            else:
                lineNew = lineNew+'\t'+item
                print(lineNew)
                fh.write(lineNew+'\n')
                i = 1


def test():
    a = [1, 2, 3, 45, 6, 76, 89, 7, 6, 5, 4, 3, 2, 1]
    np_a = np.array(a)
    for x, y in enumerate(a):
        print(x)
    # b = [x for x in a if x % 2]
    # c = [x for x in a if not x % 2]

    # print(b)
    # print(c)


def main():
    # appendWordComment()
    # writeComments(2)
    # readAWSlist()
    test()


if __name__ == "__main__":
    main()
