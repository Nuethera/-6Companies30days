#
# @lc app=leetcode id=166 lang=python3
#
# [166] Fraction to Recurring Decimal
#

# @lc code=start
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator//denominator)
        sign = '' if numerator * denominator >= 0 else '-'
        n = abs(numerator)
        d=abs(denominator)
        res = sign + str(n//d) + "."
        n = n%d
        part = ""
        i=0
        m={n:i}
        while n%d:
            n *= 10
            i+=1
            rem = n%d
            part += str(n//d)
            if rem in m:
                part = part[:m[rem]] + '(' + part[m[rem]:]+')'
                return res+part
            m[rem] = i
            n = rem
        return res+part
        
# @lc code=end

