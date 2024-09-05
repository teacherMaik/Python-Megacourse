# todos = []
# num_todos = 0

# Gets any todos from todo file by opening file and reading it
with open('todos.txt', 'r') as file:
    todos = file.readlines()

while True:

    # Asks user what action they want to execute
    user_action = input("Do you want to add a todo, edit a todo, complete a todo, show the list of todos or exit the app? -> ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        # num_todos = num_todos + 1

        todo = user_action[4:] + "\n"
        todos.append(todo)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith('edit'):

        try:
            todo_edit = int(input("Which todo do you want to edit? (number) -> "))
            print(todo_edit)

            if todo_edit > len(todos):
                print("You don't that many todos")

            elif todo_edit <= len(todos):
                new_todo = input("What needs todo? -> ") + "\n"
                todos[todo_edit - 1] = new_todo

                with open('todos.txt', 'w') as file:
                    file.writelines(todos)

        except ValueError:
            print("Command not known")
            continue

    elif user_action.startswith('show'):

        for item, todo in enumerate(todos):
            todo = todo.strip('\n')
            row = f"{item + 1}-{todo}"
            print(row)

    elif user_action.startswith('complete'):

        index = int(input("Which todo do you want to complete? (number) -> "))

        if index > len(todos):
            print("You don't that many todos")

        elif index <= len(todos):

            todo_complete = todos[index - 1].strip('\n')
            todos.pop(index - 1)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo \'{todo_complete}\' has been removed"
            print(message)

    elif user_action.startswith('exit'):

        print("Bye then!")
        break

    else:
        print("Command not recognized")

