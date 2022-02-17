# generate all permutations of a string
# 'ab', 'ba'
# 'abc', 'acb', 'bac', 'bca', 'cab', 'cba'


# Number of permutations, n!
# Recursion:
# P(n) = n * P(n - 1)
def permute_recur(nums):
    l = len(nums)
    if l == 1:
        return [nums]
    res = []
    for perm in permute_recur(nums[1:]):
        res += [perm[:i] + [nums[0]] + perm[i:] for i in range(l)]
    return res

def permute(s):
    res = []
    if len(s) == 0:
        return []
    elif len(s) == 1:
        return [s]

    for i in range(len(s)):
        tail = permute(s[:i] + s[i+1:])
        for t in tail:
            res.append(s[i]+t)

    return res


def main():
    # s = 'abcd'
    # print(permutate(s))

    nums = [1, 2, 3, 4]
    print(permute_recur(nums))


if __name__ == "__main__":
    main()
