from typing import List

arr = [[1, 2], [3, 4], [5, 6], [2, 3]]
arr.sort(key=lambda x: -x[1])

print(-arr[1][1])

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: -x[1] )
        max_units = 0

        for box, unit in boxTypes:
            if truckSize >= box:
                max_units += box * unit
                truckSize -= box
            else:
                max_units += truckSize * unit
                break

        return max_units