        ans=ListNode(0)
        p=ans
        off=0
        while l1 or l2:
            
            if l1:
                off+=l1.val
                l1=l1.next
                
            if l2:
                off+=l2.val
                l2=l2.next
                
            p.next=ListNode(off%10)
            p=p.next
            off//=10
        
        if off>0:
            p.next=ListNode(off)
        
        return ans.next
