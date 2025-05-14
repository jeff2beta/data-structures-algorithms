# Write a function, pairs, that takes in a list as an argument. 
# The function should return a list containing all unique pairs of 
# elements. You may return the pairs in any order and the order of 
# elements within a single pair does not matter. You can assume that 
# the input list contains unique elements.

def pairs(elements):
  result = []

  for i in range(len(elements)):
    for j in range(i + 1, len(elements)):
      pair = [elements[i], elements[j]]
      result.append(pair)

  print(result) 

pairs(["a", "b", "c"]) # ->
# [
#    ["a", "b"],
#    ["a", "c"],
#    ["b", "c"]
# ]

pairs(["a", "b", "c", "d"]) # ->
# [
#    ["a", "b"],
#    ["a", "c"],
#    ["a", "d"],
#    ["b", "c"],
#    ["b", "d"],
#    ["c", "d"]
# ]
