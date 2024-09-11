import json

with open('files/bonus_5.json', 'r') as file:
    content = file.read()


data = json.loads(content)
score = 0

for index, question in enumerate(data):
    print(question['question_text'])
    for index, answer in enumerate(question['answers']):
        print(str(index + 1), "-", answer)

    user_answer = int(input("What is your answer? -> "))
    question["user_answer"] = user_answer


for index, question in enumerate(data):

    if question['user_answer'] == question['correct_answer']:
        score = score + 1
        result = "correct answer"
    else:
        result = "wrong answer"

    message = f"Question {index + 1}: You had a {result}!"\
                f" Your answer was {question['user_answer']}."\
                f" The correct answer was {question['correct_answer']}"

    print(message)


print(f"\nThank you for playing! Your final score is {score}")

