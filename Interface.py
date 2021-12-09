import PySimpleGUI as sg
from Resposta import grafico_tensão, grafico_corrente
from Imagens import *


# Layouts:
def Inicial():
    sg.change_look_and_feel('DarkBlue3')
    layout = [
        [sg.Checkbox('Circuito RL série', key='RLs', size=(22, 0))],
        [sg.Checkbox('Circuito RC série', key='RCs', size=(22, 0))],
        [sg.Checkbox('Circuito RL paralelo', key='RLp', size=(22, 0))],
        [sg.Checkbox('Circuito RC paralelo', key='RCp', size=(22, 0))],
        [sg.Checkbox('Circuito RLC série', key='RLCs', size=(22, 0))],
        [sg.Checkbox('Circuito RLC paralelo', key='RLCp', size=(22, 0))],
        [sg.Text('Calcular:'), sg.Checkbox('Tensão', key='Tensão', size=(10, 0)),
         sg.Checkbox('Corrente', key='Corrente', size=(10, 0))],
        [sg.Button('Próximo', size=(10, 0))]
    ]
    return sg.Window('Circuitos 1 - UFC', layout=layout, finalize=True)


def RCs():
    sg.change_look_and_feel('DarkBlue3')
    layout = [
        [sg.Text('Tipo de circuito:')],
        [sg.Image(data=imagem_RCs)],
        [sg.Text('Valor da Tensão da Fonte (V):', size=(22, 0)),
         sg.Input(key='Vf', size=(10, 0))],
        [sg.Text('Tempo da simulação (ms):', size=(22, 0)), sg.Input(key='tempo', size=(10, 0))],
        [sg.Text('Valor da Tensão Inicial do Capacitor (V):', size=(22, 0)), sg.Input(key='Vi', size=(10, 0))],
        [sg.Text(f'Valor do Resistor ({chr(937)})', size=(22, 0)), sg.Input(key='R', size=(10, 0))],
        [sg.Text(f'Valor do Capacitor ({chr(181)}F):', size=(22, 0)), sg.Input(key='C', size=(10, 0))],
        [sg.Button('Calcular', size=(10, 0)), sg.Button('Voltar', size=(10, 0))]
    ]
    return sg.Window('Circuitos 1 - RC série', layout=layout, finalize=True)


def RLs():
    sg.change_look_and_feel('DarkBlue3')
    layout = [
        [sg.Text('Tipo de circuito:')],
        [sg.Image(data=imagem_RLs)],
        [sg.Text('Valor da Tensão da Fonte (V):', size=(22, 0)),
         sg.Input(key='Vf', size=(10, 0))],
        [sg.Text('Tempo da simulação (ms):', size=(22, 0)), sg.Input(key='tempo', size=(10, 0))],
        [sg.Text('Valor da Corrente Inicial do Indutor (A):', size=(22, 0)), sg.Input(key='Vi', size=(10, 0))],
        [sg.Text(f'Valor do Resistor ({chr(937)})', size=(22, 0)), sg.Input(key='R', size=(10, 0))],
        [sg.Text('Valor do Indutor (mH):', size=(22, 0)), sg.Input(key='L', size=(10, 0))],
        [sg.Button('Calcular', size=(10, 0)), sg.Button('Voltar', size=(10, 0))]
    ]
    return sg.Window('Circuitos 1 - RL série', layout=layout, finalize=True)


def RCp():
    sg.change_look_and_feel('DarkBlue3')
    layout = [
        [sg.Text('Tipo de circuito:')],
        [sg.Image(data=imagem_RCp)],
        [sg.Text('Valor da Corrente da Fonte (A):', size=(22, 0)),
         sg.Input(key='Vf', size=(10, 0))],
        [sg.Text('Tempo da simulação (ms):', size=(22, 0)), sg.Input(key='tempo', size=(10, 0))],
        [sg.Text('Valor da Tensão Inicial do Capacitor (V):', size=(22, 0)), sg.Input(key='Vi', size=(10, 0))],
        [sg.Text(f'Valor do Resistor ({chr(937)})', size=(22, 0)), sg.Input(key='R', size=(10, 0))],
        [sg.Text(f'Valor do Capacitor ({chr(181)}F):', size=(22, 0)), sg.Input(key='C', size=(10, 0))],
        [sg.Button('Calcular', size=(10, 0)), sg.Button('Voltar', size=(10, 0))]
    ]
    return sg.Window('Circuitos 1 - RC paralelo', layout=layout, finalize=True)


def RLp():
    sg.change_look_and_feel('DarkBlue3')
    layout = [
        [sg.Text('Tipo de circuito:')],
        [sg.Image(data=imagem_RLp)],
        [sg.Text('Valor da Corrente da Fonte (A):', size=(22, 0)),
         sg.Input(key='Vf', size=(10, 0))],
        [sg.Text('Tempo da simulação (ms):', size=(22, 0)), sg.Input(key='tempo', size=(10, 0))],
        [sg.Text('Valor da Corrente Inicial do Indutor (A):', size=(22, 0)), sg.Input(key='Vi', size=(10, 0))],
        [sg.Text(f'Valor do Resistor ({chr(937)})', size=(22, 0)), sg.Input(key='R', size=(10, 0))],
        [sg.Text('Valor do Indutor (mH):', size=(22, 0)), sg.Input(key='L', size=(10, 0))],
        [sg.Button('Calcular', size=(10, 0)), sg.Button('Voltar', size=(10, 0))]
    ]
    return sg.Window('Circuitos 1 - RL paralelo', layout=layout, finalize=True)


def RLCs():
    sg.change_look_and_feel('DarkBlue3')
    layout = [
        [sg.Text('Tipo de circuito:')],
        [sg.Image(data=imagem_RLCs)],
        [sg.Text('Valor da Tensão da Fonte (V):', size=(22, 0)),
         sg.Input(key='Vf', size=(10, 0))],
        [sg.Text('Tempo da simulação (ms)', size=(22, 0)), sg.Input(key='tempo', size=(10, 0))],
        [sg.Text('Valor da Tensão Inicial do Capacitor (V):', size=(22, 0)), sg.Input(key='Vi', size=(10, 0))],
        [sg.Text('Valor da Corrente Inicial do Indutor (A)', size=(22, 0)), sg.Input(key='Ii', size=(10, 0))],
        [sg.Text(f'Valor do Resistor ({chr(937)})', size=(22, 0)), sg.Input(key='R', size=(10, 0))],
        [sg.Text(f'Valor do Capacitor ({chr(181)}F):', size=(22, 0)), sg.Input(key='C', size=(10, 0))],
        [sg.Text('Valor do Indutor (mH):', size=(22, 0)), sg.Input(key='L', size=(10, 0))],
        [sg.Text('Saída  sobre o:'), sg.Checkbox('Capacitor', key='Cap', size=(10, 0)),
         sg.Checkbox('Indutor', key='Ind', size=(10, 0))],
        [sg.Button('Calcular', size=(10, 0)), sg.Button('Voltar', size=(10, 0))]
    ]
    return sg.Window('Circuitos 1 - RLC série', layout=layout, finalize=True)


def RLCp():
    sg.change_look_and_feel('DarkBlue3')
    layout = [
        [sg.Text('Tipo de circuito:')],
        [sg.Image(data=imagem_RLCp)],
        [sg.Text('Valor da Corrente da Fonte (A):', size=(22, 0)),
         sg.Input(key='Vf', size=(10, 0))],
        [sg.Text('Tempo da simulação (ms)', size=(22, 0)), sg.Input(key='tempo', size=(10, 0))],
        [sg.Text('Valor da Tensão Inicial do Capacitor (V)', size=(22, 0)), sg.Input(key='Vi', size=(10, 0))],
        [sg.Text('Valor da Corrente Inicial do Indutor (A)', size=(22, 0)), sg.Input(key='Ii', size=(10, 0))],
        [sg.Text(f'Valor do Resistor ({chr(937)})', size=(22, 0)), sg.Input(key='R', size=(10, 0))],
        [sg.Text(f'Valor do Capacitor ({chr(181)}F):', size=(22, 0)), sg.Input(key='C', size=(10, 0))],
        [sg.Text('Valor do Indutor (mH)', size=(22, 0)), sg.Input(key='L', size=(10, 0))],
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
            value['RCs'] = value['RLs'] = value['RLCs'] = value['RLCp'] = value['RCp'] = value['RLp'] = False
            tipo = 'Inicio'
        elif value['Corrente'] == True and value['Tensão'] == True:
            janela1.hide()
            janela1 = Inicial()
            value['RCs'] = value['RLs'] = value['RLCs'] = value['RLCp'] = value['RCp'] = value['RLp'] = False
            tipo = 'Inicio'
        elif value['Tensão']:
            escolha = 'Tensão'
        else:
            escolha = 'Corrente'
        if value['RCs'] == True and value['RLs'] == value['RLCs'] == value['RLCp'] == value['RCp'] == value['RLp'] == False:
            janela2 = RCs()
            janela1.hide()
            tipo = 'RCs'
        elif value['RLs'] == True and value['RCs'] == value['RLCs'] == value['RLCp'] == value['RCp'] == value['RLp'] == False:
            janela2 = RLs()
            janela1.hide()
            tipo = 'RLs'
        elif value['RCp'] == True and value['RLp'] == value['RLCs'] == value['RLCp'] == value['RCs'] == value['RLs'] == False:
            janela2 = RCp()
            janela1.hide()
            tipo = 'RCp'
        elif value['RLp'] == True and value['RCp'] == value['RLCs'] == value['RLCp'] == value['RCs'] == value['RLs'] == False:
            janela2 = RLp()
            janela1.hide()
            tipo = 'RLp'
        elif value['RLCs'] == True and value['RCs'] == value['RLs'] == value['RLCp'] == value['RCp'] == value['RLp'] == False:
            janela2 = RLCs()
            janela1.hide()
            tipo = 'RLCs'
        elif value['RLCp'] == True and value['RCs'] == value['RLCs'] == value['RLs'] == value['RCp'] == value['RLp'] == False:
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
        if tipo == 'RCs':
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
        elif tipo == 'RLp':
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

        elif tipo == 'RCp':
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
        elif tipo == 'RLs':
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
