"""

Solving iteratively, solves the question N^2 complexity

To reduce the complexity, use hashmap in a smart way

Hash map --> in python --> creating a dictionary --> key value pair --> key is the the value in the input list and the corresponsing value is its index position in the list

"""

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
      num_map = {} ##creating the hashmap
      k = 0
      ## iterating through the list only one time
      #while iterating over the list check if the target - current value is present in the dictionary - this is a smart logic instead of using addition and comparing
      for i in nums: 
          if (target - i) in num_map: 
              return [num_map[target-i], num_map[i]]
          num_map[i] = k
          k+=1

      return None
