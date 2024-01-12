from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Loja(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)

class Cartao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    saldo = db.Column(db.Float, default=0.0, nullable=False)

class Transacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    loja_id = db.Column(db.Integer, db.ForeignKey('loja.id'), nullable=False)
    cartao_id = db.Column(db.Integer, db.ForeignKey('cartao.id'), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    data = db.Column(db.DateTime, nullable=False)

    # Adicionando relação muitos para um com as tabelas Loja e Cartao
    loja = db.relationship('Loja', backref=db.backref('transacoes', lazy=True))
    cartao = db.relationship('Cartao', backref=db.backref('transacoes', lazy=True))
