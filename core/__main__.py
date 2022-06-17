from .task import SentenceEditor

sentence_editor = SentenceEditor()

test = input("Enter the sentence: ")
length = input("Enter word lenght: ")

if __name__ == "__main__":
    print(sentence_editor.add_sentence(test))
    print(sentence_editor)
