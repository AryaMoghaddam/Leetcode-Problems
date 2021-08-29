class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        result = []
        
        digitchar= { 
                
                '2' : 'abc',
                '3' : 'def',
                '4' : 'ghi',
                '5' : 'jkl' , 
                '6' : 'mno',
                '7' : 'pqrs',
                '8' : 'tuv',
                '9' : 'wxyz'   }
        
        
        def backtrack(i, curset):
            if len (curset) == len (digits):
                result.append(curset)
                return
            
            for c in  digitchar[digits[i]]:
                backtrack (i + 1, curset + c)

        if digits:
             backtrack( 0 , "")

        return result

        
            
