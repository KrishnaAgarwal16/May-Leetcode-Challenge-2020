class Solution(object):
    def checkStraightLine(self,coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        if len(coordinates)<=2:
            return True
        if len(coordinates)>2:
            numo=(coordinates[1][1]-coordinates[0][1])
            deno=(coordinates[1][0]-coordinates[0][0])
            x1=coordinates[0][0]
            y1=coordinates[0][1]
            for i in range(2,len(coordinates)):
                x3 = coordinates[i][0]
                y3 = coordinates[i][1]
                if (numo*(x3-x1))!= (deno*(y3-y1)):
                    return False
                
            return True
           
