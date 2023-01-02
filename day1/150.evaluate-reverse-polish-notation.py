#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = {
                '+' : lambda x, y : x + y,
                '-' : lambda x, y : x - y,
                '*' : lambda x, y : x * y,
                '/' : lambda x, y : int(x / y)
            }
        n = []
        for i in tokens:
            if i not in "+-*/":
                n.append(int(i))
            else:
                q = n.pop()
                p = n.pop()
                n.append(op[i](p, q))

        return int(n[-1])
# @lc code=end

