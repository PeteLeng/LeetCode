# Naive approach, loop through the array,
# use each element or pair of elements as axis
def longest_palindrome_naive(s):
    n = len(s)
    longest = ''
    for k in range(n):
        i, j = k, k
        while i >= 0 and j <= n-1 and s[i] == s[j]:
            i -= 1
            j += 1
        longest = max(s[i+1:j], longest, key=lambda x:len(x))
        i, j = k, k+1
        while i >= 0 and j <= n-1 and s[i] == s[j]:
            i -= 1
            j += 1
        longest = max(s[i+1:j], longest, key=lambda x: len(x))
    return longest


# Divide and conquer
# Each time divide the string in half,
# check the longest substring for the middle two elements,
# compare with the longest substring for left and right substring
# Time complexity: O(nlogn)
# Unfortunately this solution does not work
def longest_palindrome(s):
    n = len(s)
    if n <= 1:
        return s

    mid = int((n-1)/2)
    print(f'left string: {s[:mid+1]} \nright string: {s[mid+1:]}')
    left_str = longest_palindrome(s[:mid+1])
    right_str = longest_palindrome(s[mid+1:])

    mid_str = ''
    if s[mid] == s[mid+1]:
        i, j = mid, mid+1
        while i >= 0 and j <= n-1 and s[i] == s[j]:
            i -= 1
            j += 1
        mid_str = max(s[i+1:j], mid_str, key=lambda x:len(x))
    elif mid > 0:
        i, j = mid, mid
        while i >= 0 and j <= n-1 and s[i] == s[j]:
            i -= 1
            j += 1
        mid_str = max(s[i+1:j], mid_str, key=lambda x:len(x))
    elif mid+1 < n:
        i, j = mid+1, mid+1
        while i >= 0 and j <= n-1 and s[i] == s[j]:
            i -= 1
            j += 1
        mid_str = max(s[i+1:j], mid_str, key=lambda x:len(x))

    longest = max(left_str, right_str, mid_str, key=lambda s:len(s))
    # print(f'longest substring in {s}: {longest}')
    return longest


# Dynamic programming
# Let P(i, j) = 1 if s[i:j] is a palindrome else 0
# P(i, j) = P(i+1, j-1) + s[i] = s[j]
# Start from palindrome of length 1 all the way up to n
# import numpy as np


def longest_palindrome_dynamic(s):
    n = len(s)
    longest = ''
    update = 1
    tb = {}
    if n > 0:
        for i in range(0, n):
            for j in range(n-i):
                if i == 0:
                    tb[(i, j)] = 1
                elif i == 1:
                    tb[(i, j)] = int(s[j]==s[j+i])
                else:
                    tb[(i, j)] = int(s[j]==s[j+i] and tb[(i-2, j+1)])

                if update and tb[(i, j)]:
                    longest = s[j:j+i+1]
                    update = 0
            update = 1
    return longest

# Note that if numpy can't be used, do not use tb = [['nan']*n]*n to generate the matrix upfront.
# This reuses the list objects and cause trouble in assignment.
# Use a dictionary
# See [List of lists changes reflected across sublists unexpectedly](https://stackoverflow.com/questions/240178/list-of-lists-changes-reflected-across-sublists-unexpectedly)

if __name__ == '__main__':
    l = [
        "babad",
        "cbbd",
        "a",
        "ac",
        '!% ab    ba %!',
        'abc',
        'acbdhakalekkkksssee',
        "abacdfgdcaba",
        "caba",
        "dqmvxouqesajlmksdawfenyaqtnnfhmqbdcniynwhuywucbjzqxhofdzvposbegkvqqrdehxzgikgtibimupumaetjknrjjuygxvncvjlahdbibatmlobctclgbmihiphshfpymgtmpeneldeygmzlpkwzouvwvqkunihmzzzrqodtepgtnljribmqneumbzusgppodmqdvxjhqwqcztcuoqlqenvuuvgxljcnwqfnvilgqrkibuehactsxphxkiwnubszjflvvuhyfwmkgkmlhmvhygncrtcttioxndbszxsyettklotadmudcybhamlcjhjpsmfvvchduxjngoajclmkxiugdtryzinivuuwlkejcgrscldgmwujfygqrximksecmfzathdytauogffxcmfjsczaxnfzvqmylujfevjwuwwaqwtcllrilyncmkjdztleictdebpkzcdilgdmzmvcllnmuwpqxqjmyoageisiaeknbwzxxezfbfejdfausfproowsyyberhiznfmrtzqtgjkyhutieyqgrzlcfvfvxawbcdaawbeqmzjrnbidnzuxfwnfiqspjtrszetubnjbznnjfjxfwtzhzejahravwmkakqsmuynklmeffangwicghckrcjwtusfpdyxxqqmfcxeurnsrmqyameuvouqspahkvouhsjqvimznbkvmtqqzpqzyqivsmznnyoauezmrgvproomvqiuzjolejptuwbdzwalfcmweqqmvdhejguwlmvkaydjrjkijtrkdezbipxoccicygmmibflxdeoxvudzeobyyrutbcydusjhmlwnfncahxgswxiupgxgvktwkdxumqp"
    ]
    for s in l:
        # print(longest_palindrome_naive(s))
        print(longest_palindrome_dynamic(s))