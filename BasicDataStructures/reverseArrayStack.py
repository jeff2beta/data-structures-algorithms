# Suppose you are given an array, A, containing n numbers in order. 
# Describe an efficient algorithm for reversing the order 
# of the numbers in A using a single for-loop that indexes through the 
# cells of A, to insert each element into a stack, and then another 
# for-loop that removes the elements from the stack and puts them back
# into A in reverse order. What is the running time of this algorithm?

def reverseArrayStack(A):
    stack = []

    # Push all items onto the stack
    for item in A:
        stack.append(item)

    # Pop from the stack to reverse the array in place
    for i in range(len(A)):
        A[i] = stack.pop()

    return A

A = [1,2,3,4,5,6,7]
print(reverseArrayStack(A)) # Output: [7, 6, 5, 4, 3, 2, 1]


# Time = O(n)
# Space = O(n)