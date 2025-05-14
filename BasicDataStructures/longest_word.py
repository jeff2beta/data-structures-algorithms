# Write a function, longest_word, that takes in a sentence string as 
# an argument. The function should return the longest word in the 
# sentence. If there is a tie, return the word that occurs later in 
# the sentence. You can assume that the sentence is non-empty.

def longest_word(sentence):
  words = sentence.split()
  long_word = words[0]
  for word in words:
    if len(word) >= len(long_word):
      long_word = word

  print(long_word)
  

longest_word("what a wonderful world") # -> "wonderful"
longest_word("have a nice day") # -> "nice"
longest_word("the quick brown fox jumped over the lazy dog") # -> "jumped"
longest_word("who did eat the ham") # -> "ham"
longest_word("potato") # -> "potato"
