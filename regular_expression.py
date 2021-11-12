# Given input s and pattern p,
# implement rg with support for '.' and '*'
# Note that the marks refer to the pattern
# - '.' Matches any single character.
# - '*' Matches zero or more of the preceding element.

# # I misunderstood in the beginning, (a*) together means zero or more 'a's,
# # rather than 'a' followed by zero or more 'a's
# The naive iterative approach does not work.
def isMatch(s, p):
    i, j = 0, 0
    matching = 0
    while i <= len(s) - 1 and j <= len(p) - 1:
        if p[j] == '*':
            j -= 1
            if s[i] == p[j] or p[j] == '.':
                # print(f'{s[i]} matches with {p[j]}')
                i += 1
                j += 1
                continue
            else:
                # print(f"{s[i]} doesn't match with {p[j]}")
                j += 2
        if j > len(p) - 1:
            return False

        if s[i] == p[j] or p[j] == '.':
            # print(f'{s[i]} matches with {p[j]}')
            matching = 1
            i += 1
            j += 1
        else:
            # print(f"{s[i]} doesn't match with {p[j]}")
            if matching:
                return False
            else:
                j += 1

    # return f"s: {s[i:]}, p: {p[j:]}"
    if s[i:]:
        return False
    else:
        if not p[j:]:
            return True
        else:
            k = len(s) - 1
            l = len(p) - 1
            print(f'stop at p[{j}]')
            while l >= j:
                print(f"p[{l}], s[{k}]")
                if k < 0:
                    return False
                if p[l] != s[k] and p[l] != '*':
                    return False
                l -= 1
                k -= 1
            return True


# Matching without support for asterisk is simple,
# simply check from left to right if each character in s matches with the pattern

# If a * is present,
# - either ignore this part of the pattern match s with p[2:]
# - or delete a matching character in s and match s[1:] with p

def is_match(s, p):
    # this is clever
    # the base case,
    # if p runs out and if s does not, return false
    if not p:
        return not s

    # this is beautiful code,
    # bool(s) handles situation where s runs out and p has characters other than *.
    # If s runs out and p contains non * character,
    # the recursive call always reaches the second branch and evaluates to False without going deeper,
    # thus it's unnecessary to check base case for s is empty string.
    # On the other hand, is s runs out, and p contains only *,
    # the if branch will always be executed and p will be recursively reduced to base case.
    first_match = bool(s) and (s[0] == p[0] or p[0] == ".")
    # when indexing, check length to avoid exception.
    if len(p) >= 2 and p[1] == "*":
            return is_match(s, p[2:]) or (first_match and is_match(s[1:], p))
    else:
        return first_match and is_match(s[1:], p[1:])


def main():
    pools = [
        # dict(s = "aa", p = "a"),
        # dict(s = "aa", p = "a*"),
        # dict(s = "ab", p = ".*"),
        # dict(s = "aab", p = "c*a*b"),
        # dict(s = "mississippi", p = "mis*is*p*."),
        dict(s = "ab", p = ".*c"),
        dict(s="aaa", p="a*a"),
        dict(s="aaa", p="a*aa"),
        dict(s="abcdasdaff", p=".*daff"),
        dict(s="daff", p=".*daff"),
    ]
    for d in pools:
        print(f'Matching {d["s"]} against {d["p"]}')
        print(isMatch(d["s"], d["p"]))

if __name__ == '__main__':
    main()

    # Edge case:
    # Input: s = "ab", p = ".*c";
    # Output: False

