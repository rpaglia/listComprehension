# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 09:48:19 2021

@author: Richard Paglia

List Comprehension

List comprehensions follow naturally from set builder notation and lambda calculus. They are very cool and make your life a lot easier. 
Read about list comprehensions in the text book. Also the Wikipedia article on list comprehensions is good, and

Problems: write a python (.py or .ipynb) that: 
1. Writes a list comprehension that prints a list of the cubes of the numbers 1 through 10.
2. Write a list comprehension that prints out the possible results of two coin flips (one result would be ’ht’).
(Hint - how many results should there be?)
3. Write a function that takes in a string and uses a list comprehension to return all the vowels in the string.
4. Run this list comprehension 
[x+y for x in [10,20,30] for y in [1,2,3]]

and figure out what is going on here,.   Next, write a nested for loop that gives you the same result. 
This will show you've explained what the comprehension does 
"""
# List of cubes of the numbers 1-10
for x in range(1, 11):
    print([x**3])

# Possible results of two coin flips
for x in ('h', 't'):
    for y in ('h', 't'):
        print([x+y])

# Return all vowels in a string
def returnVowels(string):
    vowels = "AaEeIiOoUu"
    result = [x for x in string if x in vowels]
    print(result)

string = input('Enter a string: ')
returnVowels(string)

# Run this list comprehension [x+y for x in [10,20,30] for y in [1,2,3]]
for x in [10,20,30]:
    for y in [1,2,3]:
        print([x+y])
