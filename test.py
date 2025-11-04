def sortit(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[0]
    left, right = [], []
    for i in nums:
        if i <= pivot:
            left.append(i)
        else:
            right.append(i)
    return sortit(left) + [pivot] + sortit(right)


def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    nums = sortit(a)
    result = [nums[n - 2], nums[1]]
    return result