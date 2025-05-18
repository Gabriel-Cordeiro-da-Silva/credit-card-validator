"""
arquivo principal da aplicação Flask
para o validador de bandeiras de cartão de crédito
"""
from flask import Flask, render_template, request # importando Flask e módulos necessários
from validator import validar_cartao # importando a função de validação do cartão

app = Flask(__name__) # criando uma instância do Flask

@app.route('/', methods=['GET', 'POST']) # definindo a rota principal
def index(): # função para a rota principal
    resultado = None # variável para armazenar o resultado da validação
    if request.method == 'POST': # se o método for POST, significa que o formulário foi enviado
        numero_cartao = request.form['numero_cartao'] # obtendo o número do cartão do formulário
        resultado = validar_cartao(numero_cartao) # chamando a função de validação do cartão
    return render_template('index.html', resultado=resultado) # renderizando o template index.html com o resultado da validação

if __name__ == '__main__': 
    app.run(debug=True) # iniciando a aplicação Flask em modo de depuração
# para que possamos ver os erros diretamente no navegador
# para executar a aplicação, use o comando: python app.py
# e acesse http://