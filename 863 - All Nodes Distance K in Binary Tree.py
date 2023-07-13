# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def add_parent(cur, parent):
            if cur:
                cur.parent = parent
                add_parent(cur.left, cur)
                add_parent(cur.right, cur)

        add_parent(root, None)

        answer = []
        visited = set()
        
        def dfs(cur, distance):
            if (not cur) or (cur in visited):
                return
            visited.add(cur)
            if distance == 0:
                answer.append(cur.val)
                return

            dfs(cur.parent, distance - 1)
            dfs(cur.left, distance - 1)
            dfs(cur.right, distance - 1)

        dfs(target, k)

        return answer



        # Implementing parent pointers
        # cannot access parents manually - add a pointer to the parent
        # when a pointer reaches the depth - comes backward - at that time are the parent pointers implemented
        # to keep track of visited nodes hash set is used
    # use dfs to calculate distance and find the result nodes
