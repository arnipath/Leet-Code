#Merge Strings Alternately
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergedString = ""
        #Check length to properly merge
        if(len(word1) == len(word2)):
            for i in range(len(word1)):
                mergedString += word1[i]
                mergedString += word2[i]
        elif(len(word1) > len(word2)):
            for i in range(len(word1)):
                if(i >= len(word2)):
                    mergedString += word1[i]
                else:
                    mergedString += word1[i]
                    mergedString += word2[i]
        else:
            for i in range(len(word2)):
                if(i >= len(word1)):
                    mergedString += word2[i]
                else:
                    mergedString += word1[i]
                    mergedString += word2[i]
        return mergedString
