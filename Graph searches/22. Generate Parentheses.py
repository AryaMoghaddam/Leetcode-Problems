class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
      
# only add "(" if open < n
# only add "(" if close < open
# stop when open == close == n


      stack = []
      res = []
          # open = o , close = c
          def backtrack(o, c)
            if o == c == n:    
            res.append("".join(stack))
            return
          
            if o < n:
              stack.append("(")
              backtrack(o + 1, c)
              stack.pop()
              
            if c < n:
              stack.append(")")
              backtrack (o , c + 1)
              stack.pop()
              
        backtrack (0,0)
        return res
              
