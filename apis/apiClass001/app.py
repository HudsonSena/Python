# API - É um lugar paa disponibilizar recursos e/ou funcionalidades
# 1. Objetivo - criar uma api de disponibilidade a consulta, criação, edição e exclusão de livros.
# 2. URL base - localhost
# 3. Endpoints - 
    #- localhost/livros (GET)
    #- localhost/livros (POST)
    #- localhost/livros/id (GET)
    #- localhost/livros/id (PUT)
    #- locahhost/livros (DELETE)
# 4. Quais recursos - Livros

from flask import Flask
app = Flask(__name__)
