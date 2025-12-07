# Projeto Desafio: Sistema de Usuários

Este é um projeto backend + frontend desenvolvido como **desafio de criação de usuários**, organizado seguindo **DDD (Domain-Driven Design) + Clean Architecture**, utilizando **FastAPI** no backend e **React/Vite** no frontend.

---

## 📝 Objetivo

- Criar um sistema simples para gerenciar usuários.
- Seguir boas práticas de arquitetura (DDD + Clean Architecture).
- Preparar o projeto para futura evolução em microserviços.
- Integrar backend e frontend usando Docker.

---

## ⚙️ Ferramentas e Tecnologias

### Backend

- Python 3.12
- FastAPI – Framework para APIs REST
- SQLAlchemy – ORM para manipulação do banco de dados
- PostgreSQL – Banco de dados relacional
- psycopg2-binary – Driver PostgreSQL para Python
- asyncpg – Driver assíncrono PostgreSQL (opcional para async)
- Pydantic – Validação e serialização de dados
- Passlib[argon2] – Hashing de senhas
- PyJWT – Autenticação via JWT
- python-dotenv – Carregamento de variáveis de ambiente
- Uvicorn[standard] – Servidor ASGI para rodar FastAPI

### Frontend

- React – Biblioteca para interface de usuário
- Vite – Bundler moderno para React (ou Next.js opcional)
- Node.js / npm – Gerenciador de pacotes e execução do frontend

### DevOps / Ferramentas Auxiliares

- Docker – Containerização do backend e frontend
- docker-compose – Orquestração de containers
- Git – Controle de versão
- VS Code – IDE recomendada

---

## 📁 Estrutura do Projeto

```

meu-projeto/
├── backend/
│ ├── src/
│ │ ├── domain/ ← Regras de negócio puras
│ │ ├── application/ ← Casos de uso
│ │ ├── interfaces/ ← Rotas e schemas
│ │ ├── infrastructure/ ← Banco e serviços externos
│ │ └── config/ ← Configurações do projeto (.env)
│ ├── main.py ← Entrypoint FastAPI
│ ├── Dockerfile ← Docker backend
│ └── requirements.txt ← Dependências Python
│
├── frontend/
│ ├── src/ ← Código fonte React
│ ├── public/ ← Assets estáticos
│ ├── package.json ← Dependências e scripts Node
│ └── vite.config.ts ← Configuração Vite
│
├── docker-compose.yml ← Orquestração containers
├── .gitignore
├── .dockerignore
└── README.md

```

---

## 🚀 Como rodar o projeto

### Pré-requisitos

- Docker e docker-compose instalados
- Python 3.12 (caso rode backend local sem Docker)
- Node.js e npm (para frontend)

### Rodando com Docker

```bash
# No diretório raiz do projeto
docker-compose up --build
```

- Backend: `http://localhost:8000`
- Frontend: `http://localhost:5173` (Vite padrão)

### Rodando apenas backend local (sem Docker)

```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Linux / Mac
.venv\Scripts\activate     # Windows
pip install -r requirements.txt
uvicorn src.main:app --reload
```

### Rodando frontend local

```bash
cd frontend
npm install
npm run dev
```

---

## 🧩 Próximos passos / Evoluções

- Implementar autenticação JWT completa
- Criar testes unitários por camada (domain, application, infrastructure)
- Evoluir para microserviços (ex: separar usuários e tarefas)
- Integrar frontend com backend via API
- Implementar Docker para CI/CD

---

## 📄 Referências

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [React](https://reactjs.org/)
- [Vite](https://vitejs.dev/)
- [DDD + Clean Architecture](https://8thlight.com/blog/uncle-bob/2012/08/13/the-clean-architecture.html)
