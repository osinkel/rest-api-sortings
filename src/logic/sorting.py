import random


def selection_sort(nums: list, i: int = 0):
    if i == len(nums):
        return nums
    else:
        index_min = nums[::-1].index(min(nums[i:])) + 1
        nums[-index_min], nums[i] = nums[i], nums[-index_min]
        i += 1
        selection_sort(nums, i)
        return nums


def insertion_sort(nums: list):
    i = 1
    while i != len(nums):
        k, j = i - 1, i
        while k >= 0 and nums[j] < nums[k]:
            nums[j], nums[k] = nums[k], nums[j]
            j = k
            k -= 1
        i += 1
    return nums


def quick_sort(nums: list):
    if len(nums) > 1:
        pivot = random.choice(nums)
        less = [x for x in nums if x < pivot]
        more = [x for x in nums if x > pivot]
        equal = [pivot] * nums.count(pivot)
        return quick_sort(less) + equal + quick_sort(more)
    else:
        return nums


def shaker_sort(nums: list):
    direction, k = 1, 0
    last_index = len(nums) - 1
    for i in range(len(nums)):
        k = i + 1
        if last_index - i <= 0:
            return nums
        while True:
            if k == last_index + 1:
                last_index -= 1
                direction = -1
                k -= 1

            if nums[k] < nums[k - 1]:
                nums[k], nums[k - 1] = nums[k - 1], nums[k]

            k += direction

            if k == i:
                direction = 1
                break


