import functions
import FreeSimpleGUI as sg

#Instances of elements / widgets
label = sg.Text('Type in a To-Do')
input_box = sg.Input(tooltip="Enter To-Do", key="todo")
add_button = sg.Button("Add")

#Instance of a window, mother of widget instances. All items in layout list of lists MUST be gui widgets
window = sg.Window('My To-Do App',
                   [[label], [input_box, add_button]],
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
        case sg.WIN_CLOSED:
            break
        case "Edit":
            

window.close()


