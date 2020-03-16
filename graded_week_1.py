# The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary. Find the total number of characters in the file and save to the variable num.

file = open("travel_plans.txt","r")
count = file.read()
num = len(count)



# We have provided a file called emotion_words.txt that contains lines of words that describe emotions. Find the total number of words in the file and assign this value to the variable num_words.

with open ("emotion_words.txt","r") as obj:
    lst = obj.read().split();
    print(lst)
    num_words = len(lst) 



# Assign to the variable num_lines the number of lines in the file school_prompt.txt.

with open ("school_prompt.txt","r") as obj:
    count = 0;
    for i in obj.readlines():
        count += 1
    num_lines = count    
    
    
    
# Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.
with open ("school_prompt.txt","r") as obj:
    constants = obj.read()
    beginning_chars = constants[:30]



# Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.

obj = open('school_prompt.txt','r')
three = []
lines = obj.readlines()
for i in lines:
    a = i.split()
    three.append(a[2])



# Challenge: Create a list called emotions that contains the first word of every line in emotion_words.txt.

emotions = []
with open ("emotion_words.txt","r") as obj:
    
    for i in lines:
        a = i.split()
        emotions.append(a[0])  
        
        
        
# Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.

with open ("travel_plans.txt","r") as obj:
    first_chars = obj.read(33)


# Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.

op=open('school_prompt.txt','a')
p_words=[]
lst = op.read().split()
for i in lst:
    if 'p' in i:
        p_words.append(i)




    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
