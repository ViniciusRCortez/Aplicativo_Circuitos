# temas :  DarkBlue3
import PySimpleGUI as sg
from Resposta import grafico

"""class TelaPython:
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
        self.values['Idade'] = self.values['Idade'].replace(',', '.')
        self.values['Idade'] = float(self.values['Idade'])

    def Iniciar(self):

        print(self.values)
        print(self.values['Nome'])
        print(self.values['Idade'])
        print(type(self.values['Nome']))
        print(type(self.values['Idade']))


tela = TelaPython()
tela.Iniciar()"""


# Layouts:
def Inicial():
    sg.change_look_and_feel('DarkBlue3')
    layout = [
        [sg.Checkbox('Circuito RL', key='RL', size=(30, 0))],
        [sg.Checkbox('Circuito RC', key='RC', size=(30, 0))],
        [sg.Checkbox('Circuito RLC série', key='RLCs', size=(30, 0))],
        [sg.Checkbox('Circuito RLC paralelo', key='RLCp', size=(30, 0))],
        [sg.Button('Próximo', size=(10, 0))]
    ]
    return sg.Window('Circuitos 1 - UFC', layout=layout, finalize=True)


def RC():
    sg.change_look_and_feel('DarkBlue3')
    layout = [
        [sg.Text('Valor da Tensão Final da Fonte em Volts:', size=(30, 0)),
         sg.Input(key='Vf', size=(10, 0))],
        [sg.Text('Tempo da simulação em MiliSegundos:', size=(30, 0)), sg.Input(key='tempo', size=(10, 0))],
        [sg.Text('Valor da Tensão de Inicial em Volts:', size=(30, 0)), sg.Input(key='Vi', size=(10, 0))],
        [sg.Text('Valor do Resistor em Ohms', size=(30, 0)), sg.Input(key='R', size=(10, 0))],
        [sg.Text('Valor do Capacitor em MicroFaradays:', size=(30, 0)), sg.Input(key='C', size=(10, 0))],
        [sg.Button('Calcular', size=(10, 0)), sg.Button('Voltar', size=(10, 0))]
    ]
    return sg.Window('Circuitos 1 - RC', layout=layout, finalize=True)


def RL():
    sg.change_look_and_feel('DarkBlue3')
    layout = [
        [sg.Text('Valor da Tensão Final da Fonte em Volts:', size=(30, 0)),
         sg.Input(key='Vf', size=(10, 0))],
        [sg.Text('Tempo da simulação em MiliSegundos:', size=(30, 0)), sg.Input(key='tempo', size=(10, 0))],
        [sg.Text('Valor da Tensão de Inicial em Volts:', size=(30, 0)), sg.Input(key='Vi', size=(10, 0))],
        [sg.Text('Valor do Resistor em Ohms', size=(30, 0)), sg.Input(key='R', size=(10, 0))],
        [sg.Text('Valor do Indutor em MileHenrys:', size=(30, 0)), sg.Input(key='L', size=(10, 0))],
        [sg.Button('Calcular', size=(10, 0)), sg.Button('Voltar', size=(10, 0))]
    ]
    return sg.Window('Circuitos 1 - RL', layout=layout, finalize=True)


def RLCs():
    sg.change_look_and_feel('DarkBlue3')
    layout = [
        [sg.Text('Valor da Tensão Final da Fonte em Volts:', size=(30, 0)),
         sg.Input(key='Vf', size=(10, 0))],
        [sg.Text('Tempo da simulação em MiliSegundos:', size=(30, 0)), sg.Input(key='tempo', size=(10, 0))],
        [sg.Text('Valor da Tensão de Inicial em Volts:', size=(30, 0)), sg.Input(key='Vi', size=(10, 0))],
        [sg.Text('Valor do Resistor em Ohms', size=(30, 0)), sg.Input(key='R', size=(10, 0))],
        [sg.Text('Valor do Capacitor em MicroFaradays:', size=(30, 0)), sg.Input(key='C', size=(10, 0))],
        [sg.Text('Valor do Indutor em MileHenrys:', size=(30, 0)), sg.Input(key='L', size=(10, 0))],
        [sg.Button('Calcular', size=(10, 0)), sg.Button('Voltar', size=(10, 0))]
    ]
    return sg.Window('Circuitos 1 - RLC série', layout=layout, finalize=True)


def RLCp():
    sg.change_look_and_feel('DarkBlue3')
    layout = [
        [sg.Text('Valor da Tensão Final da Fonte em Volts:', size=(30, 0)),
         sg.Input(key='Vf', size=(10, 0))],
        [sg.Text('Tempo da simulação em MiliSegundos:', size=(30, 0)), sg.Input(key='tempo', size=(10, 0))],
        [sg.Text('Valor da Tensão de Inicial em Volts:', size=(30, 0)), sg.Input(key='Vi', size=(10, 0))],
        [sg.Text('Valor do Resistor em Ohms', size=(30, 0)), sg.Input(key='R', size=(10, 0))],
        [sg.Text('Valor do Capacitor em MicroFaradays:', size=(30, 0)), sg.Input(key='C', size=(10, 0))],
        [sg.Text('Valor do Indutor em MileHenrys:', size=(30, 0)), sg.Input(key='L', size=(10, 0))],
        [sg.Button('Calcular', size=(10, 0)), sg.Button('Voltar', size=(10, 0))]
    ]
    return sg.Window('Circuitos 1 - RLC paralelo', layout=layout, finalize=True)


# Janelas Iniciais:
janela1, janela2 = Inicial(), None

# Leitor de janelas:
while True:
    window, event, value = sg.read_all_windows()
    # Janela Fechada:
    if event == sg.WIN_CLOSED:
        break
    # Proxima Janela:
    if event == 'Próximo':
        #Circuito RC
        if value['RC'] == True and value['RL'] == value['RLCs'] == value['RLCp'] == False:
            janela2 = RC()
            janela1.hide()
            tipo = 'RC'
        elif value['RL'] == True and value['RC'] == value['RLCs'] == value['RLCp'] == False:
            janela2 = RL()
            janela1.hide()
            tipo = 'RL'
        elif value['RLCs'] == True and value['RC'] == value['RL'] == value['RLCp'] == False:
            janela2 = RLCs()
            janela1.hide()
            tipo = 'RLCs'
        elif value['RLCp'] == True and value['RC'] == value['RLCs'] == value['RL'] == False:
            janela2 = RLCp()
            janela1.hide()
            tipo = 'RLCp'
        else:
            sg.popup('Escolha somente uma opção')
    #Voltando para janela anterior:
    if event == 'Voltar':
        janela2.hide()
        janela1 = Inicial()
        tipo = 'Inicio'
    #Plotando grafico:
    if event == 'Calcular':
        if tipo == 'RC':
            # Extraindo dados:
            lista = ('R', 'C', 'Vf', 'tempo', 'Vi')
            for i in lista:
                if value[i] == None or value[i] == '':  # Zera os valores em branco
                    value[i] = 0
                value[i] = float(value[i])  # Troca , por .
            if value['tempo'] == 0:
                value['tempo'] = 1  # Caso tempo esteja em branco sera 1ms
            value['R'] = float(value['R'])
            value['C'] = (float(value['C'])) / (10 ** 6)
            value['Vf'] = float(value['Vf'])
            value['tempo'] = (float(value['tempo'])) / (10 ** 3)
            value['Vi'] = float(value['Vi'])
            grafico(value['R'], value['C'], 0, value['Vf'], value['Vi'],
                value['tempo'], tipo)
        elif tipo == 'RL':
            lista = ('R', 'L', 'Vf', 'tempo', 'Vi')
            for i in lista:
                if value[i] == None or value[i] == '':  # Zera os valores em branco
                    value[i] = 0
                value[i] = float(value[i])  # Troca , por .
            if value['tempo'] == 0:
                value['tempo'] = 1  # Caso tempo esteja em branco sera 1ms
            value['R'] = float(value['R'])
            value['L'] = (float(value['L']))/(10**3)
            value['Vf'] = float(value['Vf'])
            value['tempo'] = (float(value['tempo'])) / (10 ** 3)
            value['Vi'] = float(value['Vi'])
            grafico(value['R'], 0, value['L'], value['Vf'], value['Vi'],
                    value['tempo'], tipo)

