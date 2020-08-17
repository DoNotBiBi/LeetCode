# 题目描述：
# 删除排序数组中的重复项
# 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
#
# 不要使用额外的数组空间，你必须在原地修改输入数组
# 并在使用O(1)额外空间的条件下完成。
# 示例
# 1:给定数组nums = [1, 1, 2],函数应该返回新的长度2, 并且原数组nums的前两个元素被修改为1, 2。
# 你不需要考虑数组中超出新长度后面的元素。
# 示例
# 2:给定nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],函数应该返回新的长度5, 并且原数组nums的前五个元素被修改为0, 1, 2, 3, 4。
# 你不需要考虑数组中超出新长度后面的元素。


# 题目描述
# 合并两个有序链表
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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

# 判断回文串（只考虑数字和字母不管大小写，空字符串也是）
class Solution:
    def removeDuplicates(self, nums):
        nums[:] = sorted(list(set(nums)))  # 此事nums数组重新赋值
        return len(nums)

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        pre_l = ListNode()
        new_head = pre_l

        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                pre_l.next = l1
                pre_l = l1
                l1 = l1.next
            else:
                pre_l.next = l2
                pre_l = l2
                l2 = l2.next
        if l1 is not None:
            pre_l.next = l1
        if l2 is not None:
            pre_l.next = l2
        return new_head.next

    def singleNumber(self, list_nums) -> int:
        a: int = 0
        for num in list_nums:
            a = a ^ num
        return a

    def isPalindrome(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(filter(str.isalnum, s)).lower()  # filter函数用来过滤序列(字符串可以当做序列)
                                                     # 最后返回的是迭代器对象list()可以直接转化
        return s == s[::-1]




if __name__ == '__main__':
    cls_s = Solution()
    nums = 'aba,aba'
    print(cls_s.isPalindrome(nums))
