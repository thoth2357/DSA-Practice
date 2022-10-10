"""
You're given a list of n integers arr, which represent elements in a queue (in order from front to back). You're also given an integer x, and must perform x iterations of the following 3-step process:

Pop x elements from the front of queue (or, if it contains fewer than x elements, pop all of them)
Of the elements that were popped, find the one with the largest value (if there are multiple such elements, take the one which had been popped the earliest), and remove it
For each one of the remaining elements that were popped (in the order they had been popped), decrement its value by 1 if it's positive (otherwise, if its value is 0, then it's left unchanged), and then add it back to the queue
Compute a list of x integers output, the ith of which is the 1-based index in the original array of the element which had been removed in step 2 during the ith iteration.
Signature
int[] findPositions(int[] arr, int x)
Input
x is in the range [1, 316].
n is in the range [x, x*x].
Each value arr[i] is in the range [1, x].

Output
Return a list of x integers output, as described above.
Example
n = 6
arr = [1, 2, 2, 3, 4, 5]
x = 5
output = [5, 6, 4, 1, 2]
The initial queue is [1, 2, 2, 3, 4, 5] (from front to back).
"""

from collections import deque

def queueRemoval(arr,x):
    q = deque([k for k in enumerate(arr)])
    
    out = []
    for i in range(x):
        g = 0
        max_number = float('-inf')
        pop_left = []
        while g < x and q:
            item_popped = q.popleft()
            if item_popped[1] > max_number:
                max_number = item_popped[1]
                max_index = item_popped[0]
            pop_left.append(item_popped)
            g += 1
        for h in pop_left:
            if h[0] != max_index:
                q.append((h[0],max(0,h[1]-1)))
        out.append(max_index+1)
    return out
    

arr=[1,2,2,3,4,5]
x = 5
print(queueRemoval(arr, x))

    