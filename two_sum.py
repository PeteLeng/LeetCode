# Given an array of integers nums, and an integer target,
# return indices of two numbers such that they add up to target
import random


# Use dictionary, O(n)
def two_sum(nums, target):
    sums = {}
    for i, num in enumerate(nums):
        if num not in sums:
            sums[target-num] = i
        else:
            return [sums[num], i]


# Naive double loop, O(n**2)
def two_sum_quad(nums, target):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# Sort list, O(nlogn)
def quicksort(nums, start, end):
    if start != end:
        pivot = random.choice(range(start, end+1))
        nums[start], nums[pivot] = nums[pivot], nums[start]
        i = start
        for j in range(start+1, end+1):
            if nums[j] < nums[start]:
                i += 1
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
        nums[start], nums[i] = nums[i], nums[start]
        if i > start:
            quicksort(nums, start, i-1)
        if i < end:
            quicksort(nums, i+1, end)

def find(arr, number, start, end):
    """
    Suppose the array is sorted and the number
    is between the smallest and the largest element in the array.
    :param arr:
    :param number:
    :param start:
    :param end:
    :return:
    """
    if end == start + 1:
        return start, end
    else:
        mid = int((start + end)/2)
        if arr[mid] == number:
            return mid, mid+1
        elif arr[mid] > number:
            return find(arr, number, start, mid)
        else:
            return find(arr, number, mid, end)


# The idea is that for two number that add up to the target
# one is smaller than the target, the other is larger than the target
def two_sum_sort(nums, target):
    nums_sorted = nums[:]
    quicksort(nums_sorted, 0, len(nums)-1)
    i, j = find(nums_sorted, target/2, 0, len(nums)-1)
    while i >= 0 and j <= len(nums)-1:
        if nums_sorted[i] + nums_sorted[j] == target:
            return nums.index(nums_sorted[i]), nums.index(nums_sorted[j])
        elif nums_sorted[i] + nums_sorted[j] < target:
            j += 1
        else:
            i -= 1


if __name__ == '__main__':
    nums = [2, 7, 11, 15, 1, 3, 5, 28, 10, 4, 18, 9]
    target = 19

    # nums = [3, 2, 4]
    # target = 6

    # nums = [3, 3]
    # target = 6
    print(two_sum(nums, target))
    print(two_sum_quad(nums, target))
    print(two_sum_sort(nums, target))

    # Test quicksort and bisection find
    # quicksort(nums, 0, len(nums)-1)
    # print(nums)
    # res = find(nums, target/2, 0, len(nums)-1)
    # print(f'{target/2} is between {nums[res[0]], nums[res[1]]}')