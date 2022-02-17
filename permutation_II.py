# Given a collection of n numbers,
# there might be duplicates,
# find all unique permutations


# In the case where no duplicates exist,
# we use recursion that
# the first element has n options,
# ...
def permute_unique(nums):
    l = len(nums)
    if l == 1:
        return [nums]

    unique = {}
    res = []
    for i in range(len(nums)):
        if nums[i] not in unique:
            unique[nums[i]] = 1
            tail_permutaions = permute_unique(nums[:i] + nums[i+1:])
            for p in tail_permutaions:
                res.append([nums[i]] + p)
    return res


def main():
    nums = [1, 1, 2]
    print(permute_unique(nums))


if __name__ == '__main__':
    main()
