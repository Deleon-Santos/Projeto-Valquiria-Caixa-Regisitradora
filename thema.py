import PySimpleGUI as sg 
sg.LOOK_AND_FEEL_TABLE['MyCreatedTheme'] = {'BACKGROUND': '#A9A9A9', 
                                        'TEXT': '#000000', 
                                        'INPUT': '#DCDCDC', 
                                        'TEXT_INPUT': '#000000', 
                                        'SCROLL': '#99CC99', 
                                        'BUTTON': ('#000000', '#C0C0C0'), 
                                        'PROGRESS': ('#D1826B', '#CC8019'), 
                                        'BORDER': 3, 'SLIDER_DEPTH': 1,  
'PROGRESS_DEPTH': 1, } 
sg.theme('MyCreatedTheme') 
sg.popup_get_text('This how the MyNewTheme is created')