#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    return list(set(set_1) ^ set(set_2))
print(only_diff_elements({ "Python", "C", "Javascript" }, { "Bash", "C", "Ruby", "Perl" }))
