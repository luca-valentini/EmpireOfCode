def find_message(text):
    secret_message = ""
    """Find a secret message"""
    for char in text:
        if char.isupper():
            secret_message += char
    return secret_message


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"

    print("Earn cool rewards by using the 'Check' button!")
