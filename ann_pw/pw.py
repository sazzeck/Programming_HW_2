import re
import typing as t


class SentenceManipulator:
    def __init__(self):
        self.__first_sentence: t.List = []
        self.__second_sentence: t.List = []
        self.__words_numbering: t.Dict = {}
        self.__words_length: t.Dict = {}

    @property
    def words_list(self) -> t.List:
        return self.__first_sentence

    @property
    def word_numbering(self) -> t.Dict:
        words = self.__words_numbering
        for i, item in enumerate(self.__first_sentence):
            words[i + 1] = item
        return words

    @property
    def word_length(self) -> t.Dict:
        words = self.__words_length
        for word in self.__first_sentence:
            words[word] = len(word)
        return words

    def add_sentence(self, sentence: str) -> t.List:
        punctuation_cleaning = re.sub(r"\W", " ", sentence).split()
        self.__first_sentence.extend(punctuation_cleaning)

    def search_words(self, word_number: str) -> str:
        words_numbering = self.__words_numbering
        for key, value in words_numbering.items():
            if int(word_number) == key:
                return value
    # реализовать not found

    def search_words_length(self, word_length: str) -> t.List:
        words = self.__words_length
        desired_words = []
        for key, value in words.items():
            if value > int(word_length):
                desired_words.append(key)
        return desired_words
    # реализовать not found
