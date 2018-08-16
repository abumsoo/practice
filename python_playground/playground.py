#!/usr/bin/env python

import string
import random

def reverse(in_str):
    rev_str = ''
    for c in in_str:
        rev_str = c + rev_str
    return rev_str

def pig_latin(in_str):
    if in_str[0] in 'aoeui':
        pig_str = in_str + 'ay'
    else:
        pig_str = in_str[1:] + in_str[0] + 'ay'
    return pig_str

def vowel_count(in_str):
    total = 0
    per_vowel = {}
    for c in in_str:
        if c in 'aoeui':
            total += 1
            if c not in per_vowel:
                per_vowel[c] = 1
            else:
                per_vowel[c] += 1
    return total, per_vowel

def palindrome(in_str):
    str_len = len(in_str)
    for i in range(str_len//2+1):
        if in_str[i] != in_str[str_len-(i+1)]:
            return False
    return True

def write_odd():
    odd_file = open("odds.txt", "w")
    for i in range(100):
        if i % 2 != 0:
            odd_file.write(str(i)+"\n")

    odd_file.close()

def write_even():
    even_file = open("evens.txt", "w")
    for i in range(100):
        if i % 2 == 0:
            even_file.write(str(i)+"\n")

    even_file.close()

def read_even():
    even_file = open("evens.txt", "r")
    lines = even_file.readlines()
    for line in lines:
        print(line)

def write_height():
    name = input("name: ")
    age = input("age: ")
    height = input("height: ")
    input_file = open("input.txt", "a")
    input_file.write(name + "," + age + "," + height + "\n")
    input_file.close()

def find_repeats():
    input_file = open("input.txt", "r")
    lines = input_file.readlines()
    lines = [line for line in lines if lines.count(line) > 1]
    print(lines)

def count_repeats():
    input_file = open("input.txt", "r")
    lines = input_file.readlines()
    for i in range(len(lines)):
        if lines[i] not in lines[:i]:
            print(lines[i],lines.count(lines[i]))

def fill_files():
    one_file = open("file1.txt", "w")
    two_file = open("file2.txt", "w")
    for i in range(20):
        one_file.write("This is line " + str(i) + "\n")
    for i in range(20, 40):
        two_file.write("This is line " + str(i) + "\n")
    one_file.close()
    two_file.close()

def swap_file_content():
    with open("file1.txt") as one_file, open("file2.txt") as two_file:
        one_lines = one_file.readlines()
        two_lines = two_file.readlines()
    with open("file1.txt", "w") as one_file, open("file2.txt", "w") as two_file:
        for line in two_lines:
            one_file.write(line)
        for line in one_lines:
            two_file.write(line)

def append_content():
    with open("file2.txt") as two_file, open("file1.txt", "a") as one_file:
        two_lines = two_file.readlines()
        for line in two_lines:
            one_file.write(line)

def extract_unique_content():
    with open("file2.txt") as two_file, open("file1.txt") as one_file:
        one_lines = one_file.readlines()
        two_lines = two_file.readlines()
    with open("file3.txt", "w") as three_file:
        for line in one_lines:
            if line not in two_lines:
                three_file.write(line)
        for line in two_lines:
            if line not in one_lines:
                three_file.write(line)

def main():
    with open("scores", "w") as f:
        for i in range(100):
            name = ""
            for i in range(4):
                name += random.choice(string.ascii_lowercase)
            f.write(name + "," +
                    str(random.randrange(101)) + "," +
                    str(random.randrange(101)) + "," +
                    str(random.randrange(101)) + "\n")
    


if __name__ == "__main__":
    main()
