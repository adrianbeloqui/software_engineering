class StringBuilder:
    def __init__(self) -> None:
        self.words = []
        pass

    def append(self, word: str) -> None:
        self.words.append(word)

    def __str__(self) -> str:
        return ' '.join(self.words)

def join_words(array: list) -> str:
    sentence = StringBuilder()
    for word in array:
        sentence.append(word)
    return str(sentence)

test_case = ['hi', 'how', 'are', 'you', 'doing?']
print(join_words(test_case))
