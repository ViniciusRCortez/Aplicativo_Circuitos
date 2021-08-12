# temas :  DarkBlue3
import PySimpleGUI as sg


class TelaPython:
    def __init__(self):
        sg.change_look_and_feel('DarkBlue3')
        #Layout
        layout = [
            [sg.Text('Nome', key='Nome'), sg.Input()],
            [sg.Text('Idade', key='Idade'), sg.Input()],
            [sg.Button('Enviar')]
        ]
        #Janela
        janela = sg.Window("Hello, interface!").layout(layout)
        #Extrair dados
        self.btn, self.values = janela.Read()

    def Iniciar(self):
        print(self.values)


tela = TelaPython()
tela.Iniciar()

