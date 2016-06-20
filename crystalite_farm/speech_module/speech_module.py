FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen",
              "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty",
              "sixty", "seventy", "eighty", "ninety"]
HUNDRED = "hundred"
THOUSAND = "thousand"


def tell_number(number):
    if number == 0:
        return "zero"
    number_string = ""
    number = str(number)
    i = len(number)
    if (number[0] == '-'):
        number_string += "minus "
        i -= 1
    if i == 7:
        if number[-i] != '0':
            number_string += FIRST_TEN[int(number[-i]) - 1] + " million "
        i -= 1
    if i == 6:
        if number[-i] != '0':
            number_string += FIRST_TEN[int(number[-i]) - 1] + " hundred "
        i -= 1
    if i == 5:
        if number[-i] != '0':
            if int(number[-5:-3]) < 20 and int(number[-5:-3]) > 9:
                number_string += SECOND_TEN[int(number[-i:]) - 10]
                i -= 1
            else:
                number_string += OTHER_TENS[int(number[-i]) - 2] + " "
        i -= 1
    if i == 4:
        if number[-i] != '0':
            number_string += FIRST_TEN[int(number[-i]) - 1] + " thousand "
        i -= 1
    if i == 3:
        if number[-i] != '0':
            number_string += FIRST_TEN[int(number[-i]) - 1] + " hundred "
        i -= 1
    if i == 2:
        if number[-i] != '0':
            if int(number[-2:]) < 20 and int(number[-2:]) > 9:
                number_string += SECOND_TEN[int(number[-i:]) - 10]
                i -= 1
            else:
                number_string += OTHER_TENS[int(number[-i]) - 2] + " "
        i -= 1
    if i == 1:
        if number[-i] != '0':
            number_string += FIRST_TEN[int(number[-i]) - 1]
        i -= 1
    if number_string[-1:] == " ":
        number_string = number_string[:-1]
    return number_string


if __name__ == '__main__':

    print(tell_number(245312))
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # Rank 1
    assert tell_number(4) == 'four', "1st example"
    assert tell_number(133) == 'one hundred thirty three', "2nd example"
    assert tell_number(12) == 'twelve', "3rd example"
    assert tell_number(101) == 'one hundred one', "4th example"
    assert tell_number(212) == 'two hundred twelve', "5th example"
    assert tell_number(40) == 'forty', "6th example"
    assert not tell_number(212).endswith(' '), "Dont forget strip whitespaces at the end of string"

    # Rank 2
    assert tell_number(-133) == 'minus one hundred thirty three', "Minus"
    assert tell_number(0) == 'zero', "Zero"

    # Rank 3
    assert tell_number(42000) == 'forty two thousand', "42 many"
    assert (tell_number(-999999) ==
            "minus nine hundred ninety nine thousand nine hundred ninety nine"), "Abyss"

    print("Earn cool rewards by using the 'Check' button!")
