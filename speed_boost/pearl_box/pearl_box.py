def white_probability(white_marbles, black_marbles):
    return float(white_marbles) / (white_marbles + black_marbles)

def probability(marbles, step):
    black_marbles = marbles.count("b")
    white_marbles = marbles.count("w")
    wp = white_probability(white_marbles, black_marbles)
    bp = 1 - wp
    for i in range(step):
        if step == 1:
            wp = white_probability(white_marbles, black_marbles)
            return white_probability(white_marbles, black_marbles)
        else:
            if (white_marbles == 0):
                wp = white_probability(white_marbles, black_marbles)
                return probability("w" * (white_marbles+1) + "b" * (black_marbles-1), step-1)
            elif (black_marbles == 0):
                wp = white_probability(white_marbles, black_marbles)
                return probability("w" * (white_marbles-1) + "b" * (black_marbles+1), step-1)
            else:
                wp = white_probability(white_marbles, black_marbles)
                return (wp * probability("w" * (white_marbles-1) + "b" * (black_marbles+1), step-1)) + (bp * probability("w" * (white_marbles+1) + "b" * (black_marbles-1), step-1))

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(probability('bbw', 3), 0.48), "1st example"
    assert almost_equal(probability('wwb', 3), 0.52), "2nd example"
    assert almost_equal(probability('www', 3), 0.56), "3rd example"
    assert almost_equal(probability('bbbb', 1), 0), "4th example"
    assert almost_equal(probability('wwbb', 4), 0.5), "5th example"
    assert almost_equal(probability('bwbwbwb', 5), 0.48), "6th example"
    print("All done? Earn rewards by using the 'Check' button!")
