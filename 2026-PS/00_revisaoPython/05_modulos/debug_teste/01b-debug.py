# debug_teste/01b-debug.py
# ATENÇÃO: 4 Erros propositais. Encontre e corrija todos!
# Rode de dentro de 05_modulos/: python debug_teste/01b-debug.py

# adiciona a pasta ao caminho do Python para importar módulos dos projetos
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# import Temperatura                                                         ERRO 1: "Temperatura" não é uma biblioteca

from conversores.temperatura import celsius_para_kelvin# converter_distancia ERRO 2: "converter_distancia" não existe na pasta conversores.

resultado = celsius_para_kelvin(25)                                        # ERRO 3: aqui a função não está sendo executada. Faltava passar um valor entre parênteses
print(f"25°C em K: {resultado}")

from utils.formatador import formatar_resultado
print(formatar_resultado("teste", 100, "km", 62.1, "mi"))                  # ERRO 4: a função formatar_resultado espera 5 argumentos

from conversores import km_para_milhas
print(f"50 km = {km_para_milhas(50):.2f} mi ")
