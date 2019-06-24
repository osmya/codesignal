""" Note: Write a solution that only iterates over the string once and uses O(1) additional memory, 
since this is what you would be asked to do during a real interview.

Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. 
If there is no such character, return '_'.

Example

For s = "abacabad", the output should be
firstNotRepeatingCharacter(s) = 'c'.

There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first."""

def firstNotRepeatingCharacter(s):
    letters = [] # lists letters in string
    count = {} # counts letter repetition as key:value in a dict
    for i in s:
        if i in count:
            count[i] += 1 # count occurence
        else:
            count[i] = 1 # add key == letter
            letters.append(i)
    for i in letters: # search through dict
        if count[i] == 1: # finds the first not repeated letter
            return i
    return "_"
