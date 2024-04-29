word1 = "abcuiuiuiui"
word2 = "pqryys"


def mergeAlternatively(word1: str, word2: str) -> str:
    merged_word = ''
    shortest_word = min([word1, word2], key=len)
    longest_word = set({word1, word2} - {shortest_word}).pop()
    for idx in range(len(shortest_word)):
        merged_word += word1[idx] + word2[idx]

    merged_word += longest_word[len(shortest_word):]

    return merged_word


if __name__ == '__main__':
    result = mergeAlternatively(word1, word2)
    print(result)
