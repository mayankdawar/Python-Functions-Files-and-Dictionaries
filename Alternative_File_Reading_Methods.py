#Using the file school_prompt2.txt, find the number of characters in the file and assign that value to the variable num_char.

fil = open("school_prompt2.txt","r")
consts = fil.read()
num_char = len(consts)
fil.close()



#Find the number of lines in the file, travel_plans2.txt, and assign it to the variable num_lines.

file = open("travel_plans2.txt","r")
count = file.readlines()
num_lines = len(count)



#Create a string called first_forty that is comprised of the first 40 characters of emotion_words2.txt.

file = open("emotion_words2.txt","r")
const = file.read()
first_forty = const[:40]
