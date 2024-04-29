str1 = "ABABABAB"
str2 = "ABAB"


def gcdOfStrings(str1: str, str2: str) -> str:
    shortest_word = min([str1, str2], key=len)
    largest_gcd = ''
    for idx in range(len(shortest_word)):
        gcd = shortest_word[:idx + 1]
        if str1.replace(gcd, '') == str2.replace(gcd, '') == '':
            largest_gcd = gcd

    return largest_gcd


if __name__ == '__main__':
    result = gcdOfStrings(str1, str2)
    print(result)
