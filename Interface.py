import PySimpleGUI as sg
from Resposta import grafico

class TelaPython():
    def __init__(self):
        sg.change_look_and_feel('DarkBlue3')
        #Layout:
        layout = [
            [sg.Text('Valor da Tensão da Fonte, em regime não-estacionario, em Volts:', size=(30, 0)),
             sg.Input(key='Vi', size=(10, 0))],
            [sg.Text('Tempo da simulação em MiliSegundos:', size=(30, 0)), sg.Input(key='tempo', size=(10, 0))],
            [sg.Text('Valor da Tensão de Inicial em Volts:', size=(30, 0)), sg.Input(key='V0', size=(10, 0))],
            [sg.Text('Valor do Resistor em Ohms', size=(30, 0)), sg.Input(key='R', size=(10, 0))],
            [sg.Text('Valor do Capacitor em MicroFaradays:', size=(30, 0)), sg.Input(key='C', size=(10, 0))],
            [sg.Text('Valor do Indutor em MileHenrys:', size=(30, 0)), sg.Input(key='L', size=(10, 0))],
            [sg.Button('Calcular', size=(10, 0))]
        ]
        #Janela:
        janela = sg.Window('Circuitos 1 - UFC').layout(layout)
        #Extrair dados:
        self.btn, self.values = janela.Read()
        lista = ('R', 'C', 'L', 'Vi', 'tempo', 'V0')
        for i in lista:
            if self.values[i] == None or self.values[i] == '':
                self.values[i] = 0
        if self.values['tempo'] == 0:
            self.values['tempo'] = 1
        self.values['R'] = float(self.values['R'])
        self.values['C'] = (float(self.values['C']))/(10**6)
        self.values['L'] = (float(self.values['L']))/(10**3)
        self.values['Vi'] = float(self.values['Vi'])
        self.values['tempo'] = (float(self.values['tempo']))/(10**3)
        self.values['V0'] = float(self.values['V0'])

    def Iniciar(self):
        grafico(self.values['R'], self.values['C'], self.values['L'], self.values['Vi'], self.values['V0'],
                self.values['tempo'])


tela = TelaPython()
tela.Iniciar()
