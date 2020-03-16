# Write code to find out how many lines are in the file emotion_words.txt as shown above. Save this value to the variable num_lines. Do not use the len method.

file = open("emotion_word.txt","r")
count = 0
for aline in file.readlines():
    count += 1
num_lines = count
