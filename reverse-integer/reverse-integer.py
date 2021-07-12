class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        
        if x < 0:
            isNeg = 1
        else:
            isNeg = 0
        
        if( isNeg ):
            prestr = str(x)[1::]
            numstr = '-'+prestr[::-1]
        else:
            numstr = str(x)[::-1]
        
        ret = int(numstr)
        
        if( ret < -(2**31) or ret > (2**31)-1):
            ret = 0
            
        return ret
        
                    
        