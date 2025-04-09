from flask import Blueprint, request, jsonify
import pandas as pd
from .models import Pessoa
from . import db
from datetime import datetime

bp = Blueprint('routes', __name__)

@bp.route('/inserir_excel', methods=['POST'])
def inserir_excel():
    file = request.files['file']
    if not file:
        return jsonify({'error': 'Arquivo excel não enviado'}), 400
    
    df = pd.read_excel(file)
    for _, row in df.iterrows():
        pessoa = Pessoa(
            nome=row['Nome completo'],
            nascimento=row['Data de Nascimento'],
            sexo=row['Sexo'],
            email=row['E-mail'],
            telefone=row['Celular'] 
        )
        print(df.columns)
        db.session.add(pessoa)
    db.session.commit()
    return jsonify({'message': 'Dados inseridos com sucesso'}), 200

@bp.route('/listar', methods=['GET'])
def listar():
    sexo = request.args.get('sexo')
    query = Pessoa.query
    if sexo:
        query = query.filter(sexo == sexo)
    pessoas = query.all()
    return jsonify([
        {
            'id': p.id,
            'nome': p.nome,
            'nascimento': p.nascimento.strftime('%d/%m/%Y'),
            'sexo': p.sexo,
            'email': p.email,
            'telefone': p.telefone
        } for p in pessoas
    ])

@bp.route('/atualizar/<int:id>', methods=['PUT'])
def atualizar(id):
    data = request.json
    pessoa = Pessoa.query.get(id)
    if not pessoa:
        return jsonify({'error': 'Pessoa não encontrada'}), 404

    pessoa.nascimento = datetime.strptime(data['nascimento'], "%Y-%m-%d").date()
    db.session.commit()
    return jsonify({'message': 'Data de nascimento atualizada com sucesso'})

@bp.route('/deletar_todos', methods=['DELETE'])
def deletar_todos():
    Pessoa.query.delete()
    db.session.commit()
    return jsonify({'message': 'Todos os registros foram deletados'}), 200