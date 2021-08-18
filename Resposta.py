"""
Responder a EDO para a resposta tensão dos casos RC, RL e RLC
"""
from math import exp
import numpy as np
import matplotlib.pyplot as plt


def grafico(R, C, L, Vi, V0, tempo):
    """
    Plota um grafico interatico depois de passado os valores das variaveis.
    :param R: Valor do Resistor.
    :param C: Valor do Capacitor.
    :param L: Valor do Indutor.
    :param Vi: Valor da Tensão na fonte, durante o regime não estacionario(t>0+).
    :param V0: Condição inicial da fonte.
    :param tempo: Valor do Resistor.
    """
    n = tempo / 100

    #   RC ou RL Serie
    if C != 0 and L == 0:
        Resultado = lambda t: (V0 - Vi) * (exp(-(1 / (R * C)) * t))  # (K - V)e^(-1/rc)t
    elif C == 0 and L != 0:
        Resultado = lambda t: -R * (V0 - Vi) * (exp(-(R / L) * t))  # -R(K - V)e^(-R/L)t
    x = np.arange(0, tempo + n, n)
    V = np.array([Resultado(t) for t in x])

    plt.ion()
    plt.cla()
    plt.clf()
    plt.tight_layout()
    plt.style.use('ggplot')
    plt.plot(x * 1000, V, 'r-', label='Vcarga')
    plt.title('Tesão sobre a carga - Serie')
    plt.xlabel('t(ms)')
    plt.ylabel('Vcarga(V)')
    plt.legend(loc='best')
    plt.pause(0.1)
    plt.ioff()
    plt.show()


"""R = 10
C = 1
C /= 1000000
L = 0
L /= 1000
Vi = 10
V0 = 0
tempo = 0.1
tempo /= 1000
grafico(R, C, L, Vi, V0, tempo)"""
