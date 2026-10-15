#Olivia Dodds
#Python FA2026
#Due: October 22
#Lab 4: Words
#Program takes a sentence from the user and counts the number of words in the sentence

#gets sentence from user
sentence = input("Enter a sentence to count the number of words: ")

#figures out how many words are in the sentence based on the number of spaces in the sentence
#function also checks to make sure that there are no extra spaces in the sentence
def countWords(sentence):
    #finds the index of the last character in the sentence
    index = len(sentence) - 1

    #keeps track of the number of words in the sentence
    wordCount = 0

    #loops through the sentence and counts the number of words in the sentence
    for i in range(len(sentence)):
        #if the first character in the sentence is not a space, add one to the word count
        if sentence[i] == " " and sentence[i - 1] != " ":
            wordCount += 1

    return wordCount

#if no words are in the sentence, print a message saying so. Otherwise, print the number of words in the sentence.
if countWords(sentence) == 0:
    print("There are no words in the sentence.")
else:
    print("The number of words in the sentence is: ", countWords(sentence))