# def capitalize(sentence):
#     for i in range(0, len(sentence)):
#         if i == 0:
#             sentence = sentence[i].upper() + sentence[1:]
#         elif sentence[i] == '.' and i != len(sentence)-1:
#             sentence = sentence[:i+2] + sentence[i+2].upper() + sentence[i+3:]
#     return sentence

# def main():
#     sentence = input('Enter sentence to be capitalized:')
#     print(capitalize(sentence))

# # Call the main function.
# if __name__ == '__main__':
#     main()

def capitalize(sentence):
    myList = list(sentence)
    myList[0] = myList[0].upper()
    for i in range(len(myList)-1):
        if myList[i] == "." or myList[i] == "?" and i != len(myList)-1:
                myList[i+2] = myList[i+2].upper()
    newSentence = ''.join(myList)
    return newSentence   
          
        
    # words = sentence.split()
    # for i, word in enumerate(words):
    #     if word.lower() in ["hi,", "my", "what", "Joe"]:
    #         words[i] = word.capitalize()
    #     else:
    #         words[i] = word.lower()
    # return ' '.join(words)
    print(count)

def main():
    sentence = input("Enter the sentence to be capitalized:")
    display_sentence = capitalize(sentence)
    print(display_sentence)
    
main()