from .pw import SentenceManipulator

manipulator = SentenceManipulator()

test = input("Enter the sentence: ")
length = input("Enter word lenght: ")

manipulator.add_sentence(test)

if __name__ == "__main__":
    print(manipulator.word_length)
    print(manipulator.search_words_length(length))
