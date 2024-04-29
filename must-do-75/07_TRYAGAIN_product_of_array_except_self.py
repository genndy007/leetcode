import math

nums = [1, 2, 3, 4]



def productExceptSelfN2(nums: list[int]) -> list[int]:
    answer = [1 for num in nums]
    for i in range(len(nums)):
        for j in range(len(answer)):
            if i != j:
                answer[j] *= nums[i]

    return answer


def productExceptSelfDivision(nums: list[int]) -> list[int]:
    product = math.prod(nums)
    for idx in range(len(nums)):
        nums[idx] = product // nums[idx] if nums[idx] != 0 else product

    return nums



productExceptSelf = productExceptSelfDivision

if __name__ == '__main__':
    result = productExceptSelf(nums)
    print(result)
