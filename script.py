"""
Testing
"""
import PySimpleGUI as sg

sg.theme('DarkAmber')

layout =[   [sg.Text('Some test on row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('ok'), sg.Button('cancel')] ]

window = sg.Window('Note Taker', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()
