# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        dp = [[] for _ in range(n + 1)]
        # Base Case - return none when no BSTs can be constructed
        dp[0].append(None)

        for numberOfNodes in range(1, n + 1):
            for i in range(1, numberOfNodes + 1):
                off_set = numberOfNodes - i
                for left in dp[i - 1]:
                    for right in dp[off_set]:
                        root = TreeNode(i , left, self.clone(right, i))
                        dp[numberOfNodes].append(root)

        return dp[n]

    def clone(self, node,  offset):
        if not node:
            return None
        cloned_node = TreeNode(node.val + offset)
        cloned_node.left = self.clone(node.left, offset)
        cloned_node.right = self.clone(node.right, offset)
        return cloned_node
    