# temas :  DarkBlue3
import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        sg.change_look_and_feel('DarkBlue3')
        #Layout
        layout = [
            [sg.Text('Nome', size=(40, 0)), sg.Input(key='Nome', size=(10, 0))],
            [sg.Text('Idade'), sg.Input(key='Idade')],
            [sg.Button('Enviar')]
        ]
        #Janela
        janela = sg.Window("Hello, interface!").layout(layout)
        #Extrair dados
        self.btn, self.values = janela.Read()
        self.values['Idade'] = float(self.values['Idade'])

    def Iniciar(self):

        print(self.values)
        print(self.values['Nome'])
        print(self.values['Idade'])
        print(type(self.values['Nome']))
        print(type(self.values['Idade']))


tela = TelaPython()
tela.Iniciar()

