# Write your substring_between_letters function here:
def substring_between_letters(word, start, end):
  init_index = word.find(start)
  final_index = word.find(end)
  if init_index == - 1 or final_index == - 1:
    return word
  else:
    return word[init_index + 1: final_index]

# Uncomment these function calls to test your function:
#print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"