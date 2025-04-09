import re
from Flask import Blueprint, request, jsonify
from datetime import datetime
from .models import Pessoa
from . import db

bp = Blueprint('webhook', __name__)

@bp.route('/webhook', methods=['POST'])
def receber_dados():
    data=request.json
    nome=data.get('nome')
    nascimento=data.get('nascimento')

    data_nasc = datetime.strptime(nascimento, '%Y/%m/%d')
    hoje = datetime.today()
    idade = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))

    pessoa = Pessoa.query.filter_by(nome=nome).first()
    if pessoa:
        pessoa.nascimento = nascimento
        db.session.commit()

    return jsonify({'idade': idade})