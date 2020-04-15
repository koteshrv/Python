from Question import Question

question_prompts = [
    "What is the colour of the sky?\n(a) Blue\n(b) Green\n(c) Yellow\n\n",
    "What is the colour of the Banana?\n(a) Blue\n(b) Green\n(c) Yellow\n\n",
    "What is the colour of a leaf?\n(a) Blue\n(b) Green\n(c) Yellow\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")


run_test(questions)
