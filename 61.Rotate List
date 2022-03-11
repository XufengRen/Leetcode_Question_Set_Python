       #First apporach: copy value from linked list to list, use it to build a new linked list
       
       #Early exit
       if not head or not head.next:
            return head
        l=[]
        ans=[]
        p=head
        while p is not None:
            l.append(p.val)
            p=p.next
        a=ListNode(0)
        p=a
        k=len(l)-k%len(l)
        for i in range(len(l)):
            p.next=ListNode(l[(i+k)%len(l)])
            p=p.next
        return a.next
        
        #Second appraoch: linked the tail to head and make the linked list into a circle, then break 
        #the circle at certain place
        #         Early exit
        if head is None or head.next is None:
            return head        
        p1=head
        n=1
        while p1.next:
            n+=1
            p1=p1.next
        p1.next=head        
        p2=head
        k=k%n
        # print(n)
        while n>k+1:
            p2=p2.next
            n-=1
        # print(n,k,p2.val)
        ans=p2.next
        p2.next=None
        return ans
