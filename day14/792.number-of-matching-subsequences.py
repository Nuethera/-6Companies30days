#
# @lc app=leetcode id=792 lang=python3
#
# [792] Number of Matching Subsequences
#

# @lc code=start
class Node:
    def __init__(self,word):
        self.word = word
        self.ind = 0


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        buckets = defaultdict(list)
        for word in words:
            startingChar = word[0]
            buckets[startingChar].append(Node(word))
        
        ans = 0
        for c in s:
            currBucket = buckets[c]
            buckets[c] = []
            for node in currBucket:
                node.ind += 1
                if node.ind == len(node.word):
                    ans += 1
                else:
                    buckets[node.word[node.ind]].append(node)


        return ans
# @lc code=end

