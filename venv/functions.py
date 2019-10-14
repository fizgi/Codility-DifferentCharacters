def different_char_count(string):
    different_chars = []

    for char in string:
        if char not in different_chars:
            different_chars.append(char)

    return len(different_chars)


def solution(string, number):
    char_list = []
    reversed_string = string[::-1]

    substring_start_index = 0
    substring_end_index = 0

    left_flag = 1
    right_flag = 1

    for left_pointer, right_pointer in zip(string, reversed_string):
        if left_pointer not in char_list and left_flag == 1:
            if len(char_list) < number:
                char_list.append(left_pointer)
            else:
                substring_start_index = string.index(left_pointer)
                left_flag = 0
        if right_pointer not in char_list and right_flag == 1:
            if len(char_list) < number:
                char_list.append(right_pointer)
            else:
                substring_end_index = len(string) - reversed_string.index(right_pointer)
                right_flag = 0

    return substring_start_index, substring_end_index
