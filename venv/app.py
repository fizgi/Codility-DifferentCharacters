from functions import *

string = input("Enter a string: ")
number = int(input("Enter an integer: "))

if number > different_char_count(string):
    print("There is no such substring of S that, after removal, " +
          "leaves S containing exactly " + str(number) + " different character(s).")
else:
    start_index, end_index = solution(string, number)
    print(string[:start_index] + " < " + string[start_index:end_index] + " > " + string[end_index:])
