def anagram(s1,s2): # to check string comparison same char neglect space and uppercase
    
    # Remove spaces and lowercase letters
    s1 = s1.replace(' ','').lower()#.replace() will replace all occurances
    s2 = s2.replace(' ','').lower()# we can use dict to count one string and minus the other string and dict count should be zero at final
    
    # Return boolean for sorted match.
    return sorted(s1) == sorted(s2)

