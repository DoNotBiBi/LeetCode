class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution: # 解决方案的类
    # 给定一个二叉树，返回其节点值自底向上的层次遍历。
    # （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
    def levelOrderBottom(self, root: TreeNode):
        if not root:
            return []
        queue = []
        cur = [root]
        while cur:
            cur_val = []
            next_node = []
            for x in cur:
                cur_val.append(x.val)
                if x.left:
                    next_node.append(x.left)
                if x.right:
                    next_node.append(x.right)
            cur = next_node
            queue.insert(0, cur_val)
        return queue
    # 题目描述
    # 给定一个二叉树，找出其最大深度。
    #
    # 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
    #
    # 说明: 叶子节点是指没有子节点的节点。
    # Definition for a binary tree node.
    def maxDepth(self, root: TreeNode) -> int:
        def top_down(node, h):
            return h if node is None else max(top_down(node.left, h + 1), top_down(node.right, h + 1))

        return top_down(root, 0)

    # 求树的最小深度
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans = 0
        if not root.left and not root.right:  # 叶子节点
            ans = 1
        elif root.left and root.right:  # 左右子树均不为空
            ans = min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        elif root.left:  # 左子树不为空 & 右子树为空
            ans = self.minDepth(root.left) + 1
        else:  # 左子树为空 & 右子树不为空
            ans = self.minDepth(root.right) + 1
        return ans
    # 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
    # 要求:左右两个子树的高度差的绝对值不超过1。
    def sortedArrayToBST(self, nums) -> TreeNode:
        if nums:
            m = len(nums) // 2
            r = TreeNode(nums[m])
            r.left, r.right = map(self.sortedArrayToBST, [nums[:m], nums[m + 1:]])
            return r

    def sortedArrayToBST2(self, nums2) -> TreeNode:
        if len(nums2) == 0:
            return None
        else:
            root = TreeNode(nums2[(len(nums2) // 2)])
            root.left = self.sortedArrayToBST(nums2[0:(len(nums2) // 2)])
            root.right = self.sortedArrayToBST(nums2[(len(nums2) // 2 + 1):len(nums2) + 1])
        return root
    # 判断是不是平衡树
    def isBalanced(self, root: TreeNode) -> bool:
        self.res = True
        def helper(root):
            if not root:
                return 0

            left = helper(root.left) + 1
            right = helper(root.right) + 1

            if abs(right - left) > 1:
                self.res = False
            return max(left, right)

        helper(root)
        return self.res
    
     