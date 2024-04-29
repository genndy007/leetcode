candies = [12,1,12]
extraCandies = 10


def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    greatest_number_list = []
    for kid_candies in candies:
        greatest_number = kid_candies + extraCandies >= max(candies)
        greatest_number_list.append(greatest_number)

    return greatest_number_list


if __name__ == '__main__':
    result = kidsWithCandies(candies, extraCandies)
    print(result)
