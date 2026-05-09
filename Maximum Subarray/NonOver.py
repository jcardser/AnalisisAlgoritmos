class Solution:
    #Tiempo O(nlog n)
    #Espcio(1)
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        print(intervals)
        removed, previous_end = 0, intervals[0][1]
        for i in range(1, len(intervals)):
            if previous_end > intervals[i][0]:
                removed += 1
            else:
                previous_end = intervals[i][1]
        return removedﬁ
