def getUserQuestion():
    user_question = input("What is your question?")
    return user_question

question = getUserQuestion()
while question != 'quit':
    if question[-1] != "?":
        print("I'm sorry, I can only answer questions.")
    question = getUserQuestion()
