class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """      
        counter=collections.Counter(s)   
        chart=[0 for i in range(10)]
        chart[0]=counter['z']
        chart[2]=counter['w']
        chart[4]=counter['u']
        chart[6]=counter['x']
        chart[8]=counter['g']
        chart[3]=counter['h']-chart[8]
        chart[5]=counter['f']-chart[4]
        chart[7]=counter['v']-chart[5]
        chart[1]=counter['o']-chart[0]-chart[2]-chart[4]
        chart[9]=counter['i']-chart[6]-chart[5]-chart[8]
        ans=''
        for i in range(10):
            ans+=str(i)*chart[i]
        return ans
