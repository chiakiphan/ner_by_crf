import io
import pandas as pd
import pickle


class DictionaryLoader:
    def __init__(self, data_path=None):
        self.words_data = None
        self.data_path = data_path

    def read_txt(self):
        with io.open(self.data_path, "r", encoding="utf-8") as f:
            text = f.read()
        return text

    def read_bin(self, path):
        with open(path, 'rb') as fr:
            model = pickle.load(fr)
        return model

    def read_csv(self, path):
        data = pd.read_csv(path, encoding='utf8', error_bad_lines=False, header=None,
                           names=["Word", "POS", "Tag", "Sentence"],
                           sep='\t')
        data = data.fillna(method="ffill")
        return data

    def save_model(self, path, model):
        with open(path, 'wb+') as fw:
            pickle.dump(model, fw)

    @property
    def words(self):
        if not self.words_data:
            content = DictionaryLoader.read_txt(self)
            words = content.split("\n")
            self.words_data = words
        return self.words_data
