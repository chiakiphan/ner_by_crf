class Word2Features:

    def __init__(self):
        self.vie_dic = []
        self.stop_word = []
        self.link_vie = '/home/citigo/Documents/ner_tagging/data/vietnamese-wordlist/Viet74K.txt'
        self.link_stop = '/home/citigo/Documents/ner_tagging/data/stop_word.txt'

    def load_dictionary(self, link, mode=None):
        dic = []
        with open(link, encoding='utf8') as fr:
            for line in fr:
                if len(line.split(' ')) < 4:
                    dic.append(line.strip('\n'))
        if mode == 'stopword':
            self.stop_word = dic
        self.vie_dic = dic

    def is_vie_word(self, word):
        if len(self.vie_dic) == 0:
            self.load_dictionary(self.link_vie)
        word = word.lower()
        if word in self.vie_dic:
            return True
        return False

    def is_stop_word(self, word):
        if len(self.stop_word) == 0:
            self.load_dictionary(self.link_stop, mode='stopword')
        word = word.lower()
        if word in self.stop_word:
            return True
        return False

    def number_syllable(self, word):
        return len(word.split(' '))

    def has_number(self, word):
        for char in list(word):
            if char.isdigit():
                return True
        return False

    def word2features(self, sent, indx):
        word = sent[indx][0]
        postag = sent[indx][1]
        word = word.replace('_', ' ').strip()

        features = {
            'bias': 1.0,
            'word.lower': word.lower(),
            'word.isalpha': word.isalpha(),
            'word.isdigit': word.isdigit(),
            'word.has_number': self.has_number(word),
            # 'word.number_syllable': self.number_syllable(word),
            'word.is_vie_word': self.is_vie_word(word),
            # 'word.is_stop_word': self.is_stop_word(word),
            'word.istitle': word.istitle(),
            # 'word.isupper': word.isupper(),
            'pos tag': postag
        }
        if indx > 0:
            word1 = sent[indx - 1][0]
            word2 = word1 + ' ' + word
            postag1 = sent[indx - 1][1]
            features.update({
                '-1:word.lower': word1.lower(),
                # '-1:word2.lower': word2.lower(),
                '-1:word.isalpha': word1.isalpha(),
                '-1:word.isdigit': word1.isdigit(),
                '-1:word.has_number': self.has_number(word1),
                # '-1:word.number_syllable': self.number_syllable(word1),
                '-1:word.is_vie_word': self.is_vie_word(word1),
                # '-1:word.is_stop_word': self.is_stop_word(word1),
                '-1:word.istitle': word1.istitle(),
                # '-1:word.isupper': word1.isupper(),
                '-1:pos tag': postag1
            })
        else:
            features['BOS'] = True

        if indx < len(sent) - 1:
            word1 = sent[indx + 1][0]
            word2 = word + ' ' + word1
            postag1 = sent[indx + 1][1]
            features.update({
                '+1:word.lower': word1.lower(),
                # '+1:word2.lower': word2.lower(),
                '+1:word.isalpha': word1.isalpha(),
                '+1:word.isdigit': word1.isdigit(),
                '+1:word.has_number': self.has_number(word1),
                # '+1:word.number_syllable': self.number_syllable(word1),
                '+1:word.is_vie_word': self.is_vie_word(word1),
                # '+1:word.is_stop_word': self.is_stop_word(word1),
                '+1:word.istitle': word1.istitle(),
                # '+1:word.isupper': word1.isupper(),
                '+1:pos tag': postag1
            })
        else:
            features['EOS'] = True
        return features

    def sent2features(self, sent):
        return [self.word2features(sent, i) for i in range(len(sent))]

    def sent2labels(self, sent):
        return [label for token, postag, label in sent]