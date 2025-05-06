# In the children's game "hot potato," a group of n children sit 
# in a circle passing an object, called the "potato," around the 
# circle (say in a clockwise direction). The children continue passing 
# the potato until a leader rings a bell, at which point the child 
# holding the potato must leave the game, and the other children 
# close up the circle. This process is then continued until there is 
# only one child remaining, who is declared the winner. Using a list, 
# describe an efficient method for implementing this game. Suppose 
# the leader always rings the bell immediately after the potato has 
# been passed k times. (Determining the last child remaining in this 
# variation of hot potato is known as the Josephus problem.) 
# What is the running time of your method in terms of n and k, 
# assuming the list is implemented with a doubly linked list? 
# What if the list is implemented with an array?

from collections import deque

def hotPotato(names, k):
    queue = deque(names)

    while len(queue) > 1:
        for _ in range(k - 1):
            queue.append(queue.popleft()) # pass the potato
        queue.popleft() # eliminate the person holding the potato

    return queue[0]

children = ["Alice", "Bob", "Charlie", "David", "Eve"]
k = 3
winner = hotPotato(children, k)
print("The winner is:", winner)