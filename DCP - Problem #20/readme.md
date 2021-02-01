### Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

### For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

### In this example, assume nodes with the same value are the exact same node objects.

### Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space


`Approach::-`


- find the `longest` list, let it be `list1` with length `l1` and `list2` with length `l2`.
- now `skip=abs(l1-l2)` nodes from the longest list.
- After skipping, traverse both list simultaneously with two pointer `start1` and `start2`.
- at any moment of time, if `start1 is start2` i.e, `both addresses are same` than it will be our `intersecting node`.
