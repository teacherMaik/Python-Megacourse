import FreeSimpleGUI as sg
import bonus_gui_zip_funtcions

sg.theme('Black')

select_label = sg.Text("Select file to unzip")
select_input = sg.Input()
select_browser = sg.FilesBrowse('Choose', key='file')

dest_label = sg.Text("Select folder to save files")
dest_input = sg.Input()
dest_browser = sg.FolderBrowse('Choose', key='dest_folder')

unzip_btn = sg.Button('un-zip')
exit_btn = sg.Button('Exit')

window = sg.Window('My unzip gui', layout=[[select_label, select_input, select_browser],
                                                [dest_label, dest_input, dest_browser],
                                                [unzip_btn, exit_btn]])
while True:
    event, values = window.read()
    archive_path = values['file']
    folder = values['dest_folder']

    match event:
        case 'un-zip':
            print(archive_path)
            print(folder)

            try:
                bonus_gui_zip_funtcions.extract_archive(archive_path, folder)
            except IndexError:
                print(IndexError)
        case 'Exit':
            break


