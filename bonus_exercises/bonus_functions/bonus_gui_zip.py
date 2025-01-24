import FreeSimpleGUI as sg
import shutil

label_from = sg.Text("Select Files")
input_from = sg.Input(tooltip="")
button_from_choose = sg.FileBrowse("Choose Files")

label_to = sg.Text("Select Folder")
input_to = sg.Input(tooltip="route to")
button_to_choose = sg.FolderBrowse("Choose Folder")

button_compress = sg.Button('compress')


window = sg.Window("My compressor App",
                   layout=[[label_from, input_from, button_from_choose],
                           [label_to, input_to, button_to_choose],
                           [button_compress]])

window.read()
window.close()