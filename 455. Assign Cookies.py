#455 Assign Cookies
def findContentChildren(self, g: List[int], s: List[int]) -> int:
        #sort cookies in ascending order
        g.sort()
        s.sort()
        #two pointers to track arrays
        i = 0
        j = 0
        length_g = len(g)
        length_s = len(s)
        #keep track of the number of kids
        number_of_kids = 0
        #loop through the arrays and compare size of greed to cookie
        #if the greed less than or equal to cookie size then keep track of kid
        #and move on to next cookie and kid
        while i < length_g and j < length_s:
            if(g[i] <= s[j]):
                number_of_kids += 1
                i += 1
                j += 1
            #otherwise move on to next cookie
            else:
                j += 1
        #return number_of_kids
        return number_of_kids

