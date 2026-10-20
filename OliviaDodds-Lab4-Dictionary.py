#Olivia Dodds
#Python FA2026
#Due: October 22
#Lab 4: Dictionary
#Program creates a dictionary of names and scores, updates and deletes entries, and calculates the average score.


#names and scores of students
names = ['Joe', 'Tom', 'Barb', 'Sue', 'Sally']
scores = [10, 23, 13, 18, 12]

#create the dictionary of names and scores
def makeDictionary(names, scores):
    scoreDict = {}

    for i in range(len(names)):
        scoreDict[names[i]] = scores[i]

    return scoreDict

scoreDict = makeDictionary(names, scores)

#printing the dictionary of names and scores
print("The dictionary of names and scores is: ", scoreDict)

#printing the score for Barb
print("The score for Barb is: ", scoreDict['Barb'])

#updating the score for John and printing the dictionary
scoreDict['John'] = 19
print("The dictionary of names and scores after adding John is: ", scoreDict)

#creating a sorted list of all the scores in scoreDict
sortedScores = sorted(scoreDict.values())
print("The sorted list of scores is: ", sortedScores)

#finds the average of all the scores in scoreDict
def averageScore(scoreDict):
    #adds all the scores in scoreDict and divides by the number of scores to find the average
    total = sum(scoreDict.values())
    average = total / len(scoreDict)
    return average

# Calculate and print the average score
average = averageScore(scoreDict)
print("The average score is: ", average)

#updating the score for Sally and printing the dictionary
scoreDict['Sally'] = 13
print("The dictionary of names and scores after updating Sally's score is: ", scoreDict)

#deleting Tom and his score from scoreDict and printing the dictionary
del scoreDict['Tom']
print("The dictionary of names and scores after deleting Tom is: ", scoreDict)