### 1. Lista de Tarefas Simples

- **Backend (FastAPI)**: Rotas GET /tasks (listar), POST /tasks (criar: título, descrição), PUT /tasks/{id} (marcar feito), DELETE /tasks/{id}. Use SQLAlchemy para modelo Task (id, título, descrição, feito: bool).
- **Banco**: PostgreSQL com tabela tasks. Conexão via asyncpg ou SQLAlchemy async.
- **Frontend (React)**: Página com lista de tarefas (useState para array), formulário add (fetch POST), botões check/delete (fetch PUT/DELETE). Use useEffect para fetch inicial.
- **Docker**: Compose com serviços: db (postgres:alpine, env: POSTGRES_DB, USER, PASSWORD), api (build: ., command: uvicorn main:app --reload, depends_on: db, env: DATABASE_URL=postgresql://user:pass@db/dbname).
- **Rodar**: docker compose up; API em localhost:8000, React em Vite (npm run dev).

### 2. Cadastro + Login Básico

- **Backend**: Rotas POST /register (email, senha: hash com Argon2), POST /login (verifica hash, retorna JWT). Use PyJWT para token (secret_key). Modelo User (id, email, hashed_password).
- **Banco**: Tabela users.
- **Frontend**: Telas login/register (forms com fetch POST), armazena token no localStorage. Após login, mostra "Bem-vindo, {email}!" (fetch GET /me protegido por header Authorization: Bearer {token}).
- **Docker**: Adicione ao compose: volumes para persistência db, api com deps para passlib[argon2], pyjwt.
- **Segurança**: JWT expira em 30min; valida com depends_on_current_user.

### 3. Perfil do Usuário

- **Backend**: Extensão do login: GET /me (retorna user info), PUT /me (atualiza email/nome, re-hash senha se mudada). Protegido por JWT.
- **Banco**: Adicione coluna nome em users.
- **Frontend**: Após login, página perfil com form edit (pré-preenchido via GET /me, submit PUT). useState para form data.
- **Docker**: Mesma base, adicione env SECRET_KEY para JWT.
- **Extra**: Validação email único no register.

### 4. Lista de Compras Compartilhada

- **Backend**: Após login, rotas para items: GET/POST/PUT/DELETE /items (item: nome, quantidade, comprado: bool). Filtre por user_id.
- **Banco**: Tabela items (id, user_id FK, nome, qtd, comprado).
- **Frontend**: Lista itens (fetch GET com token), add form, botões comprar/delete.
- **Docker**: Mesmo compose; api volumes para código.
- **Compartilhado**: Opcional: rota share via link público read-only (sem JWT para GET).

### 5. Diário Pessoal

- **Backend**: Rotas POST /entries (data, texto), GET /entries (lista por user), DELETE /entries/{id}. Protegido JWT.
- **Banco**: Tabela entries (id, user_id, data: date, texto).
- **Frontend**: Lista entradas (ordenada por data), form nova entrada, delete botão.
- **Docker**: Adicione date handling com datetime.
- **Simples**: Sem edit, só create/read/delete.

### 6. Gerenciador de Contatos

- **Backend**: CRUD /contacts (nome, telefone, email). Protegido, filtro por user.
- **Banco**: Tabela contacts (id, user_id, nome, tel, email).
- **Frontend**: Tabela ou lista contatos, form add/edit, delete.
- **Docker**: Base igual, use Pydantic para validação (email validator opcional).
- **Busca**: Adicione query param para filtro nome.
