# 📚 API de Livros com Flask

API REST desenvolvida em **Python** utilizando o framework **Flask**, com operações CRUD para gerenciamento de livros.

O projeto foi desenvolvido com o objetivo de praticar os fundamentos da criação de APIs REST, incluindo **rotas, métodos HTTP, requisições JSON e códigos de status HTTP**.

## 🚀 Tecnologias

* Python
* Flask
* JSON
* API REST

## 📌 Funcionalidades

A API permite:

* 📖 Consultar todos os livros
* 🔎 Consultar um livro pelo ID
* ✏️ Editar um livro
* 🗑️ Excluir um livro

Os dados são armazenados temporariamente em uma lista Python, portanto, **não há banco de dados neste projeto**.

## 📂 Estrutura

```text
.
├── app.py
└── README.md
```

## ⚙️ Como executar

### 1. Clone o repositório

```bash
git clone <URL_DO_REPOSITORIO>
```

### 2. Entre na pasta do projeto

```bash
cd <NOME_DA_PASTA>
```

### 3. Instale o Flask

```bash
pip install flask
```

### 4. Execute a aplicação

```bash
python app.py
```

A API será iniciada em:

```text
http://localhost:5000
```

## 🔗 Endpoints

### GET `/livros`

Retorna todos os livros cadastrados.

**Exemplo de resposta:**

```json
[
    {
        "id": 1,
        "titulo": "O Senhor dos Anéis",
        "autor": "J.R.R. Tolkien"
    },
    {
        "id": 2,
        "titulo": "Harry Potter e a Pedra Filosofal",
        "autor": "J.K. Rowling"
    },
    {
        "id": 3,
        "titulo": "O Pequeno Príncipe",
        "autor": "Antoine de Saint-Exupéry"
    }
]
```

---

### GET `/livros/<id>`

Retorna um livro específico através do seu ID.

**Exemplo:**

```http
GET /livros/1
```

**Resposta:**

```json
{
    "id": 1,
    "titulo": "O Senhor dos Anéis",
    "autor": "J.R.R. Tolkien"
}
```

Caso o livro não seja encontrado:

```json
{
    "mensagem": "Livro não encontrado"
}
```

Status HTTP:

```text
404 Not Found
```

---

### PUT `/livros/<id>`

Atualiza os dados de um livro existente.

**Exemplo:**

```http
PUT /livros/1
```

**Body:**

```json
{
    "titulo": "O Senhor dos Anéis - Edição Especial",
    "autor": "J.R.R. Tolkien"
}
```

A API retorna o livro atualizado.

---

### DELETE `/livros/<id>`

Exclui um livro através do seu ID.

**Exemplo:**

```http
DELETE /livros/1
```

**Resposta:**

```json
{
    "mensagem": "Livro excluído com sucesso"
}
```

Caso o livro não exista:

```json
{
    "mensagem": "Livro não encontrado"
}
```

Status HTTP:

```text
404 Not Found
```

## 🧪 Testando a API

A API pode ser testada utilizando ferramentas como:

* Postman
* Insomnia
* Thunder Client
* `curl`

Exemplo utilizando `curl`:

```bash
curl http://localhost:5000/livros
```

Para buscar um livro específico:

```bash
curl http://localhost:5000/livros/1
```

## 📚 Conceitos praticados

Este projeto permite praticar conceitos fundamentais de desenvolvimento de APIs:

* Criação de uma aplicação Flask
* Definição de rotas
* Métodos HTTP
* GET, PUT e DELETE
* Parâmetros de rota
* Requisições JSON
* Respostas JSON
* Códigos de status HTTP
* Operações CRUD
* Manipulação de listas e dicionários em Python

## 🔮 Próximos passos

Possíveis melhorias para evoluir o projeto:

* [ ] Adicionar criação de novos livros com `POST`
* [ ] Utilizar banco de dados
* [ ] Adicionar validação dos dados recebidos
* [ ] Implementar tratamento de erros
* [ ] Criar testes automatizados
* [ ] Organizar o projeto em diferentes módulos
* [ ] Criar documentação da API com Swagger/OpenAPI
* [ ] Adicionar autenticação
* [ ] Criar um arquivo `requirements.txt`

## 👩‍💻 Objetivo

Projeto desenvolvido para estudo e prática de **Python, Flask e desenvolvimento de APIs REST**, servindo como parte do meu portfólio de desenvolvimento backend.
