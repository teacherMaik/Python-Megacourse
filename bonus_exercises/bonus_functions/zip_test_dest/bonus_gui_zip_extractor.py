import FreeSimpleGUI as sg

sg.theme('Black')

select_label = sg.Text("Select file to unzip")
select_input = sg.Input()
select_browser = sg.FilesBrowse('Choose', key='file')


