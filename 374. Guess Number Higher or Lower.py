# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # pick -> computer picks
        # num -> user guesses
        # we will call guess api 
        # -> pass the number use guessed 
        # -> pass p
        # -> guess api return -1/ 1/ 0

        left, right = 1, n
        
        while left <= right:
            num = (left + right) // 2  
            response = guess(num)

            if response == 0:
                return num
            elif response == -1:
                right = num - 1
            else:
                left = num + 1
