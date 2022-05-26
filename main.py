# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") -->


from gettext import find


# def find_anagram(word, anagram):
# [assignment] Add your code here

a = input("word:")
b = input("anagram:")
sorted_a = sorted(a)
sorted_b = sorted(b)
if sorted_a == sorted_b:
    print("True")
else:
    print("False")
