# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
# 有效字符串需满足：
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。
#
# 示例 1:
#
# 输入: "()"
# 输出: true
# 示例2:
#
# 输入: "()[]{}"
# 输出: true
# 示例3:
#
# 输入: "(]"
# 输出: false
# 示例4:
#
# 输入: "([)]"
# 输出: false
# 示例5:
#
# 输入: "{[]}"
# 输出: true

class Solution:
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


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
