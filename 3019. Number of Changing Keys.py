#3019. Number of Changing Keys
class Solution:
    def countKeyChanges(self, s: str) -> int:
        times_key_changed = 0
        word = s.lower()
        #loop through word
        for i in range(len(s)-1):
            #check if char is different
            #and keep track
            if(word[i] != word[i+1]):
                times_key_changed += 1
        return times_key_changed
