class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
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
    # 找公共结点，并输出对应的值
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ha, hb = headA, headB
        while ha!=hb:
            ha=ha.next if ha else headB
            hb=hb.next if hb else headA
        return ha