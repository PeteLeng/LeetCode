# Covert a string to 32-bit integer
def myAtoi(s):
    numbers = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    is_prefix = 1
    is_positive = 1
    res = 0
    for c in s:
        if is_prefix:
            if c == ' ':
                continue
            else:
                is_prefix = 0
                if c == '+':
                    is_positive = 1
                elif c == '-':
                    is_positive = 0
                elif c in numbers:
                    res = 10 * res + numbers[c]
                else:
                    return 0
        else:
            if c in numbers:
                res = 10 * res + numbers[c]
            else:
                break
    res = res if is_positive else -res
    if res > 2**31 - 1:
        return 2**31 - 1
    elif res < - 2**31:
        return -2**31
    else:
        return res


def main():
    s_list = [
        "42",
        "   -42",
        "4193 with words",
        "words and 987",
        "-91283472332",
    ]
    for s in s_list:
        print(myAtoi(s))


if __name__ == '__main__':
    main()