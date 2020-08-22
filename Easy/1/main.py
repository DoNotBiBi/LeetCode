# 1.题目描述：
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
#
# 示例:
# 给定 nums = [2, 7, 11, 15], target = 9
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]

class Solution:
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
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def top_down(node, h):
            return h if node is None else max(top_down(node.left, h + 1), top_down(node.right, h + 1))
        return top_down(root, 0)

if __name__ == '__main__':
    s = Solution()
    nums = [2, 7, 11, 15]
    target = 18
    print(s.twoSum(nums, target))
