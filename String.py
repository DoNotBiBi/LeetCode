class Solution:
    def isPalindrome(self, s: str) -> bool:
            """
            :type s: str
            :rtype: bool
            """
            s = ''.join(filter(str.isalnum, s)).lower()  # filter函数用来过滤序列(字符串可以当做序列)
                                                        # 最后返回的是迭代器对象list()可以直接转化
            return s == s[::-1]
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
            res = res + x[i]
        return res

    def longestCommonPrefix3(self, strs) -> str:
        s = ""
        for i in zip(*strs):
            if len(set(i)) == 1:
                s += i[0]
            else:
                break
        return s