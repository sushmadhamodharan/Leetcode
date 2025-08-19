# Create a dictionary structure of possible combinations
# Use while loop and try to eliminate 2 sequence at a time and then go for 1

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
                     "IV":4, "IX":9, "XL": 40, "XC":90, "CD": 400, 
                     "CM": 900, "I":1, "V": 5, "X": 10, "L": 50, "C": 100,
                     "D": 500, "M": 1000
                    }
        i = 0
        num = 0
        while i<len(s):
            if s[i: i+2] in roman_map:
                num += roman_map[s[i: i+2]]
                i+=2
            else:
                num += roman_map[s[i]]
                i+=1
        return num
