# Provided is a string saved to the variable name sentence. Split the string into a list of words, then create a dictionary that contains each word and the number of times it occurs. Save this dictionary to the variable name word_counts.

sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."
lst = sentence.split()
word_counts = {}
for a in lst:
    if a not in word_counts:
        word_counts[a] = 0
        
        
    word_counts[a] += 1



# Create a dictionary called char_d from the string stri, so that the key is a character and the value is how many times it occurs.

stri = "what can I do"
char_d = {}
for i in stri:
    if i not in char_d:
        char_d[i] = 0
        
    char_d[i] += 1 
