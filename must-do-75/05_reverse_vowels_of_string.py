s = "za wArudO"
# s = "leetcode"
answer = "zO wurAda"


def reverseVowelsOLD(s: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u']

    stack_vowels = []
    for letter in s:
        if letter.lower() in vowels:
            stack_vowels.append(letter)

    result_string = ''
    for idx in range(len(s)):
        if s[idx].lower() in vowels:
            result_string += stack_vowels.pop()
        else:
            result_string += s[idx]

    return result_string


def reverseVowels(s: str) -> str:
    VOWELS = ['a', 'e', 'i', 'o', 'u']
    stack_vowels = [letter for letter in s if letter.lower() in VOWELS]
    return ''.join([stack_vowels.pop() if letter.lower() in VOWELS else letter for letter in s])


if __name__ == '__main__':
    result = reverseVowels(s)
    print(result)

    # for idx in range(len(s)):
    #     letter = s[idx]
    #     if letter.lower() in vowels:
    #         vowels_values.insert(0, letter)
