#!/usr/bin/env python3
# -*- coding: utf-8 -*-


entered_word = input("Enter a word: ")
#makes case-insensitive
entered_word = entered_word.lower()
word_length = len(entered_word)
#creates a new empty string where a word will be read backwards
reversed_string = ""

#goes through the whole string and compares the first and the last letter,then the second from the beginning and the second from the end, and so on.
for letter in range(word_length,0,-1):
#adds every letter to the reserved string    
    reversed_string += entered_word[letter-1]
if entered_word == reversed_string:
        print("This is a palindrome.")

else:
        print("This is not a palindrome.")
        

