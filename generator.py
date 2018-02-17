from dictionary import Dictionary

import random


class Generator(object):
    def __init__(self, source_file):
        self._dictionary = Dictionary(source_file)

    def generate_text(self, max_words):
        count = 0
        while count < max_words:
            if count == 0:
                # The beginning of a sentence
                sentence = random.choice(self._dictionary.line_list)
                key = sentence[0] + sentence[1]
                text = key
                post_word = sentence[1]
            else:
                word = random.choice(self._dictionary.dict[key])
                text += word
                # Update the key
                pre_word = post_word
                post_word = word
                key = pre_word + post_word
                # '。' is the end of the sentence
                if post_word == '。':
                    break
            count += 1
            if count == max_words:
                text += '。'
        return text


if __name__ == '__main__':
    generator = Generator('source.txt')
    text = generator.generate_text(50)
    print('text :', text)
