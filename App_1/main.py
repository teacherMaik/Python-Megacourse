todos = []
num_todos = 0

while True:

    user_action = input("Do you want to add a todo, edit a todo, complete a todo, show the list of todos or exit the app? -> ")
    user_action = user_action.strip()

    match user_action:
        case 'add' | 'add todo' | 'add a todo':
            num_todos = num_todos + 1
            todo = input("What is there todo? -> ")
            todos.append(todo)

            # todo_to_add = str(num_todos) + " - " + todo
            # todos.append(todo_to_add)
        case 'edit' | 'edit todo' | 'edit a todo':
            todo_edit = int(input("Which todo do you want to edit? (number) -> "))

            if todo_edit > len(todos):
                print("You don't that many todos")
            elif todo_edit <= len(todos):
                new_todo = input("What needs todo? -> ")
                todos[todo_edit - 1] = new_todo
                # new_todo_to_add = str(todo_edit) + " - " + new_todo
                # todos[todo_edit - 1] = new_todo_to_add
        case 'show' | 'show todos' | 'show list':
            for i, todo in enumerate(todos):
                row = f"{i + 1}-{todo}"
                print(row)
        case 'complete' | 'complete todo' | 'complete a todo':
            todo_remove = int(input("Which todo have you completed? (number) -> "))
            todos.pop(todo_remove - 1)
        case 'exit':
            print("Bye then!")
            break
        case _:
            print("Command not recognized")

