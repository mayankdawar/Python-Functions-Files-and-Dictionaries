# We have provided some synthetic (fake, semi-randomly generated) twitter data in a csv file named project_twitter_data.csv which has the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet. We have also words that express positive sentiment and negative sentiment, in the files positive_words.txt and negative_words.txt.
# Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. You will create a csv file, which contains columns for the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score for each tweet. At the end, you upload the csv file to Excel or Google Sheets, and produce a graph of the Net Score vs Number of Retweets.
# To start, define a function called strip_punctuation which takes one parameter, a string which represents a word, and removes characters considered punctuation from everywhere in the word. (Hint: remember the .replace() method for strings.)

punctuation_char = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(Str):
    for pointer in punctuation_char:
        Str = Str.replace(pointer, "")
    return Str
   
   

# Next, copy in your strip_punctuation function and define a function called get_pos which takes one parameter, a string which represents one or more sentences, and calculates how many words in the string are considered positive words. Use the list, positive_words to determine what words will count as positive. The function should return a positive integer - how many occurrences there are of positive words in the text. Note that all of the words in positive_words are lower cased, so you’ll need to convert all the words in the input string to lower case as well.

punctuation_char = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

def strip_punctuation(Str):
    for pointer in punctuation_char:
        Str = Str.replace(pointer, "")
    return Str

def get_pos(string):
    newStr = strip_punctuation(string)
    lstNewStr = newStr.split()
    counter = 0
    for word in lstNewStr:
        word = word.lower()
        for pointer in positive_words:
       #     lowerString = pointer.lower()
    
            if word == pointer:
                counter += 1
    return counter
    
            

    




# Next, copy in your strip_punctuation function and define a function called get_neg which takes one parameter, a string which represents one or more sentences, and calculates how many words in the string are considered negative words. Use the list, negative_words to determine what words will count as negative. The function should return a positive integer - how many occurrences there are of negative words in the text. Note that all of the words in negative_words are lower cased, so you’ll need to convert all the words in the input string to lower case as well.

punctuation_char = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
           
def strip_punctuation(Str):
    for pointer in punctuation_char:
        Str = Str.replace(pointer, "")
    return Str

def get_pos(Str):
    newStr = strip_punctuation(Str)
    lstNewStr = newStr.split()
    counter = 0
    for word in lstNewStr:
        word = word.lower()
        for pointer in positive_words:  
            if word == pointer:
                counter += 1
    return counter

def get_neg(Str):
    newStr = strip_punctuation(Str)
    lstNewStr = newStr.split()
    counter = 0
    for word in lstNewStr:
        word = word.lower()
        for pointer in negative_words:  
            if word == pointer:
                counter += 1
    return counter





    
# Finally, copy in your previous functions and write code that opens the file project_twitter_data.csv which has the fake generated twitter data (the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet). Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. Copy the code from the code windows above, and put that in the top of this code window. Now, you will write code to create a csv file called resulting_data.csv, which contains the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score (how positive or negative the text is overall) for each tweet. The file should have those headers in that order. Remember that there is another component to this project. You will upload the csv file to Excel or Google Sheets and produce a graph of the Net Score vs Number of Retweets. Check Coursera for that portion of the assignment, if you’re accessing this textbook from Coursera.

import sys
sys.setExecutionLimit(500000)
punctuation_char = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(Str):
    for pointer in punctuation_char:
        Str = Str.replace(pointer, "")
    return Str

def get_pos(Str):
    newStr = strip_punctuation(Str)
    lstNewStr = newStr.split()
    counter = 0
    for word in lstNewStr:
        word = word.lower()
        for pointer in positive_words: 
            
            if word == pointer:
                counter += 1
    return counter

def get_neg(Str):
    newStr = strip_punctuation(Str)
    lstNewStr = newStr.split()
    counter = 0
    for word in lstNewStr:
        word = word.lower()
        for pointer in negative_words:  
            if pointer == word:
                counter += 1
    return counter            

TwitterFile = open("project_twitter_data.csv","r")
resultFile = open("resulting_data.csv","w")
resultFile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
resultFile.write("\n")
linesTwitter = TwitterFile.readlines()
noHeader = linesTwitter.pop(0)
for lines in linesTwitter:
    lst = lines.strip().split(',')
    resultFile.write("{}, {}, {}, {}, {}".format(lst[1], lst[2], get_pos(lst[0]), get_neg(lst[0]), (get_pos(lst[0])-get_neg(lst[0]))))    
    resultFile.write("\n")
        


