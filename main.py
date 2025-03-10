from SentenceReadingAgent import SentenceReadingAgent

def test():
    #This will test your SentenceReadingAgent
	#with nine initial test cases.

    test_agent = SentenceReadingAgent()

    sentence_1 = "Ada brought a short note to Irene."
    question_1 = "Who brought the note?"
    question_2 = "What did Ada bring?"
    question_3 = "Who did Ada bring the note to?"
    question_4 = "How long was the note?"

    sentence_2 = "David and Lucy walk one mile to go to school every day at 8:00AM when there is no snow."
    question_5 = "Who does Lucy go to school with?"
    question_6 = "Where do David and Lucy go?"
    question_7 = "How far do David and Lucy walk?"
    question_8 = "How do David and Lucy get to school?"
    question_9 = "At what time do David and Lucy walk to school?"

    sentence_3 = "There are one hundred adults in that city."
    question_10 = "How many adults are in this city?"

    sentence_4 = "Give us all your money."
    question_11 = "Who should you give your money to?"

    sentence_5 = "It will snow soon."
    question_12 = "When will it snow?"

    sentence_6 = "The blue bird will sing in the morning."
    question_13 = "What will sing in the morning?"

    sentence_7= "The white dog and the blue horse play together."
    question_14 = "What color is the horse?"

    sentence_8 = "The island is east of the city."
    question_15= "What is east of the city?"

    sentence_9 = "Their children are in school."
    question_16 = "Who is in school?"

    sentence_10 = "This tree came from the island."
    question_17 = "Where did the tree come from?"

    print(test_agent.solve(sentence_1, question_1))  # "Ada"
    print(test_agent.solve(sentence_1, question_2))  # "note" or "a note"
    print(test_agent.solve(sentence_1, question_3))  # "Irene"
    print(test_agent.solve(sentence_1, question_4))  # "short"

    print(test_agent.solve(sentence_2, question_5))  # "David"
    print(test_agent.solve(sentence_2, question_6))  # "school"
    print(test_agent.solve(sentence_2, question_7))  # "mile" or "a mile"
    print(test_agent.solve(sentence_2, question_8))  # "walk"
    print(test_agent.solve(sentence_2, question_9))  # "8:00AM"

    print(test_agent.solve(sentence_3, question_10))
    print(test_agent.solve(sentence_4, question_11))
    print(test_agent.solve(sentence_5, question_12))
    print(test_agent.solve(sentence_6, question_13))
    print(test_agent.solve(sentence_7, question_14))
    print(test_agent.solve(sentence_8, question_15))
    print(test_agent.solve(sentence_9, question_16))
    print(test_agent.solve(sentence_10, question_17))

if __name__ == "__main__":
    test()