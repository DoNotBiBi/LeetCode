import math
class Solution:
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
     # 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
    # 有效字符串需满足：
    # 左括号必须用相同类型的右括号闭合。
    # 左括号必须以正确的顺序闭合。
    # 注意空字符串可被认为是有效字符串。
    # 示例 1:
    # 输入: "()"
    # 输出: true
    # 示例2:
    # 输入: "()[]{}"
    # 输出: true
    # 示例3:
    # 输入: "(]"
    # 输出: false
    # 示例4:
    # 输入: "([)]"
    # 输出: false
    # 示例5:
    # 输入: "{[]}"
    # 输出: true
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:  # 奇数长度
            return False

        d = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for char in s:
            if char in d:  # 左括号入栈
                stack.append(char)
            else:
                if not stack or d[stack.pop()] != char:  # 没入栈就出栈 或 出栈元素不匹配当前元素
                    return False

        return True if not stack else False
    # 题目描述
    # 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
    #
    # 说明：
    #
    # 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
    #
    # 示例 1:
    #
    # 输入: [2,2,1]
    # 输出: 1
    # 示例2:
    #
    # 输入: [4,1,2,1,2]
    # 输出: 4
    #
    def removeDuplicates(self, nums):
        nums[:] = sorted(list(set(nums)))  # 此事nums数组重新赋值
        return len(nums)

    

    def singleNumber(self, list_nums) -> int:
        a: int = 0
        for num in list_nums:
            a = a ^ num
        return a
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
    
    # 计数质数

    def countPrimes(self, n: int) -> int:
        d = [True] * n
        count = 0
        for i in range(2, n):
            if d[i]:
                count += 1
                for j in range(i, n, i):
                    d[j] = False
        return count

    # 厄拉多塞筛法python实现
    def countPrimes2(self, n: int) -> int:
        List = [1] * n
        if n < 3:
            return 0
        List[0], List[1] = 0, 0
        for i in range(2, int(n ** 0.5) + 1):
            if List[i] == 1:
                List[i * i:n:i] = [0] * len(List[i * i:n:i])
        return sum(List)

    # 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        a = nums[0:l - k]
        a.reverse()
        b = nums[l - k:l]
        b.reverse()
        print(a)
        print(b)
        c = a + b
        print(c)
        nums.clear()
        c.reverse()
        nums += c
    
    # 统计阶乘结果末尾0的个数  主要是看里面有多个被5整除的元素
    def trailingZeroes(self, n: int) -> int:
        return 0 if not n else self.trailingZeroes(n//5)+n//5
    
    def isPerfectSquare(self, num: int) -> bool:
        return math.sqrt(num) == int(math.sqrt(num))
        # 牛顿迭代法
        # tmp = num
        # while tmp > num / tmp:
        #     tmp = (tmp + num // tmp) // 2
        # return tmp == num / tmp
    # 统计 二进制1的个数
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count