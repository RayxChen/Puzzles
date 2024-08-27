from functools import cache

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n):
        # Catalan number
        # 1/(n+1) C(2n, n)

        # dfs:= list of unique BST [List[List]]
        @cache
        def dfs(l, r):
            if l > r:
                return [None]
            res = []
            for i in range(l, r+1):
                left = dfs(l, i-1) # list of list
                right = dfs(i+1, r)
                for a in left:
                    for b in right:
                        root = TreeNode(i, a, b)
                        res.append(root)
            return res
        
        return dfs(1, n)

