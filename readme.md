# Projeto Desafio: Sistema de Usuários

Projeto full-stack (backend + frontend) para gerenciamento de usuários, com arquitetura em camadas escalável usando **FastAPI** (backend) e **React + Vite** (frontend).

---

## 📝 Objetivo

- Criar um sistema simples de cadastro e gerenciamento de usuários
- Aplicar boas práticas de organização e separação de responsabilidades
- Preparar o projeto para evoluir para microserviços no futuro
- Rodar tudo com Docker

---

## ⚙️ Tecnologias

### Backend

- Python 3.12
- FastAPI
- SQLAlchemy + PostgreSQL
- Pydantic
- PyJWT + Passlib (Argon2)
- python-dotenv
- Uvicorn

### Frontend

- React
- Vite
- Node.js / npm

### DevOps

- Docker + docker-compose

---

## 🚀 Como rodar

### Com Docker (recomendado)

```bash
docker-compose up --build
```

- Backend: http://localhost:8000
- Frontend: http://localhost:5173

### Backend local

```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # ou .venv\Scripts\activate no Windows
pip install -r requirements.txt
uvicorn src.main:app --reload
```

### Frontend local

```bash
cd frontend
npm install
npm run dev
```

---

## Próximos passos

- Autenticação JWT completa
- Testes unitários e de integração
- Separação em microserviços
- CI/CD com Docker

---

## 📄 Referências

- [FastAPI](https://fastapi.tiangolo.com/)
- [React](https://reactjs.org/)
- [Vite](https://vitejs.dev/)

Pronto. Simples, verdadeiro e profissional.
