def flat_list(array):
    new_array = []
    for element in array:
        if type(element) is int:
            new_array.append(element)
        else:
            new_array.extend(flat_list(element))
    return new_array

if __name__ == "__main__":
    assert flat_list([1, 2, 3]) == [1, 2, 3], "Flat"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "One"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Nested"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "In In"
    flat_list([[-1], [1, [-2], 1], []])
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
