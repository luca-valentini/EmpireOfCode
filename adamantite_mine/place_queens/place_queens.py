def place_queens(placed):
    print(placed)
    for queen in placed:
        print(queen[0], queen[1])
        print(ord(queen[0]), ord(queen[1]))

        for rival in placed:
            if queen != rival:
                if queen[0] == rival[0] or queen[1] == rival[1]:
                    print("POTTO")
                    return []
                for i in range(8):
                    if (ord(queen[0]) % 8) == (ord(rival[0]) + i) % 8 and (ord(queen[1]) % 8) == (ord(rival[1]) + i) % 8:
                        print("POTTOOOO")
                        print(queen[0], queen[1])
                        print(str((ord(rival[0]) + i) % 8), str((ord(rival[1]) + i) % 8))
                        return []
    return placed


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    from itertools import combinations

    COLS = "abcdefgh"
    ROWS = "12345678"

    THREATS = {c + r: set(
        [c + ROWS[k] for k in range(8)] +
        [COLS[k] + r for k in range(8)] +
        [COLS[k] + ROWS[i - j + k] for k in range(8) if 0 <= i - j + k < 8] +
        [COLS[k] + ROWS[- k + i + j] for k in range(8) if 0 <= - k + i + j < 8])
        for i, r in enumerate(ROWS) for j, c in enumerate(COLS)}

    def check_coordinate(coor):
        c, r = coor
        return c in COLS and r in ROWS

    def checker(func, placed, is_possible):
        user_set = func(placed.copy())
        if not all(isinstance(c, str) and len(c) == 2 and check_coordinate(c) for c in user_set):
            print("Wrong Coordinates")
            return False
        threats = []
        for f, s in combinations(user_set.union(placed), 2):
            if s in THREATS[f]:
                threats.append([f, s])
        if not is_possible:
            if user_set:
                print("Hm, how did you place them?")
                return False
            else:
                return True
        if not all(p in user_set for p in placed):
            print("You forgot about placed queens.")
            return False
        if is_possible and threats:
            print("I see some problems in this placement.")
            return False
        return True
    place_queens(["b2", "c3", "d6", "e8"])
    #assert checker(place_queens, {"b2", "c4", "d6", "e8"}, True), "1st Example"
    #assert checker(place_queens, {"b2", "c4", "d6", "e8", "a7", "g5"}, False), "2nd Example"

    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")
