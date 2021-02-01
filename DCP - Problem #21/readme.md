### Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

#### For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.


`Approach::-`

- Sort the intervals based on their starting time
- let 1 denotes `start` of the interval and 0 denotes `end` of the interval
- now traverse the modified array, maintain a `count` which will store count of all the interval who have started only,
- update `ans=max(ans,count)`
- if current interval has `end` than do `count-=1` else `count+=1`

### LOOK AT THE .PY FILE.
