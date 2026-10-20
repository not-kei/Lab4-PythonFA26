#Olivia Dodds
#Python FA2026
#Due: October 22
#Lab 4: Pirate
#Program takes a sentence from the user and replaces specific words with pirate equivalents

#gets sentence from user
sentence = input("Enter a sentence to be translated into pirate: ")
sentence = sentence.lower()

#translates sentence into pirate speak by replacing certain words with pirate equivalents
def toPirate(sentence):
    pirate_sentence = sentence.replace("hello", "avast")
    pirate_sentence = pirate_sentence.replace("excuse", "arrr")

    malePeople = ["sir", "boy", "man"]

    for person in malePeople:
        pirate_sentence = pirate_sentence.replace(person, "matey")

    femalePeople = ["madam", "woman"]
    for person in femalePeople:
        pirate_sentence = pirate_sentence.replace(person, "proud beauty")
        
    pirate_sentence = pirate_sentence.replace("officer", "foul blaggart")
    pirate_sentence = pirate_sentence.replace("the", "th'")
    pirate_sentence = pirate_sentence.replace("my", "me")
    pirate_sentence = pirate_sentence.replace("you", "ye")
    pirate_sentence = pirate_sentence.replace("your", "yer")
    pirate_sentence = pirate_sentence.replace("is", "be")
    pirate_sentence = pirate_sentence.replace("are", "be")
    pirate_sentence = pirate_sentence.replace("kitchen", "galley")
    pirate_sentence = pirate_sentence.replace("hotel", "fleabag inn")
#Note: Some words may have parts replaced that are not intended to be replaced. For example, "the" will be replaced in "there".


#returns the translated pirate sentence
    return pirate_sentence

#prints the translated pirate sentence
print(toPirate(sentence))   