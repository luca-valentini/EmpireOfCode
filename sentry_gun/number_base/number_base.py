def convert(str_number, radix):
    str_number = str_number[::-1]
    i = 0
    total = 0
    for char in str_number:
        print(char)
        if char.isalpha():
            if (ord(char) - 55) >= radix:
                total = -1
                break
            total += (ord(char) - 55) * (radix ** i)
        elif char.isdigit():
            if int(char) >= radix:
                total = -1
                break
            total += int(char) * (radix ** i)
        i += 1
    return total


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert convert("AF", 16) == 175, "Hex"
    assert convert("101", 2) == 5, "Bin"
    assert convert("101", 5) == 26, "5 base"
    assert convert("Z", 36) == 35, "Z base"
    assert convert("AB", 10) == -1, "B > A > 10"

    print("Use 'Check' to earn sweet rewards!")
