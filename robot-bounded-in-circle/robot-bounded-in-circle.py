class Solution:
    
    #north -> west -> south -> east
    # 0,1     -1, 0   0, -1   1, 0       
    def isRobotBounded(self, instructions: str) -> bool:
        x_pos = 0
        y_pos = 0
        dir = (0,1) # x = 1-> east, -1 -> west, y = 1 -> north, y = -1 -> south 
        for i in instructions:
            if i == 'G':
                x_pos+= int(dir[0])
                y_pos+= int(dir[1])
            elif i == 'L':
                if dir == (0,1):
                    dir = (-1,0)
                elif dir == (-1,0):
                    dir = (0, -1)
                elif dir == (0, -1):
                    dir = (1, 0)
                else:
                    dir = (0, 1)
            else:
                if dir == (0,1):
                    dir = (1,0)
                elif dir == (1,0):
                    dir = (0, -1)
                elif dir == (0, -1):
                    dir = (-1, 0)
                else:
                    dir = (0, 1)
       
        if dir != (0,1) or x_pos == y_pos == 0:
            return True
        else:
            return False