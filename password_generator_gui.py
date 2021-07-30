import PySimpleGUI as sg

from pasword_generator import PasswordGenerator


class PasswordGeneratorGui:

    def create_gui(self) -> None:
        body_text_font = ('Aerial', 16)
        frame_title_font_size = ('Aerial', 20)

        password_options_column_one_layout = [
            [
                sg.Text(
                    text='Password Length',
                    justification='left',
                    font=body_text_font
                )
            ],
            [
                sg.Slider(
                    key='-PASSWORD_LENGTH-',
                    range=(8, 100),
                    default_value=8,
                    size=(30, 10),
                    orientation='horizontal',
                    font=body_text_font
                )
            ],
            [
                sg.Checkbox(
                    key='-DIGITS-',
                    text='Include Numbers',
                    default=True,
                    font=body_text_font
                )
            ],
            [
                sg.Checkbox(
                    key='-SPECIAL_CHARS-',
                    text='Include Special Characters',
                    default=True,
                    font=body_text_font
                )
            ],
        ]

        password_options_column_two_layout = [
            [
                sg.Text(
                    text='Number of Words',
                    justification='left',
                    font=body_text_font
                )
            ],
            [
                sg.Slider(
                    key='-NUM_OF_WORDS-',
                    range=(4, 20),
                    default_value=4,
                    size=(30, 10),
                    orientation='horizontal',
                    font=body_text_font
                )
            ],
        ]

        password_options_layout = [
            [
                sg.DropDown(
                    key='-OPTIONS_LIST-',
                    values=['Shuffled Passwords', 'Human-Readable Passwords'],
                    default_value='Shuffled Passwords',
                    enable_events=True,
                    font=body_text_font,
                )
            ],
            [
                sg.Column(
                    key='-PO_COL_1-',
                    layout=password_options_column_one_layout
                ),
                sg.Column(
                    key='-PO_COL_2-',
                    layout=password_options_column_two_layout,
                    visible=False
                )
            ],
        ]

        output_frame_layout = [
            [
                sg.Output(
                    key='-OUTPUT-',
                    size=(35, 11),
                    font=body_text_font
                )
            ]
        ]

        button_frame_layout = [
            [
                sg.Button(
                    button_text='Generate',
                    key='-GENERATE-',
                    font=body_text_font
                ),
                sg.Button(
                    button_text='Reset',
                    key='-RESET-',
                    font=body_text_font
                ),
                sg.Button(
                    button_text='Clear Output',
                    key='-CLEAR-',
                    font=body_text_font
                ),
                sg.Button(
                    button_text='Exit',
                    key='-EXIT-',
                    font=body_text_font
                ),
            ]
        ]

        layout = [
            [
                sg.Frame(
                    'Password Options',
                    layout=password_options_layout,
                    element_justification='c',
                    font=frame_title_font_size
                ),
                sg.Frame(
                    'Generated Passwords',
                    layout=output_frame_layout,
                    element_justification='c',
                    font=frame_title_font_size
                )
            ],
            [
                sg.Frame(
                    title='',
                    layout=button_frame_layout,
                    element_justification='c',
                    border_width=0
                )
            ]
        ]

        window = sg.Window(
            title='Password Generator',
            layout=layout,
            margins=(50, 50),
            auto_size_text=True,
            auto_size_buttons=True,
            resizable=True,
            element_justification='c',
        ).finalize()

        password_length_key = '-PASSWORD_LENGTH-'
        while True:
            event, values = window.read()

            if event == '-GENERATE-' and window['-PO_COL_1-'].visible:
                password_generator = PasswordGenerator(
                    password_length=int(values['-PASSWORD_LENGTH-']),
                    include_numbers=values['-DIGITS-'],
                    include_special_chars=values['-SPECIAL_CHARS-'],
                )
                password = password_generator.generate_shuffled_password()
                print(password)
                print('\n')

            elif event == '-GENERATE-' and window['-PO_COL_2-'].visible:
                password_generator = PasswordGenerator(
                    password_length=int(values['-NUM_OF_WORDS-']),
                )
                password = password_generator.generate_human_readable_password()
                print(password)
                print('\n')

            if event == '-OPTIONS_LIST-':
                if values['-OPTIONS_LIST-'] == 'Shuffled Passwords':
                    window['-PO_COL_1-'].update(visible=True)
                    window['-PO_COL_2-'].update(visible=False)

                elif values['-OPTIONS_LIST-'] == 'Human-Readable Passwords':
                    window['-PO_COL_1-'].update(visible=False)
                    window['-PO_COL_2-'].update(visible=True)

            if event == '-RESET-':
                if '-DIGITS-' in values.keys():
                    window.FindElement('-DIGITS-').Update(True)

                if '-SPECIAL_CHARS-' in values.keys():
                    window.FindElement('-SPECIAL_CHARS-').Update(True)

                if '-PASSWORD_LENGTH-' in values.keys():
                    window.FindElement('-PASSWORD_LENGTH-').Update(0)

                if '-NUM_OF_WORDS-' in values.keys():
                    window.FindElement('-NUM_OF_WORDS-').Update(0)

            if event == '-CLEAR-':
                window.FindElement('-OUTPUT-').Update('')

            if event == '-EXIT-' or event == sg.WIN_CLOSED:
                break

        window.close()

