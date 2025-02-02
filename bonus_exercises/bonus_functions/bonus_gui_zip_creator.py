import FreeSimpleGUI as sg
import bonus_gui_zip_funtcions

# from bonus_exercises.bonus_functions.bonus_gui_zip_funtcions import make_archive

label_from = sg.Text("Select Files")
input_from = sg.Input(tooltip="")
button_from_choose = sg.FilesBrowse("Choose", key="files")

label_to = sg.Text("Select Folder")
input_to = sg.Input(tooltip="route to")
button_to_choose = sg.FolderBrowse("Choose", key="folder")

button_compress = sg.Button('Compress')
button_exit = sg.Button('Exit')
output_label = sg.Text('', key="output")


window = sg.Window("My compressor App",
                   layout=[[label_from, input_from, button_from_choose],
                           [label_to, input_to, button_to_choose],
                           [button_compress, output_label],
                           [button_exit]])

while True:
    event, values = window.read()
    filepaths = values['files'].split(";")
    folder = values['folder']
    print(filepaths, folder)
    match event:

        case "Compress":
            try:
                bonus_gui_zip_funtcions.make_archive(filepaths, folder)
                window['output'].update('Your files have been compressed')
            except IndexError:
                output_label = "There has been an error"

        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()