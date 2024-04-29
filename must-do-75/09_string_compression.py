chars = ["a","a","a","b","b","a","a"]


def compress(chars: list[str]) -> int:
    pass
    # curr_char = chars[0]
    # char_start_idx = 0
    # char_count = 1
    # i = 1
    # while i < len(chars):
    #     if i == len(chars) - 1 and char_count > 1:
    #         char_count += 1
    #         chars[char_start_idx + 1:] = [symbol for symbol in str(char_count)]
    #         break
    #
    #     if chars[i] == curr_char:
    #         char_count += 1
    #     elif char_count > 1:
    #         chars[char_start_idx + 1 : i] = [symbol for symbol in str(char_count)]
    #         i = char_start_idx + 1 + len(str(char_count))
    #         curr_char = chars[i]
    #         char_start_idx = i
    #         char_count = 1
    #         continue
    #
    #     if chars[i] != curr_char:
    #         curr_char = chars[i]
    #         char_start_idx = i
    #         char_count = 1
    #
    #     i += 1
    #
    # print(chars)
    # return len(chars)


if __name__ == '__main__':
    result = compress(chars)
    print(result)
