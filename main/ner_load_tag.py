from main.word2vec import Word2Features
from main.dictionary_load import DictionaryLoader
from main.processing_sentence import SentenceGetter
from underthesea import word_tokenize, pos_tag
from main.utils import tokenize
# from vncorenlp import VnCoreNLP
# annotator = VnCoreNLP(address="http://127.0.0.1", port=9000)


class Tagger:
    def __init__(self):
        self.w2 = Word2Features()
        self.tag = None
        self.path_to_model = 'main/model/crf.crfsuite'
        self.process_file = DictionaryLoader()

    # return list tuple include word and label.
    # mode 'text' is used to convert sentence to normal sentence,
    # where the words are the product to be capitalized.
    def combine_tag_with_word(self, tags, sent, mode=None):
        # words = [word.replace('_', ' ').strip().lower() for word in annotator.tokenize(sent)[0]]
        words = word_tokenize(sent)
        f_sent_dict = (list(zip(words, tags)))
        if mode is 'text':
            f_sent_text = ''
            for word in f_sent_dict:
                w = word[0].lower()
                t = word[1]
                if t is not 'O':
                    w = w.upper()
                f_sent_text += w + ' '
            return f_sent_text.rstrip(' ')
        return f_sent_dict

    def ner(self, text, mode=None):
        if self.tag is None:
            self.tag = self.process_file.read_bin(self.path_to_model)
        for i in range(0, 1):
            if i == 0:
                pos_sent = pos_tag(text)
            test_features = self.w2.sent2features(SentenceGetter.combine_word_with_pos(pos_sent))
            prediction = self.tag.predict([test_features])
            # if i == 0 and 'PRODUCT' not in prediction:
            #     pos_sent = [(word[0].replace('_', ' ').strip(), word[1]) for word in
                            # annotator.pos_tag(tokenize(text))[0]]

        return Tagger().combine_tag_with_word(prediction[0], text, mode)
# jdbc_connection_string => "jdbc:sqlserver://192.168.152.194:1433;databasename=development"


def ner_tag(sent, mode=None):
    tag = Tagger()
    return tag.ner(sent, mode)


def test():
    ner_tag = Tagger()
    sent = 'Kem đặc trị rạn cũ lâu năm và ngừa vết rạn mới giá 1750k tuýp này bạn ạ'
    # annotated_text = annotator.pos_tag(sent)
    # print(annotated_text)
    # print(pos_tag(sent))
    print(ner_tag.ner(sent, mode='text'))
    print(ner_tag.ner(sent))
    # print(chunk(sent))


if __name__ == '__main__':
    test()
