import functions
import FreeSimpleGUI as sg

#Instances of elements / widgets
label = sg.Text('Type in a To-Do')
input_box = sg.Input(tooltip="Enter To-Do", key="todo")
add_button = sg.Button("Add")

list_box = sg.Listbox(values=functions.get_todos(),
                      key="todos",
                      enable_events=True,
                      size=(45, 10))


edit_button = sg.Button("Edit", mouseover_colors='red')
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

#Instance of a window, mother of widget instances. All items in layout list of lists MUST be gui widgets
window = sg.Window('My To-Do App',
                   [[label],
                            [input_box, add_button],
                            [list_box, edit_button, complete_button],
                            [exit_button]],
                   font=("Helvetica", 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + "\n"
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select a to-do to edit first")
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                print(todo_to_complete)
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)

            except IndexError:
                sg.popup("Please select a to-do to edit first")
        case "todos":
            window['todo'].update(value=values['todos'][0])

        case "Exit":
            break

        case sg.WIN_CLOSED:
            break

window.close()


