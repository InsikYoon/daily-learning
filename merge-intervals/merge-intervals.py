class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        a = []
        intervals.sort()
        minval = intervals[0][0]
        maxval = intervals[0][1]
        for i,j in intervals:
            if( maxval < i ):
                a.append((minval,maxval))
                minval = i
                maxval = j
            elif ( maxval == i):
                maxval = j
            else:
                if( maxval < j):
                    maxval = j
        
        if (minval, maxval) not in a:
            a.append((minval, maxval))
        return a
            
            