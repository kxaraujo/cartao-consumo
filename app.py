from flask import Flask, render_template, redirect, url_for, request
from models import db, Cartao, Transacao, Loja
from datetime import datetime
from secret_key import SECRET_KEY

app = Flask(__name__)
app.secret_key = SECRET_KEY

# Configurações do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cartao_consumo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa a extensão do SQLAlchemy
db.init_app(app)

# Definindo as rotas

# Rota principal
@app.route('/')
def index():
    lojas = Loja.query.all()
    cartao = Cartao.query.first()
    return render_template('index.html', lojas=lojas, cartao=cartao)

# Rota para comprar
@app.route('/comprar/<loja_id>', methods=['POST'])
def comprar(loja_id):
    cartao_id = request.form['cartao_id']
    valor_compra = float(request.form['valor_compra'])

    # Verifica se há saldo suficiente para a compra
    cartao = Cartao.query.get(cartao_id)
    if cartao.saldo >= valor_compra:
        # Atualiza o saldo do cartão
        cartao.saldo -= valor_compra

        # Registra a transação
        transacao = Transacao(loja_id=loja_id, cartao_id=cartao_id, valor=valor_compra, data=datetime.now())
        db.session.add(transacao)
        db.session.commit()

    return redirect(url_for('index'))

# Rota para adicionar saldo
@app.route('/adicionar_saldo/<cartao_id>', methods=['POST'])
def adicionar_saldo(cartao_id):
    valor_saldo = float(request.form['valor_saldo'])

    # Atualiza o saldo do cartão
    cartao = Cartao.query.get(cartao_id)
    cartao.saldo += valor_saldo

    # Registra a transação
    transacao = Transacao(cartao_id=cartao_id, valor=valor_saldo, data=datetime.now())
    db.session.add(transacao)
    db.session.commit()

    return redirect(url_for('index'))

# Rota para o histórico de compras
@app.route('/historico/<cartao_id>')
def historico(cartao_id):
    historico_compras = Transacao.query.filter_by(cartao_id=cartao_id).all()
    return render_template('historico.html', historico_compras=historico_compras)

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
        # Adiciona alguns dados de exemplo ao banco de dados
        loja1 = Loja(nome='Loja 1')
        loja2 = Loja(nome='Loja 2')
        db.session.add_all([loja1, loja2])
        db.session.commit()

        cartao = Cartao(saldo=100.0)
        db.session.add(cartao)
        db.session.commit()

    app.run(debug=True)
