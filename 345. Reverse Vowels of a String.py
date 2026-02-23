#345 Reverse Vowels of a String
class Solution:
    def reverseVowels(self, s: str) -> str:
        #find all vowels first and then reverse them
        #then go back through the string and replace them
        list_of_vowels = ""
        new_s = ""
        for char in s:
            if(char in "aeiouAEIOU"):
                list_of_vowels += char
        reversed_str = "".join(reversed(list_of_vowels))

        for i in range(len(s)):
            if(s[i] in "aeiouAEIOU"):
                new_s += reversed_str[0:1]
                reversed_str = reversed_str[1:]
            else:
                new_s += s[i]
        return new_s
