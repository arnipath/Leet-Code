#151 Reverse Words in a String
class Solution:
    def reverseWords(self, s: str) -> str:
        #can have extra space
        #space next to space or space in front or end
        reverse_str = ""
        for i in range(len(s)):
            if(i == 0 or i == len(s)-1):
                if(s[i] != " "):
                    reverse_str += s[i]
            else:
                if(s[i] == " "):
                    if(s[i+1] != " "):
                        reverse_str += s[i]
                else:
                    reverse_str += s[i]
        reverse_str = reverse_str.split()
        return " ".join(reversed(reverse_str))
