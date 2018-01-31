import random

def getUserQuestion():
	user_question = input("What is your question?")
	while user_question != 'quit':
    	if user_question[-1] != "?":
        	print("I'm sorry, I can only answer questions.")
    	else:
			response = returnAnswer()
			print(response)
		user_question = input("What is your question? (type 'quit' to exit) ")


def returnAnswer():
	possible_answers = []
	possible_answers.append("It is certain")
	possible_answers.append("It is decidedly so")
	possible_answers.append("Without a doubt")
	possible_answers.append("Yes definitely")
	possible_answers.append("You may rely on it")
	possible_answers.append("As I see it, yes")
	possible_answers.append("Most likely")
	possible_answers.append("Outlook good")
	possible_answers.append("Yes")
	possible_answers.append("Signs point to yes")
	possible_answers.append("Reply hazy try again")
	possible_answers.append("Ask again later")
	possible_answers.append("Better not tell you now")
	possible_answers.append("Cannot predict now")
	possible_answers.append("Concentrate and ask again")
	possible_answers.append("Don't count on it")
	possible_answers.append("My reply is no")
	possible_answers.append("My sources say no")
	possible_answers.append("Outlook not so good")
	possible_answers.append("Very doubtful")

	#pick random index between 0 and 19
	return possible_answers[random.randint(1,20)-1]


getUserQuestion()

