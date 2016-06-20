def count_ingots(report):
    total = 0
    row = ""
    col = 0
    report = report.split(",")
    for element in report:
        for char in element:
            if char.isalpha():
                row = ord(char) - 65
            if char.isdigit():
                col = int(char)
        total = total + col + row * 9
    return total

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_ingots("A2,B1") == 12, "Two and ten"
    assert count_ingots("A1,A1,A1") == 3, "One, two, three"
    assert count_ingots("Z9,X8,Y7") == 672, "XYZ"
    assert count_ingots("C1,D1,B1,E1,F1") == 140, "Daily normal"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
