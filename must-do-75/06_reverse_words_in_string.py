s = " the sky  is   blue   "
s = "a good   example"


def reverseWordsOLD(s: str) -> str:
    words = []
    current_word = ''
    for letter in s:
        if letter != ' ':
            current_word += letter
        elif current_word:
            words.append(current_word)
            current_word = ''

    if current_word:
        words.append(current_word)

    return ' '.join(words[::-1])

def reverseWords(s: str) -> str:
    # words = s.split()
    return ' '.join(s.split()[::-1])



if __name__ == '__main__':
    result = reverseWords(s)
    print(result)
