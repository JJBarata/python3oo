from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário:'), sg.Input(key='usuario', size=(40,1))],
    [sg.Text('Senha:'), sg.Input(key='senha', password_char='*', size=(40,1))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]
# janela
janela = sg.Window('Tela de Login', layout)
# Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'Jorge' and valores['senha'] == '123456':
            print('Seja Bem-vindo ao DevPython!')

