import PySimpleGUI as sg
from Resposta import grafico_tensão, grafico_corrente


# Layouts:
def Inicial():
    sg.change_look_and_feel('DarkBlue3')
    layout = [
        [sg.Checkbox('Circuito RL', key='RL', size=(30, 0))],
        [sg.Checkbox('Circuito RC', key='RC', size=(30, 0))],
        [sg.Checkbox('Circuito RLC série', key='RLCs', size=(30, 0))],
        [sg.Checkbox('Circuito RLC paralelo', key='RLCp', size=(30, 0))],
        [sg.Text('Calcular:'), sg.Checkbox('Tensão', key='Tensão', size=(10, 0)),
         sg.Checkbox('Corrente', key='Corrente', size=(10, 0))],
        [sg.Button('Próximo', size=(10, 0))]
    ]
    return sg.Window('Circuitos 1 - UFC', layout=layout, finalize=True)


def RC():
    sg.change_look_and_feel('DarkBlue3')
    layout = [
        [sg.Text('Valor da Tensão Final da Fonte em Volts:', size=(30, 0)),
         sg.Input(key='Vf', size=(10, 0))],
        [sg.Text('Tempo da simulação em MiliSegundos:', size=(30, 0)), sg.Input(key='tempo', size=(10, 0))],
        [sg.Text('Valor da Tensão Inicial em Volts:', size=(30, 0)), sg.Input(key='Vi', size=(10, 0))],
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
        [sg.Text('Valor da Tensão Inicial em Volts:', size=(30, 0)), sg.Input(key='Vi', size=(10, 0))],
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
        [sg.Text('Valor da Tensão Inicial do Capacitor em Volts:', size=(30, 0)), sg.Input(key='Vi', size=(10, 0))],
        [sg.Text('Valor da Corrente Inicial do Indutor em Amperes:', size=(30, 0)), sg.Input(key='Ii', size=(10, 0))],
        [sg.Text('Valor do Resistor em Ohms', size=(30, 0)), sg.Input(key='R', size=(10, 0))],
        [sg.Text('Valor do Capacitor em MicroFaradays:', size=(30, 0)), sg.Input(key='C', size=(10, 0))],
        [sg.Text('Valor do Indutor em MileHenrys:', size=(30, 0)), sg.Input(key='L', size=(10, 0))],
        [sg.Text('Saída  sobre o:'), sg.Checkbox('Capacitor', key='Cap', size=(10, 0)),
         sg.Checkbox('Indutor', key='Ind', size=(10, 0))],
        [sg.Button('Calcular', size=(10, 0)), sg.Button('Voltar', size=(10, 0))]
    ]
    return sg.Window('Circuitos 1 - RLC série', layout=layout, finalize=True)


def RLCp():
    sg.change_look_and_feel('DarkBlue3')
    layout = [
        [sg.Text('Valor da Corrente Final da Fonte em Amperes:', size=(30, 0)),
         sg.Input(key='Vf', size=(10, 0))],
        [sg.Text('Tempo da simulação em MiliSegundos:', size=(30, 0)), sg.Input(key='tempo', size=(10, 0))],
        [sg.Text('Valor da Tensão Inicial do Capacitor em Volts:', size=(30, 0)), sg.Input(key='Vi', size=(10, 0))],
        [sg.Text('Valor da Corrente Inicial do Indutor em Amperes:', size=(30, 0)), sg.Input(key='Ii', size=(10, 0))],
        [sg.Text('Valor do Resistor em Ohms', size=(30, 0)), sg.Input(key='R', size=(10, 0))],
        [sg.Text('Valor do Capacitor em MicroFaradays:', size=(30, 0)), sg.Input(key='C', size=(10, 0))],
        [sg.Text('Valor do Indutor em MileHenrys:', size=(30, 0)), sg.Input(key='L', size=(10, 0))],
        [sg.Text('Saída  sobre o:'), sg.Checkbox('Capacitor', key='Cap', size=(10, 0)),
         sg.Checkbox('Indutor', key='Ind', size=(10, 0))],
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
        if value['Corrente'] == False and value['Tensão'] == False:
            janela1.hide()
            janela1 = Inicial()
            value['RC'] = value['RL'] = value['RLCs'] = value['RLCp'] = False
            tipo = 'Inicio'
        elif value['Corrente'] == True and value['Tensão'] == True:
            janela1.hide()
            janela1 = Inicial()
            value['RC'] = value['RL'] = value['RLCs'] = value['RLCp'] = False
            tipo = 'Inicio'
        elif value['Tensão']:
            escolha = 'Tensão'
        else:
            escolha = 'Corrente'
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
            sg.popup('Escolha somente um opção valida')
    # Voltando para janela anterior:
    if event == 'Voltar':
        janela2.hide()
        janela1 = Inicial()
        tipo = 'Inicio'
    # Plotando grafico:
    if event == 'Calcular':
        # Certificando qual sobre qual carga busca a resposta:
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
            if escolha == 'Tensão':
                grafico_tensão(value['R'], value['C'], 0, value['Vf'], value['Vi'],
                               value['tempo'], tipo, 0)
            elif escolha == 'Corrente':
                grafico_corrente(value['R'], value['C'], 0, value['Vf'], value['Vi'],
                                 value['tempo'], tipo, 0)
        elif tipo == 'RL':
            lista = ('R', 'L', 'Vf', 'tempo', 'Vi')
            for i in lista:
                if value[i] == None or value[i] == '':  # Zera os valores em branco
                    value[i] = 0
                value[i] = float(value[i])  # Troca , por .
            if value['tempo'] == 0:
                value['tempo'] = 1  # Caso tempo esteja em branco sera 1ms
            value['R'] = float(value['R'])
            value['L'] = (float(value['L'])) / (10 ** 3)
            value['Vf'] = float(value['Vf'])
            value['tempo'] = (float(value['tempo'])) / (10 ** 3)
            value['Vi'] = float(value['Vi'])
            if escolha == 'Tensão':
                grafico_tensão(value['R'], 0, value['L'], value['Vf'], value['Vi'],
                               value['tempo'], tipo, 0)
            elif escolha == 'Corrente':
                grafico_corrente(value['R'], 0, value['L'], value['Vf'], value['Vi'],
                                 value['tempo'], tipo, 0)

        elif tipo == 'RLCs':
            if [value['Cap'], value['Ind']] == [True, True] or [value['Cap'], value['Ind']] == [False, False]:
                sg.popup('Escolha somente entre Indutor ou Capacitor.')
                janela2.hide()
                janela1 = Inicial()
                tipo = 'Inicio'
            lista = ('R', 'C', 'L', 'Vf', 'tempo', 'Vi')
            for i in lista:
                if value[i] == None or value[i] == '':  # Zera os valores em branco
                    value[i] = 0
                value[i] = float(value[i])  # Troca , por .
            if value['tempo'] == 0:
                value['tempo'] = 1  # Caso tempo esteja em branco sera 1ms
            value['R'] = float(value['R'])
            value['C'] = (float(value['C'])) / (10 ** 6)
            value['L'] = (float(value['L'])) / (10 ** 3)
            value['Vf'] = float(value['Vf'])
            value['tempo'] = (float(value['tempo'])) / (10 ** 3)
            value['Vi'] = float(value['Vi'])
            if tipo == 'RLCs':
                if escolha == 'Tensão':
                    grafico_tensão(value['R'], value['C'], value['L'], value['Vf'], value['Vi'],
                                   value['tempo'], tipo, [value['Cap'], value['Ind']], value['Ii'])
                elif escolha == 'Corrente':
                    grafico_corrente(value['R'], value['C'], value['L'], value['Vf'], value['Vi'],
                                     value['tempo'], tipo, [value['Cap'], value['Ind']], value['Ii'])
        elif tipo == 'RLCp':
            if [value['Cap'], value['Ind']] == [True, True] or [value['Cap'], value['Ind']] == [False, False]:
                sg.popup('Escolha somente entre Indutor ou Capacitor.')
                janela2.hide()
                janela1 = Inicial()
                tipo = 'Inicio'
            lista = ('R', 'C', 'L', 'Vf', 'tempo', 'Vi')
            for i in lista:
                if value[i] == None or value[i] == '':  # Zera os valores em branco
                    value[i] = 0
                value[i] = float(value[i])  # Troca , por .
            if value['tempo'] == 0:
                value['tempo'] = 1  # Caso tempo esteja em branco sera 1ms
            value['R'] = float(value['R'])
            value['C'] = (float(value['C'])) / (10 ** 6)
            value['L'] = (float(value['L'])) / (10 ** 3)
            value['Vf'] = float(value['Vf'])
            value['tempo'] = (float(value['tempo'])) / (10 ** 3)
            value['Vi'] = float(value['Vi'])
            if tipo == 'RLCp':
                if escolha == 'Tensão':
                    grafico_tensão(value['R'], value['C'], value['L'], value['Vf'], value['Vi'],
                                   value['tempo'], tipo, [value['Cap'], value['Ind']], value['Ii'])
                elif escolha == 'Corrente':
                    grafico_corrente(value['R'], value['C'], value['L'], value['Vf'], value['Vi'],
                                     value['tempo'], tipo, [value['Cap'], value['Ind']], value['Ii'])
        else:
            sg.popup('Valores invalidos, tente novamente.')
            janela2.hide()
            janela1 = Inicial()
