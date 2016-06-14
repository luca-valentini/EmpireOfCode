def golf(password):
    j = [0, 0, 0]
    if len(password) >= 10:
        for i in password:
            if i.isdigit():
                j[0] = 1
            elif i.isupper():
                j[1] = 1
            else:
                j[2] = 1
    return True if sum(j) == 3 else False

if __name__ == '__main__':
#     # These "asserts" using only for self-checking and not necessary for auto-testing
    golf('A1213pokl') == False
    golf('bAse730onE') == True
    golf('asasasasasasasaas') == False
    golf('QWERTYqwerty') == False
    golf('123456123456') == False
    golf('QwErTy911poqqqq') == True
    print(golf('QwErTy911poqqqq'))
    print("Use 'Check' to earn sweet rewards!")
