flowerbed = [1, 0, 0, 0, 1, 0, 0]
n = 2


def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    current_plot_idx = 0
    possible_flowers = 0
    while current_plot_idx < len(flowerbed):
        if current_plot_idx == len(flowerbed) - 1 and flowerbed[current_plot_idx] == 0:
            possible_flowers += 1
            break
        elif flowerbed[current_plot_idx] == 0 and flowerbed[current_plot_idx + 1] == 0:
            possible_flowers += 1
            current_plot_idx += 2
        elif flowerbed[current_plot_idx] == 1:
            current_plot_idx += 2
        elif flowerbed[current_plot_idx + 1] == 1:
            current_plot_idx += 3

    return possible_flowers >= n


if __name__ == '__main__':
    result = canPlaceFlowers(flowerbed, n)
    print(result)

# if flowerbed[current_plot_idx] == flowerbed[current_plot_idx + 1] == 0:
#     possible_flowers += 1
#     current_plot_idx += 2
# else:
#     current_plot_idx += 1
