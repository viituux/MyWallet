from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Configuração do Banco
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///carteira.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo
class Transacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    tipo = db.Column(db.String(10), nullable=False)
    data = db.Column(db.DateTime, default=datetime.utcnow)

# --- NOVIDADE: Filtro para formatar dinheiro (R$ 1.000,00) ---
@app.template_filter('moeda_br')
def moeda_br(valor):
    # Formata para padrão brasileiro: vírgula no decimal, ponto no milhar
    return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

@app.route("/", methods=["GET", "POST"])
def index():
    # SALVAR (POST)
    if request.method == "POST":
        descricao = request.form.get("descricao")
        valor = float(request.form.get("valor"))
        tipo = request.form.get("tipo")

        nova_transacao = Transacao(descricao=descricao, valor=valor, tipo=tipo)
        
        db.session.add(nova_transacao)
        db.session.commit()
        return redirect(url_for("index"))

    # EXIBIR (GET)
    transacoes = Transacao.query.order_by(Transacao.data.desc()).all()
    
    total_entradas = sum(t.valor for t in transacoes if t.tipo == 'entrada')
    total_saidas = sum(t.valor for t in transacoes if t.tipo == 'saida')
    saldo = total_entradas - total_saidas

    return render_template("index.html", transacoes=transacoes, 
                           saldo=saldo, entradas=total_entradas, saidas=total_saidas)

@app.route("/delete/<int:id>")
def delete(id):
    transacao = Transacao.query.get_or_404(id)
    db.session.delete(transacao)
    db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)