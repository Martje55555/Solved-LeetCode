class Solution(object):
    def helper(self, s):
        mapping = {}
        new_str = []
        
        for i, c in enumerate(s):
            if c not in mapping:
                mapping[c] = i
            new_str.append(str(mapping[c]))
        
        return " ".join(new_str)
        
    def isIsomorphic(self, s, t):
        return self.helper(s) == self.helper(t)
      
