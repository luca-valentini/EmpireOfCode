from math import acos
from math import degrees


def angles(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a or a * b * c == 0:
        return [0, 0, 0]
    else:
        ang_a = round(degrees(acos((a ** 2 - b ** 2 - c ** 2) / (-2 * b * c))))
        ang_b = round(degrees(acos((b ** 2 - a ** 2 - c ** 2) / (-2 * a * c))))
        ang_c = 180 - ang_a - ang_b
        return sorted([ang_a, ang_b, ang_c])


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert angles(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert angles(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert angles(2, 2, 5) == [0, 0, 0], "It can not be a triangle"

    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")
