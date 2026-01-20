# Habit Tracker API

API REST para gerenciamento de hábitos pessoais, permitindo que usuários criem hábitos, registrem o progresso diário e acompanhem estatísticas de consistência ao longo do tempo.

Este projeto foi desenvolvido com foco em **boas práticas de backend**, arquitetura organizada e regras de negócio realistas, sendo ideal para portfólio profissional.

---

## 🚀 Objetivo do Projeto

O objetivo da **Habit Tracker API** é fornecer uma base sólida de backend para aplicações de produtividade e bem-estar, permitindo:

* Cadastro e autenticação de usuários
* Criação e gerenciamento de hábitos
* Registro diário de progresso
* Histórico e métricas de consistência

O projeto foi pensado para crescer de forma incremental, permitindo futuras integrações com frontend web ou mobile.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.11+**
* **FastAPI** — framework web moderno e performático
* **SQLAlchemy** — ORM para acesso ao banco de dados
* **SQLite** — banco de dados inicial
* **JWT (JSON Web Token)** — autenticação segura
* **Alembic** — migrações de banco de dados
* **Uvicorn** — servidor ASGI
* **Pytest** (opcional) — testes automatizados

---

## 📁 Estrutura do Projeto

A estrutura de pastas e arquivos ainda está em fase de definição e será planejada conforme a evolução do projeto.

A ideia é iniciar com uma base simples e, à medida que novas funcionalidades forem sendo adicionadas, organizar o código seguindo boas práticas de arquitetura backend.

Essa abordagem permite maior flexibilidade e facilita refatorações conscientes durante o desenvolvimento.

---

## 🔐 Autenticação

A API utiliza **JWT (JSON Web Token)** para autenticação.

Fluxo básico:

1. Usuário se registra
2. Usuário realiza login
3. A API retorna um token JWT
4. O token deve ser enviado no header `Authorization` para acessar rotas protegidas

---

## 📌 Endpoints Principais

### Autenticação

```
POST /auth/register   # Cadastro de usuário
POST /auth/login      # Login e geração do token
```

### Usuários

```
GET /users/me         # Dados do usuário autenticado
```

### Hábitos

```
POST   /habits                 # Criar hábito
GET    /habits                 # Listar hábitos
PUT    /habits/{id}            # Atualizar hábito
DELETE /habits/{id}            # Remover hábito
```

### Progresso

```
POST /habits/{id}/check        # Marcar hábito como concluído no dia
GET  /habits/{id}/history     # Histórico do hábito
```

---

## 🧠 Regras de Negócio

* Um hábito pode ser marcado **apenas uma vez por dia**
* Hábitos inativos não podem receber novos registros
* O histórico de progresso não pode ser alterado manualmente
* O percentual de consistência é calculado automaticamente

Essas regras garantem integridade dos dados e refletem cenários reais de aplicação.

---

## ⚙️ Como Executar o Projeto

### 1️⃣ Clonar o repositório

```
git clone https://github.com/seu-usuario/habit-tracker-api.git
cd habit-tracker-api
```

### 2️⃣ Criar ambiente virtual

```
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3️⃣ Instalar dependências

```
pip install -r requirements.txt
```

### 4️⃣ Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```
SECRET_KEY=uma_chave_secreta
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 5️⃣ Executar a aplicação

```
uvicorn app.main:app --reload
```

A API estará disponível em:

```
http://localhost:8000
```

A documentação interativa pode ser acessada em:

```
http://localhost:8000/docs
```

---

## 🧪 Testes (Opcional)

Para executar os testes:

```
pytest
```

---

## 📈 Próximos Passos

* Implementar Docker
* Migrar para PostgreSQL
* Adicionar testes unitários e de integração
* Deploy em ambiente de produção
* Integração com frontend web ou mobile

---

## 👤 Autor

Desenvolvido por **Eduardo Almeida**
Formado em Análise e Desenvolvimento de Sistemas
Foco em Backend Python

---

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se à vontade para utilizar, estudar e evoluir este código.
