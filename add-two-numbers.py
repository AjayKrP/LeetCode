# https://leetcode.com/problems/add-two-numbers/solution/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode: 
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        while l1 or l2 or carry: # O(n)
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            carry, out = divmod(val1+val2 + carry, 10)

            curr.next = ListNode(out)
            curr = curr.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
        return dummyHead.next
