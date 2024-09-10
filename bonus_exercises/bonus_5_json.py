import json

with open('files/bonus_5.json', 'r') as file:
    content = file.read()


data = json.loads(content)

for question in data:
    print(question['question_text'])
    for index, answer in enumerate(question['answers']):
        print(str(index + 1), "-", answer)

    user_answer = int(input("What is your answer? -> "))

    if user_answer == question['correct_answer']:
        print("That is correct!")
    else:
        print("Sorry, wrong answer")


print("\nThank you for playing!")