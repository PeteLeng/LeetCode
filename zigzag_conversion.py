# Convert a string to 'zigzag' string

# The idea is that the pattern repeats itself every 2n-2 elements.
# The naive approach is to group elements by line, and then glue them together.
def convert(s, numRows):
    if numRows == 1:
        return s
    l = []
    for i in range(len(s)):
        idx = i % (2*numRows-2)
        if idx <= numRows-1:
            try:
                l[idx] += s[i]
            except:
                l.append(s[i])
        else:
            idx = 2*numRows-2-idx
            l[idx] += s[i]
    return ''.join(l)


# Convert a string to zigzag when printed out
# Each repetitive block has width n-1,
# elements in row 0 need (n-2) paddings,
# elements in row (n-1) need n-2 paddings,
# elements in row i need (n-2)-i paddings or i-1 paddings
def convert_full(s, numRows):
    l = []
    for i in range(len(s)):
        idx = i % (2*numRows-2)
        if idx < numRows-1:
            try:
                l[idx] += s[i].ljust(numRows-1-idx, ' ')
            except:
                l.append(s[i].ljust(numRows-1-idx, ' '))
        elif idx == numRows-1:
            try:
                l[idx] += s[i].ljust(numRows-1, ' ')
            except:
                l.append(s[i].ljust(numRows-1, ' '))
        else:
            idx = 2*numRows-2-idx
            l[idx] += s[i].ljust(idx, ' ')
    return '\n'.join(l)


# The idea is to loop through each row, if there exists a character,
# pop the list and append the character, otherwise append zero
# This is too slow and not smart enough.
# Instead, I can do additional bookkeeping while creating the list.


def main():
    s_list = [
        'PAYPALISHIRINGAVBFEESSAFGGASZZXDSDAXZZDFASDASDW@ASZCASDASDAZXCASDA',
        # 'A'
    ]
    for s in s_list:
        print(convert_full(s, 6))


if __name__ == "__main__":
    main()
