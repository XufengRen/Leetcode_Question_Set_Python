class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack=[]
        parsed=path.split('/')
        for ele in parsed:
            if ele =='' or ele =='.':
                continue
            if ele=='..':
                if len(stack)>0:
                    stack.pop(-1)
            else:
                stack.append(ele)
        
        ans='/'
        for ele in stack[0:-1]:
            ans+=ele+'/'
        if len(stack)>0:
            ans+=stack[-1]
        return ans
