## this can be solved in multiple ways, one of them being comparing the first and last index and second and second last index and so on ... 
## but the above method ain't faster compared to the reverse operation in python

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if x == x[::-1]:
            return True
        return False


## Second solution is to do this without converting to string...
## iteratively get the remainder and multiply by 10 and keep adding the new number... 
## This logic will help us reverse the number without converting to string
## but when we do this its O(n) complexity
## hence instead of reversing the entire number just reverse the first half of the number and compare

class Solution:
    def isPalindrome(self, n: int) -> bool:
      if n < 0:
          return False
      x, y = n, 0
      while x > y:
          x, y = x // 10, y * 10 + x % 10
      # When the length is an odd number, we can get rid of the middle digit by y // 10
      return x == y or x == y // 10
