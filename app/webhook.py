# app/webhook.py
from flask import Blueprint, request, jsonify
from datetime import datetime
import requests
from .models import Pessoa
from . import db

bp = Blueprint('webhook', __name__)

# Token e cabeçalhos fornecidos
TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjb21wYW55X2lkIjoiNjY0Mjc0OTc3ZmM4YmEwNTMzMmQyZjBjIiwiY3VycmVudF90aW1lIjoxNzMzNDMwMzg3NDcxLCJleHAiOjIwNDg5NjMxODd9.9kdeolnmsr2zRUeZQoOqL_FOppMAqFoC1zJqbo4769M"
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": f"Bearer {TOKEN}"
}
TEMPLATE_ID = "679a0ab6c8825d82fe8273ff"
EXECUTION_COMPANY_ID = "664274977fc8ba05332d2f0c"

@bp.route('/webhook', methods=['POST'])
def receber_dados():
    """
    Recebe dados via webhook e envia idade para API externa
    ---
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            nome:
              type: string
            nascimento:
              type: string
              example: "1995-08-15"
            form_id:
              type: string
    responses:
      200:
        description: Idade enviada com sucesso
    """
    data = request.json
    nome = data.get('nome')
    nascimento = data.get('nascimento')

    data_nasc = datetime.strptime(nascimento, '%Y-%m-%d')
    hoje = datetime.today()
    idade = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))


    form_id = data.get('form_id') 
    if not form_id:
        return jsonify({'error': 'form_id não fornecido'}), 400

    payload = {
        "form_id": form_id,
        "fields": [
            {
                "field": "idade",
                "value": idade
            }
        ]
    }

    url = "https://app.way-v.com/api/integration/checklists"
    response = requests.post(url, json=payload, headers=HEADERS)

    return jsonify({
        "idade": idade,
        "status_envio": response.status_code
    })
