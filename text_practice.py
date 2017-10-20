#!/usr/bin/env python

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

def word_count():
    

def main():
    in_str = 'aoeuueoa'

    # print('nothing yet')
    # print(vowel_count(in_str))
    # print(palindrome(in_str))

if __name__ == "__main__":
    main()
