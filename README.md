# API Wayv – Processo Seletivo

API desenvolvida com Flask e SQLite para ingestão, listagem, atualização e integração de dados de usuários, conforme especificações do processo seletivo.

---

## 🚀 Tecnologias

- Python 3.12
- Flask
- SQLAlchemy
- Pandas
- SQLite
- Swagger UI

---

## 📦 Instalação e execução

```bash
# Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Inicialize o banco de dados
python init_db.py

# Rode o servidor
python main.py
```

---

## 📘 Endpoints

### `POST /inserir_excel`

Recebe um arquivo `.xlsx` com os dados dos usuários e os insere no banco.


---

### `GET /listar`

Retorna todos os registros inseridos no banco.

---

### `PUT /atualizar/<id>`

Atualiza a data de nascimento de um registro pelo ID.



---

### `DELETE /deletar_todos`

Remove todos os registros da tabela no banco de dados.

---

### `POST /webhook`

Recebe dados de nome, nascimento e form_id e envia a idade calculada para uma API externa (de teste).



---

## ✅ Swagger

A documentação interativa dos endpoints estará disponível em:

```
http://127.0.0.1:5000/apidocs
```

Implementada com [Flasgger](https://github.com/flasgger/flasgger)

---


## 👤 Desenvolvido por

Larissa Alves  
[GitHub: @larissa04alves](https://github.com/larissa04alves)

