# Write your count_multi_char_x function here:
def count_multi_char_x(word, x):
    number = word.count(x)
    return number
  
# Uncomment these function calls to test your function:
#print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1