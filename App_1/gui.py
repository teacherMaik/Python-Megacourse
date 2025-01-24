import functions
import FreeSimpleGUI as sg

#Instances of elements / widgets
label = sg.Text('Type in a To-Do')
input_box = sg.Input(tooltip="Enter To-Do")
add_button = sg.Button("Add")

#Instance of a window, mother of widget instances. All items in layout list of lists MUST be gui widgets
window = sg.Window('My To-Do App', [[label], [input_box, add_button]])

#Mthods on the instance
window.read()
window.close()


