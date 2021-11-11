import random
import timeit

# KMP algorithm is used to search for occurrences of a word W
# within a text string S in linear time of the length the string.

# The naive implementation
# Compare all contiguous substrings in S of length |W| with the word W
# There are |S|-|W|+1 such substrings, starting from index 0 to index |S|-|W|.
# for each substring starting at index m, match S[m+i] with W[i],
# until W is exhausted, in which case we have a match,
# or if we find a mismatch, we move on to the next substring starting at index m+1

def get_str(path):
    with open(path, "r", encoding='UTF-8') as f:
        return f.readlines()


def naive_match(s, w):
    matches = []
    for i in range(len(s) - len(w) + 1):
        for j, cha in enumerate(w):
            if s[i + j] != cha:
                break
        else:
            matches.append(i)
    return matches


# KMP reduces the redundant testing of characters in the naive implementation.
# Consider the two cases:
# match word "ABCD" in string "ABCABCABCD",
# Comparing the substring starting at S[0] with W,
# the match halts at S[3] != W[3].
# Instead of incrementing the index to S[1] in naive implementation,
# we restart the process at S[3],
# since none of the suffix of the matching string "ABC" starts with "A",
# thus we are sure that any substring starting before S[3] is not a match.

# match word "ABCABCD" with string "ABCABCABCD",
# The match fails at S[6], where S[6] != W[6].
# Here the comparison resumes at index S[3], since the matching string "ABCABC"
# has suffix "ABC" that exactly matches its prefix "ABC".
# So the starting index backtracks 3, which is the length of the suffix.
# Note that in implementation, we don't need to move the string pointer back to S[3].
# We use another pointer to keep track of where in the word we are matching,
# and simply move the word pointer forward and start matching from W[3].

# The observation is that the structure of the word tells us
# where we need to resume matching if a mismatch happens.
# And the idea is to pre-build a "partial match" table aka the "failure function"
# before running the match.


# Assume we already have the match table that tells us
# how much should the string pointer backtrack, i.e., the word pointer moves forward.
# the special case is when S[m + 0] != W[0], the string index has to increase 1,
# meaning that T[i] is -1.
def kmp_search(s, w, t):
    matches = []
    i = j = 0
    # i is the string pointer
    while i < len(s):
        if s[i] == w[j]:
            i += 1
            j += 1
            if j == len(w):
                matches.append(i - j)
                j = t[j]
        else:
            # if mismatch, i backtracks
            j = t[j]
            # the special case, i does not backtrack
            if j < 0:
                i += 1
                j = 0
    return matches

# Running time
# The two branch of the loop can be thought of as
# either increasing the index of the character being matched, m + j
# or increasing the starting index of the substring, m
# the first branch can be executed at most n times,
# with the second branch being reached at most n times,
# since m <= m + j, if m >= n (second branch executed n times),
# branch one must have reached n in the past.
# The total amount of loops is bounded by 2n.

# Building the match table (fail function)
# the table value for any index j is essentially
# the index at which the next match should start in the word
# when the mismatch happens exactly at index j, S[m+j] != W[j]
# T[0] = -1, meaning that the string index m should increment by 1

# Consider the word "ABCDABCDABCDE"
# the table value for index 8, 9, 10, 11 is exactly the same as 0, 1, 2, 3,
# and 4, 5, 6, 7.
# And T[12] = 8, since the length of the longest suffix that matches the prefix is 8
# "ABCDABCD".
# We can use an pointer i to book-keep the length of the longest suffix.
# Since the prefix always starts at W[0], we set i = 0,
# walk down the word and compare W[j] with W[i],
# if there's a match, we set t[j] to t[i], and increment i,
# else when there's a mismatch,
# either we are able to find a matching suffix from the substring of len i before j
# or i is set back to 0,
# which is equivalent to finding a matching suffix at index i,
# since the preceding substring is equivalent,
# which we can then recursively check whether W[j] == w[T[i]],
# by definition, T[i] is the index we start the next match when there's a mismatch at index i.


def kmp_table(w):
    table = [-1]
    # i is the length of the matching prefix
    i = 0
    j = 1
    while j < len(w):
        if w[j] == w[i]:
            t_j = table[i]
            table.append(t_j)
            # i += 1
        else:
            t_j = i
            table.append(t_j)
            # if W[j] == W[T[i]], increment i by 1
            while i >= 0 and w[j] != w[i]:
                i = table[i]
            # i += 1
        j += 1
        i += 1
    table.append(i)
    return table


def kmp_match(s, w):
    t = kmp_table(w)
    return kmp_search(s, w, t)


def main():
    file_name = "kmp_test_word.txt"
    # Test naive
    s = "ABC ABCDAB ABCDABCDABDE"
    w = "ABCDABD"
    print(naive_match(s, w))

    # Test kmp
    t = kmp_table(w)
    # print(t)
    print(kmp_search(s, w, t))

    # Test kmp table
    # words = [
    #     "ABCDABD",
    #     "ABACABABC",
    #     "ABACABABA",
    #     "PARTICIPATE IN PARACHUTE"
    # ]
    # for w in words:
    #     print(w)
    #     print(kmp_table(w))

    # Compare speed
    # random.seed(0)
    # word = get_str(file_name)[0]
    # word_len = len(word)
    # word_str = ""
    # for i in range(100):
    #     word_str += word
    #     word_str += word[:int(random.random() * word_len)]
    # print(len(word_str))
    # print(word_str[:500])

    stmts = [
        "naive_match(word_str, word)",
        "kmp_match(word_str, word)",
    ]
    num_trials = [1]
    for num in num_trials:
        for s in stmts:
            method = s[:s.find('(')]
            t = timeit.timeit(s, globals=globals(), number=num)
            print(f'running {method} {num} times: {t} s')


if __name__ == "__main__":
    file_name = "kmp_test_word.txt"
    random.seed(0)
    word = get_str(file_name)[0]
    word_len = len(word)
    word_str = ""
    for i in range(10000):
        word_str += word
        word_str += word[:int(random.random() * word_len)]
    print(len(word_str))
    main()

    # the str length is around 10 mil, 10949820
    # "running naive_match 1 times: 4.042654400000002 s"
    # "running kmp_match 1 times: 2.6727758999999978 s"
    # This is hardly impressive, I spend the whole day understanding a algorithm
    # that only improve less than 50% running time.
    # I guess the average running time of the naive approach is pretty good already
