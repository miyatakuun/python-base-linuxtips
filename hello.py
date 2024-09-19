#!/usr/bin/env python3
"""
Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente, o programa exibe a mensagem
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Moisés Iatagan"
__license__ = "Unlicense"
# Dunder (double under)

import os
# Módulo tem a funcionalidade de ler variaveis de ambiente

current_language = os.getenv("LANG")[:5]
# padrão snake case, as VAR ligadas por underline

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour Monde!"    



print(msg) 
