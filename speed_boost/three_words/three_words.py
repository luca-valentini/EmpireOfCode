def three_words(words):
    counter = 0
    words = words.split(" ")
    for word in words:
        if word.isalpha():
            counter += 1
            if counter == 3:
                break
        else:
            counter = 0
    print(counter)
    return True if counter >= 3 else False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert three_words("Hello World hello"), "Hello"
    assert not three_words("He is 123 man"), "123 man"
    assert not three_words("1 2 3 4"), "Digits"
    assert three_words("bla bla bla bla"), "Bla Bla"
    assert not three_words("Hi"), "Hi"
    print("Earn cool rewards by using the 'Check' button!")
