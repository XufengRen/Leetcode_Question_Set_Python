# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        p=head
        l=[]
        while p:
            l.append(p.val)
            p=p.next
        i=0
        while i<len(l)-1:
            l[i],l[i+1]=l[i+1],l[i]
            i+=2
        ans=ListNode(0)
        p=ans
        for ele in l:
            p.next=ListNode(ele)
            p=p.next
        return ans.next
