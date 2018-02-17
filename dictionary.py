import MeCab


class Dictionary(object):
    def __init__(self, source_file):
        self._dict = {}
        self.line_list = []
        self._num_prefix = 2
        self.create_markov_dict(source_file)

    def tokenize_text(self, text):
        tagger = MeCab.Tagger('-Owakati')
        result = tagger.parse(text)
        result = result.split()
        return result  # result is list

    def create_line_list(self, source_file):
        line_list = []
        with open(source_file, 'r') as f:
            lines = f.readlines()
        for line in lines:
            line = line.replace('\n', '')
            line = line.split('。')
            for i, sentence in enumerate(line):
                tokenized_text_list = self.tokenize_text(sentence)
                if not i == len(line) - 1:
                    tokenized_text_list.append('。')
                if not tokenized_text_list == []:  # Except blank line
                    line_list.append(tokenized_text_list)
        self.line_list = line_list
        return line_list

    def create_markov_dict(self, file_path):
        # dictionary format : {'prefix', 'suffix'}
        line_list = self.create_line_list(file_path)
        markov_dict = {}
        for line in line_list:
            for i, word in enumerate(line):
                if i + self._num_prefix < len(line):
                    prefix = ''
                    for j in range(self._num_prefix):
                        prefix += line[i+j]
                    suffix = line[i+self._num_prefix]
                    markov_dict.setdefault(prefix, []).append(suffix)
        self._dict = markov_dict

    @property
    def dict(self):
        return self._dict
