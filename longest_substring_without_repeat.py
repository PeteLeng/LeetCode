# Find the longest substring without repetitive characters

# Maintain a list of substrings, the longest substring is always at the front of the list.
# Maintain a library of characters, store the indices.
# Whenever a repeated character shows, prune the list, according to the index.
def longest_substring(s):
    char_dict = {}
    str_list = []
    longest = ''
    start = 0
    for i, char in enumerate(s):
        if char not in char_dict:
            char_dict[char] = i
            str_list.append('')
            for j in range(start, i+1):
                str_list[j] += char
        else:
            longest = str_list[start] if len(str_list[start]) > len(longest) else longest
            repeat_char_idx = char_dict[char]
            for k in range(start, repeat_char_idx+1):
                del char_dict[s[k]]
            char_dict[char] = i
            str_list.append('')
            for j in range(repeat_char_idx+1, i+1):
                str_list[j] += char
            start = repeat_char_idx + 1
            # print(f'{s[repeat_char_idx]} at {repeat_char_idx} repeats with {char} at {i}')
            # print(f'start updates to:{start}')
    # if start <= len(s)-1:
    longest = str_list[start] if len(str_list[start]) > len(longest) else longest
    # return str_list, longest
    return len(longest)


# def longest_substring_clean(s):
#     char_dict = {}
#     str_list = []
#     longest = 0
#     start = 0
#     for i, char in enumerate(s):
#         if char not in char_dict:
#             char_dict[char] = i
#             str_list.append(0)
#             for j in range(len(str_list)):
#                 str_list[j] += 1
#         else:
#             longest = max(longest, str_list[0])
#             new_start = char_dict[char] + 1
#             for k in range(start, new_start):
#                 del char_dict[s[k]]
#                 str_list.pop(0)
#             char_dict[char] = i
#             str_list.append(0)
#             for j in range(len(str_list)):
#                 str_list[j] += 1
#             start = new_start
#     if str_list:
#         longest = max(longest, str_list[0])
#     return longest


# Clean version
def longest_substring_clean(s):
    n = len(s)
    c_dict = {}
    longest = 0
    repeat = 0
    i = 0

    while i < n:
        char = s[i]
        if char in c_dict:
            longest = max(longest, i-repeat)
            repeat = c_dict[char] + 1
            # print(f'{s[repeat-1]} at {repeat-1} repeats {char} at {i}')
            c_dict = {s[j]: j for j in range(repeat, i + 1)}
        else:
            c_dict[char] = i
        i += 1
    if repeat < n:
        longest = max(longest, n-repeat)
    return longest


# Sliding window, using HastSet
def longest_substring_hashset(s):
    n = len(s)
    char_set = [0]*128  # Initialize the hash set
    i = j = 0
    longest = 0

    while j < n:
        r_char = s[j]
        char_set[ord(r_char)] += 1

        while char_set[ord(r_char)] > 1:
            l_char = s[i]
            char_set[ord(l_char)] -= 1
            i += 1

        longest = max(longest, j-i+1)
        j += 1

    return longest


def longest_substring_hashmap(s):
    char_dict = {}
    longest_str = 1, 0  # Such that empty string will be initialized to 0
    i = 0

    for j, char in enumerate(s):
        if char not in char_dict:
            char_dict[char] = j
            if j-i > longest_str[1]-longest_str[0]:
                longest_str = i, j
        else:
            if char_dict[char] >= i:
                # if j-i-1 > longest_str[1]-longest_str[0]:
                #     longest_str = i, j
                i = char_dict[char] + 1
            else:
                if j-i > longest_str[1]-longest_str[0]:
                    longest_str = i, j
            char_dict[char] = j
        print(f'longest string from {longest_str[0]} to {longest_str[1]}: {s[longest_str[0]:longest_str[1]+1]}')
    print(f'{longest_str[0]} - {longest_str[1]}')
    return longest_str[1]-longest_str[0]+1


def lengthOfLongestSubstring(s: str) -> int:
    n = len(s)
    ans = 0
    # mp stores the current index of a character
    mp = {}

    i = 0
    # try to extend the range [i, j]
    for j in range(n):
        if s[j] in mp:
            i = max(mp[s[j]], i)

        ans = max(ans, j - i + 1)
        mp[s[j]] = j + 1

    return ans


if __name__ == '__main__':
    # s = "abcbbab caxmnzlt ashasdi"
    # s = "a0ashsd!!!!ahaka asassaasdas --12=1,aasd- maxjqa"
    s = "pwwkew"
    # s = "aab"
    s = "nfpdmpi"
    # s = ' aa'
    # s = "tmmzuxt"
    # s = "abcdedxy"
    res1 = longest_substring_clean(s)
    res2 = longest_substring_hashset(s)
    res3 = longest_substring_hashmap(s)
    res4 = lengthOfLongestSubstring(s)
    print(res1, res2, res3, res4)
