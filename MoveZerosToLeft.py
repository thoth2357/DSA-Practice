"""
Given an integer array, move all elements that are 0 to the left while maintaining the order of other elements in the array. 
The array has to be modified in-place. Try it yourself before reviewing the solution and explanation.
"""

def move_zeros_to_left(A):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    read = write = len(A) - 1
    while read >= 0:
        if A[read] != 0:
            A[write] = A[read]
            write -= 1
        read -= 1
    while write >= 0:
        A[write] = 0
        write -= 1
    return A

if __name__ == "__main__":
    A = [1, 10, 20, 0, 59, 63, 0, 88, 0]
    print(move_zeros_to_left(A))

