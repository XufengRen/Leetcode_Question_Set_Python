"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # key is the node in olld list, value is the new node
        dic={}
        pointer1=head
        ans=Node(0)
        p3=ans
        while pointer1:
            dic[pointer1]=Node(pointer1.val)
            pointer1=pointer1.next
        p2=head
        while p2:
            dic[p2].random=dic[p2.random] if p2.random else None
            p3.next=dic[p2]
            p3=p3.next
            p2=p2.next
        return ans.next
