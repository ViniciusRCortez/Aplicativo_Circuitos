"""
Responder a EDO para a resposta tensão dos casos RC, RL e RLC
"""
from math import exp
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def RLCs(y, t, R, L, C, V):
    vc, x = y  # x = dvc/dt
    dxdt = [x, (1 / (L * C)) * V - (R / L) * x - (1 / (L * C)) * vc]
    return dxdt


def RLCp(y, t, R, L, C, V):
    vc, x = y  # x = dvc/dt
    dxdt = [x, V*(1/(L*C)) - (1 / (R * C)) * x - (1 / (L * C)) * vc]
    return dxdt


def grafico_tensão(R, C, L, Vf, Vi, tempo, tipo, Sobre=[0, 0], Ii=0):
    """
    Plota um grafico interatico depois de passado os valores das variaveis.
    :param R: Valor do Resistor.
    :param C: Valor do Capacitor.
    :param L: Valor do Indutor.
    :param Vf: Valor da Tensão na fonte, durante o regime não estacionario(t>0+).
    :param Vi: Condição inicial da fonte.
    :param tipo: Tipo do circuito.
    :param tempo: Tempo de simulação.
    :param sobre: Se é a saída sobre o capacitor ou o indutor.
    :param Ii: Corrente inicial do indutor.
    """
    n = tempo / 1000
    x = np.arange(0, tempo + n, n)

    if tipo == 'RC':
        Resultado = lambda t: Vf + ((Vi - Vf) * (exp(-(1 / (R * C)) * t)))  # Vc = Vf + (Vi - Vf)e^(-1/rc)t
    elif tipo == 'RL':
        If = Vf / R
        Ii = Vi / R
        Corrente = lambda t: If + ((Ii - If) * (exp((-(R / L)) * t)))  # Il = If + (Ii - If)e^(-R/L)t
        Resultado = lambda t: Vf - R * Corrente(t)  # Vl = Vf - Vr = Vf - R*I
    # RLC serie
    elif tipo == 'RLCs' and Sobre == [True, False]:  # Tensão sobre o Capacitor
        y0 = [Vi, Ii]
        sol = odeint(RLCs, y0, x, args=(R, L, C, Vf))
        V = sol[:, 0]
    elif tipo == 'RLCs' and Sobre == [False, True]:  # Tensão sobre o Indutor
        y0 = [Vi, Ii]
        sol = odeint(RLCs, y0, x, args=(R, L, C, Vf))
        Vc = sol[:, 0]
        Il = sol[:, 1] * C
        Vf_novo = np.ones_like(Vc) * Vf
        V = Vf_novo - R * Il - Vc
    elif tipo == 'RLCp':  # Tensão sobre o Capacitor, para paralelo é a mesma
        y0 = [Vi, Ii]
        sol = odeint(RLCp, y0, x, args=(R, L, C, Vf))
        Il_linha = sol[:, 1]
        V = L*Il_linha
    if tipo == 'RC' or tipo == 'RL':
        V = np.array([Resultado(t) for t in x])

        plt.tight_layout()
        plt.style.use('ggplot')
        plt.plot(x * 1000, V, 'r-', label='Vcarga')
        plt.title('Tesão sobre a carga')
        plt.xlabel('t(ms)')
        plt.ylabel('Vcarga(V)')
        plt.legend(loc='best')
        plt.show()
    elif tipo == 'RLCs':
        plt.tight_layout()
        plt.style.use('ggplot')
        plt.plot(x * 1000, V, 'r-', label='Vcarga')
        plt.title('Tesão sobre a carga - Serie')
        plt.xlabel('t(ms)')
        plt.ylabel('Vcarga(V)')
        plt.legend(loc='best')
        plt.show()
    elif tipo == 'RLCp':
        plt.tight_layout()
        plt.style.use('ggplot')
        plt.plot(x * 1000, V, 'r-', label='Vcarga')
        plt.title('Tesão sobre a carga - Paralelo')
        plt.xlabel('t(ms)')
        plt.ylabel('Vcarga(V)')
        plt.legend(loc='best')
        plt.show()


def grafico_corrente(R, C, L, Vf, Vi, tempo, tipo, Sobre=[0, 0], Ii=0):
    """
       Plota um grafico interatico depois de passado os valores das variaveis.
       :param R: Valor do Resistor.
       :param C: Valor do Capacitor.
       :param L: Valor do Indutor.
       :param Vf: Valor da Tensão na fonte, durante o regime não estacionario(t>0+).
       :param Vi: Condição inicial da fonte.
       :param tipo: Tipo do circuito.
       :param tempo: Tempo de simulação.
       :param sobre: Se é a saída sobre o capacitor ou o indutor.
       :param Ii: Corrente inicial do indutor.
       """
    n = tempo / 1000
    x = np.arange(0, tempo + n, n)

    if tipo == 'RC':
        Vc = lambda t: Vf + ((Vi - Vf) * (exp(-(1 / (R * C)) * t)))  # Vc = Vf + (Vi - Vf)e^(-1/rc)t
        Resultado = lambda t: (Vf - Vc(t))/R
    elif tipo == 'RL':
        If = Vf / R
        Ii = Vi / R
        Resultado = lambda t: If + ((Ii - If) * (exp((-(R / L)) * t)))  # Il = If + (Ii - If)e^(-R/L)t
    # RLC serie
    elif tipo == 'RLCs':  # Tensão sobre o Capacitor
        y0 = [Vi, Ii]
        sol = odeint(RLCs, y0, x, args=(R, L, C, Vf))
        Vc_linha = sol[:, 1]
        V = C*Vc_linha
    elif tipo == 'RLCp' and Sobre == [False, True]:  # Corrente sobre o Indutor
        y0 = [Vi, Ii]
        sol = odeint(RLCp, y0, x, args=(R, L, C, Vf))
        V = sol[:, 0]
    elif tipo == 'RLCp' and Sobre == [True, False]:  # Corrente sobre o Capacitor
        y0 = [Vi, Ii]
        sol = odeint(RLCp, y0, x, args=(R, L, C, Vf))
        Il = sol[:, 0]
        Il_linha = sol[:, 1]
        Vc = L*Il_linha
        V = Vf - Vc/R - Il
    if tipo == 'RC' or tipo == 'RL':
        V = np.array([Resultado(t) for t in x])

        plt.tight_layout()
        plt.style.use('ggplot')
        plt.plot(x * 1000, V, 'r-', label='Icarga')
        plt.title('Corrente sobre a carga')
        plt.xlabel('t(ms)')
        plt.ylabel('Icarga(A)')
        plt.legend(loc='best')
        plt.show()
    elif tipo == 'RLCs':
        plt.tight_layout()
        plt.style.use('ggplot')
        plt.plot(x * 1000, V, 'r-', label='Icarga')
        plt.title('Corrente sobre a carga - Serie')
        plt.xlabel('t(ms)')
        plt.ylabel('Icarga(A)')
        plt.legend(loc='best')
        plt.show()
    elif tipo == 'RLCp':
        plt.tight_layout()
        plt.style.use('ggplot')
        plt.plot(x * 1000, V, 'r-', label='Icarga')
        plt.title('Corrente sobre a carga - Paralelo')
        plt.xlabel('t(ms)')
        plt.ylabel('Icarga(A)')
        plt.legend(loc='best')
        plt.show()



