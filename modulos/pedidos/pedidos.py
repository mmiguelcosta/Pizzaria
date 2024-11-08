from flask import Blueprint, render_template, request, redirect, flash
from database import db
from models import Pedido, Usuario, Pizza

bp_pedido = Blueprint('pedidos', __name__, template_folder='templates')

@bp_pedido.route('/')
def index():
    p = Pedido.query.all()
    return render_template('pedido.html', pedidos=p)

@bp_pedido.route('/add')
def add():
    u = Usuario.query.all()
    p = Pizza.query.all()
    return render_template('pedido_add.html', usuarios=u, pizzas=p)

@bp_pedido.route('/save', methods=['POST'])
def save():
    usuario_id = request.form.get('usuario_id')
    pedido_id = request.form.get('pizza_id')
    data = request.form.get('data')
    if usuario_id and pedido_id and data:
        objeto = Pedido(usuario_id, pedido_id, data)
        db.session.add(objeto)
        db.session.commit()
        flash('pedido salvo')
        return redirect('/pedidos')
    else:
        flash('Preencha todos os campos')
        return redirect('/pedidos/add')


