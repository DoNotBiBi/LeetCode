# 题目描述
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
#
# 示例1:
#
# 输入: 123
# 输出: 321
# 示例2:
#
# 输入: -123
# 输出: -321
# 示例 3:
#
# 输入: 120
# 输出: 21
# 注意:
#
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为[−2的31次方, 2的31次方− 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def reverse(self, x: int) -> int:
        if -2 ** 31 <= x <= 2 ** 31 - 1:
            str_x = str(x).replace('-', '')
            str_x = int(str_x[::-1])
            if str_x < 2 ** 31:
                if x >= 0:
                    return str_x
                else:
                    return -str_x
            else:
                return 0  # 确保转化的数字在一定范围内 边界考虑
        else:
            return -1

    # 杨辉三角
    def generate(self, numRows: int):
        if numRows == 0: return []
        res = [[1]]
        while len(res) < numRows:
            newRow = [a + b for a, b in zip([0] + res[-1], res[-1] + [0])]
            res.append(newRow)
        return res

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




if __name__ == '__main__':
    s = Solution()
    x = 7
    print(s.generate(x))
