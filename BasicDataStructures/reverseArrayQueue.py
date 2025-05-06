# Solve the previous exercise using a queue instead of stack. 
# That is, suppose you are given an array, A, containing n numbers 
# in order, as in the previous exercise. Describe an efficient 
# algorithm for reversing the order of the numbers in A using a 
# single for-loop that indexes through the cells of A, to insert each
# element into a queue, and then another for-loop that removes the 
# elements from the queue and puts them back into A in reverse order. 
# What is the running time of this algorithm?
from collections import deque

def reverseArrayQueue(A):
    queue = deque()
    # Enqueue all elements
    for item in A:
        queue.append(item)
    # Use a stack to reverse
    stack = []
    while queue:
        stack.append(queue.popleft())
    # Put back into the array in reversed order
    for i in range(len(A)):
        A[i] = stack.pop()
        
    return A

A = [1,2,3,4,5,6,7]
print(reverseArrayQueue(A))