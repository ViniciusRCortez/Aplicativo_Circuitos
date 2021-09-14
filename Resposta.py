"""
Responder a EDO para a resposta tensão dos casos RC, RL e RLC
"""
from math import exp
import numpy as np
import matplotlib.pyplot as plt


def grafico(R, C, L, Vf, Vi, tempo, tipo):
    """
    Plota um grafico interatico depois de passado os valores das variaveis.
    :param R: Valor do Resistor.
    :param C: Valor do Capacitor.
    :param L: Valor do Indutor.
    :param Vf: Valor da Tensão na fonte, durante o regime não estacionario(t>0+).
    :param Vi: Condição inicial da fonte.
    :param tipo: Tipo do circuito.
    :param tempo: Valor do Resistor.
    """
    n = tempo / 100

    #   RC ou RL Serie
    if tipo == 'RC':
        Resultado = lambda t: Vf + ((Vi - Vf) * (exp(-(1 / (R * C)) * t))) # Vc = Vf + (Vi - Vf)e^(-1/rc)t
    elif tipo == 'RL':
        If = Vf/R
        Ii = Vi/R
        Corrente = lambda t: If + ((Ii - If) * (exp((-(R/L)) * t)))  # Il = If + (Ii - If)e^(-R/L)t
        Resultado = lambda t: Vf-R*Corrente(t)                      #Vl = Vf - Vr = Vf - R*I
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
