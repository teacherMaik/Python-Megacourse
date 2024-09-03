todos = []

while True:

    user_action = input("Do you want to add a todo, show the list of todos or exit the app? -> ")

    match user_action:
        case 'add' | 'add todo' | 'add a todo':
            todo = input("What is there todo? -> ")
            todos.append(todo)
        case 'show' | 'show todos' | 'show list':
            for todo in todos:
                print(todo)
        case 'exit':
            print("Bye then!")
            break
        case _:
            print("Command not recognized")

