
class readAnkiExportFile():
    def __init__(self, nameFile):
        self.nameFile = nameFile
        self.countWords = 0
        self.words = []
        self.comments = []

    def split_line(self, text):
        # eng = []
        words = text.split('\t')
        sub = words[1][words[1].index("\"\"")+2:]
        words[1] = sub[0:sub.index("\"\"")]
        # eng.append(words[0])
        # lin=''.join(e+'\t' for e in words[1:])
        # for word in words:
        #     print(word)

        # for word in words:
        #     for ch in ['�', '�', '.', ',', '?', '"', '*', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '[', ']', '-', ':', '!', '(', ')', ';']:
        #         if ch in word:
        #             word = word.replace(ch, '')
        #     for wr in ['I']:
        #         if not wr in word:
        #             word = word.lower()
        #     word = word.strip(' \t\n\r')
        #     if (len(word) > 1 and len(word) < 32) or 'I' in word:
        #         #  self.countWords += 1
        #         self.words.append(word)
        #         # linkTextWordAppend('The_Old_Man_and_the_Sea', word, 1)
        #         # wordAppend(word, 2)
        return words

    def getWords(self):
        if self.words is None:
            readFile()
        return self.words

    def getComments(self):
        if not self.comments is None:
            return self.comments

    def getWordsPrint(self):
        getWords(self)
        for word in self.words:
            print(word)
        return self.words

    def readFile(self):
        with open(self.nameFile, 'rb') as fh:
            while True:
                line = fh.readline().decode("UTF-8")
                # print(line)
                if not line:
                    break
                # engs=self.split_line(line)
                # eng=''.join(e+'\t' for e in engs[1:])
                # self.comments.append(eng)
                words = self.split_line(line)
                self.comments.append([words[0],
                                      ''.join(e+'\t' for e in words[1:])])
            # for comment in self.comments:
            #     print(comment)

    def __del__(self):
        pass
