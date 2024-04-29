nums = [2, 1, 5, 0, 4, 6]


def increasingTripletFactorial(nums: list[int]) -> bool:
    for i in range(len(nums) - 2):
        first_num = nums[i]
        for j in range(i + 1, len(nums) - 1):
            if nums[j] > first_num:
                second_num = nums[j]
                for k in range(j + 1, len(nums)):
                    if nums[k] > second_num:
                        third_num = nums[k]
                        print(f"Found triplet: {first_num} < {second_num} < {third_num}")
                        return True

    return False

def increasingTripletTwoPointer(nums: list[int]) -> bool:
    if len(set(nums)) < 3:
        return False

    idx_start = 0
    idx_end = len(nums) - 1

    first_num = float('inf')
    third_num = -float('inf')

    while idx_start < idx_end:
        if nums[idx_start] < first_num:
            first_num = nums[idx_start]

        if nums[idx_end] > third_num:
            third_num = nums[idx_end]


    return False




increasingTriplet = increasingTripletFactorial

if __name__ == '__main__':
    result = increasingTriplet(nums)
    print(result)

