"""
Responder a EDO para a resposta tensão dos casos RC, RL e RLC
"""
from math import exp
import numpy as np
import matplotlib.pyplot as plt

R = float(input('Valor do Resistor em Ohms: '))
C = float(input('Valor do Capacitor em Faradays: '))
L = float(input('Valor do Indutor em Henrys: '))
Vi = float(input('Valor da Tensão da Fonte, em regime não-estacionario, em Volts: '))
fim = (float(input('Valor final do Tempo da simulação em MiliSegundos: ')))/1000
n = fim/100

#   RC ou RL Serie
V0 = float(input('Valor da Tensão de Inicial em Volts: '))
if C != 0 and L == 0:
    Resultado = lambda t: (V0 - Vi)*(exp(-(1/(R*C)) * t)) # (K - V)e^(-1/rc)t
elif C == 0 and L != 0:
    Resultado = lambda t: -R*(V0 - Vi) * (exp(-(R / L) * t))  # -R(K - V)e^(-R/L)t

x = np.arange(0, fim + n, n)
V = np.array([Resultado(t) for t in x])

plt.tight_layout()
plt.style.use('ggplot')
plt.plot(x*1000, V, 'r-', label='Vcarga')
plt.title('Tesão sobre a carga - Serie')
plt.xlabel('t(ms)')
plt.ylabel('Vcarga(V)')
plt.legend(loc='best')
plt.show()
