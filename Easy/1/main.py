class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 1.题目描述：
    # 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
    # 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
    #
    # 示例:
    # 给定 nums = [2, 7, 11, 15], target = 9
    # 因为 nums[0] + nums[1] = 2 + 7 = 9
    # 所以返回 [0, 1]
    def twoSum(self, nums, target: int):
        """
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
        """
        hashmap = {}  # 首先要声明一下其实哈希表
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index
        return None

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

    # 最长公共子串
    def longestCommonPrefix(self, strs) -> str:
        """
        :param self:
        :param strs: List[List[str]]
        :return: str
        """
        if not strs:
            return ""
        s1 = min(strs)
        s2 = max(strs)
        for i, x in enumerate(s1):
            if x != s2[i]:
                return s2[:i]
        return s1

    def longestCommonPrefix2(self, strs) -> str:
        if not strs:
            return ""
        ss = list(map(set, zip(*strs)))
        res = ""
        for i, x in enumerate(ss):
            x = list(x)
            if len(x) > 1:
                break
            res = res + x[0]
        return res

    def longestCommonPrefix3(self, strs) -> str:
        s = ""
        for i in zip(*strs):
            if len(set(i)) == 1:
                s += i[0]
            else:
                break
        return s


if __name__ == '__main__':
    s = "helllo"
    print(list(s))
