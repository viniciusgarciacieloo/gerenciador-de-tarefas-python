# Gerenciador de Tarefas (To-Do List)

Projeto desenvolvido em Python com o objetivo de praticar fundamentos de programação e evoluir gradualmente para uma aplicação Full Stack.

Este projeto faz parte do meu processo de aprendizado em Engenharia de Software, com foco em desenvolvimento Back-end. A ideia é começar com uma aplicação simples de terminal e evoluí-la para uma aplicação Web completa utilizando FastAPI, banco de dados e tecnologias de Front-end.

---

## Funcionalidades

Atualmente o sistema permite:

- Adicionar tarefas
- Listar tarefas
- Concluir tarefas
- Remover tarefas
- Geração automática de IDs
- Evitar tarefas duplicadas
- Persistência de dados em JSON
- Carregamento automático das tarefas ao iniciar o programa

---

## Tecnologias Utilizadas

- Python 3
- JSON
- Dataclasses

---

## Como Executar

Clone o repositório:

```bash
git clone https://github.com/viniciusgarciacieloo/Projetos.git
```

Entre na pasta do projeto:

```bash
cd Projetos
```

Execute o programa:

```bash
python Tarefas.py
```

---

## Exemplo de Utilização

```text
==============================
           TAREFAS
==============================

[1] Adicionar Tarefa
[2] Listar Tarefas
[3] Concluir Tarefa
[4] Remover Tarefa
[5] Sair

Digite a opção desejada:
```

Exemplo de saída:

```text
ID: 1
Título: Estudar Python
Status: Pendente

ID: 2
Título: Estudar Git
Status: Concluído
```

---

## Estrutura das Tarefas

Cada tarefa possui os seguintes atributos:

- ID
- Título
- Status

Exemplo:

```text
ID: 1
Título: Estudar Python
Status: Pendente
```

---

## Armazenamento dos Dados

As tarefas são armazenadas localmente em um arquivo JSON.

Exemplo:

```json
[
    {
        "id": 1,
        "titulo": "Python",
        "status": "Pendente"
    },
    {
        "id": 2,
        "titulo": "Git",
        "status": "Concluído"
    }
]
```

Isso permite que as tarefas continuem disponíveis mesmo após o encerramento do programa.

---

## Conceitos Praticados

Este projeto foi utilizado para praticar:

- Variáveis
- Tipos de dados
- Listas
- Dicionários
- Funções
- Condicionais
- Laços de repetição
- Dataclasses
- Manipulação de arquivos
- JSON
- Tratamento básico de erros
- Organização de código
- Git
- GitHub

---

## Estrutura Atual do Projeto

```text
Projetos/
│
├── Tarefas.py
├── tarefas.json
├── README.md
└── teste.py
```

---

## Próximos Passos

### Melhorias na versão de terminal

- [ ] Refatoração do código
- [ ] Melhor organização das funções
- [ ] Melhor tratamento de erros
- [ ] Prioridade das tarefas
- [ ] Categorias
- [ ] Data de criação
- [ ] Prazo de conclusão

### Evolução para aplicação Web

- [ ] HTML
- [ ] CSS
- [ ] JavaScript
- [ ] FastAPI
- [ ] SQLite
- [ ] PostgreSQL

### Evolução para API REST

- [ ] GET /tarefas
- [ ] GET /tarefas/{id}
- [ ] POST /tarefas
- [ ] PUT /tarefas/{id}
- [ ] DELETE /tarefas/{id}

### Melhorias profissionais

- [ ] Autenticação de usuários
- [ ] Login e cadastro
- [ ] Senhas com hash
- [ ] Testes automatizados
- [ ] Docker
- [ ] GitHub Actions
- [ ] Deploy

---

## Objetivo do Projeto

O objetivo deste projeto não é apenas criar uma To-Do List, mas construir gradualmente uma aplicação que demonstre conhecimentos em:

```text
Python
    ↓
FastAPI
    ↓
API REST
    ↓
SQLite/PostgreSQL
    ↓
HTML/CSS/JavaScript
    ↓
Git/GitHub
    ↓
Testes
    ↓
Docker
    ↓
Deploy
```

A cada nova etapa o projeto será evoluído para refletir conceitos mais avançados de desenvolvimento de software.

---

## Autor

Desenvolvido por Vinicius Garcia Del Cielo como parte dos estudos de Engenharia de Software e preparação para oportunidades de estágio em desenvolvimento de software.
