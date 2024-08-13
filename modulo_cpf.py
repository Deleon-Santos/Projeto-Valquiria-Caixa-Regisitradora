import PySimpleGUI as sg

def cpf():
    while True:
        try:
            cpf = sg.popup_get_text("Adicione um CPF?", size=(15, 1), font=('Any', 18), no_titlebar=True)
            if not cpf:
                cpf = "000.000.000-00"# cpf retorna zerado
                return cpf
            if len(cpf) == 11 and cpf.isdigit():#formata o cpf  digitado
                cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
                return cpf
            else:
                sg.popup("CPF inválido. Deve ter 11 dígitos.")
                continue
        except ValueError:
            sg.popup("CPF inválido")
            continue

    sg.popup(f"CPF formatado: {cpf}")

