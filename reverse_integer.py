# Reverse a signed 32-bit integer,
# if the reversed integer is out of 32 bits, return 0
# Example: 123 -> 321; 120 -> 21; -123 -> -321


# Reversing an integer can be done by poping the last digit
# and pushing to the revered integer.
# pop = x % 10
# rev = rev*10 + pop
# The range of 32-bit integer is [-2**31, 2**31], [-2147483648, 2147483647]
# Note to check for overflow:
# If x > 0:
# - if rev < int(2**31/10), no overflow
# - if rev == int(2**31/10) and pop > 7
# - if rev > int(2**31/10), overflow
# If x < 0:
# - if rev < int(2**31/10), no overflow
# - if rev == int(2**31/10) and pop > 8
# - if rev > int(2**31/10), overflow
def reverse(x):
    maxint = int(2**31/10)
    positive = x > 0
    x = abs(x)
    rev = 0
    while x:
        pop = x % 10
        x = int(x/10)
        # print(f'pop:{pop}, x:{x}, rev:{rev}')
        if positive:
            if rev > maxint or (rev == maxint and pop > 7):
                return 0
            else:
                rev = 10 * rev + pop
        else:
            if rev > maxint or (rev == maxint and pop > 8):
                return 0
            else:
                rev = 10 * rev + pop
    return rev if positive else -rev


def main():
    numbers = [
        1,
        100,
        -992222,
        8987172,
        3345,
        8463847412,
    ]
    for n in numbers:
        print(reverse(n))


if __name__ == '__main__':
    main()