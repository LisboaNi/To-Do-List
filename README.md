# Taskly (To-Do-List)

Este repositório contém o projeto Taskly na qual seria uma lista de tarefas (To-Do-List), projeto simples com o objetivo de práticar **Padrões de Projeto com Python**, principalmente o **MVC (Model-View-Controller)**. O projeto é simples, mas funcional, permitindo organizar, acompanhar e atualizar tarefas do dia a dia.

No diretório principal a `src` possui conjuntos como:
1. **core**: Configurações e conexão com o banco de dados.
2. **utils**: Classes base, funções utilitárias e tratamento de erros
3. **models**: Definição dos atributos e métodos das entidades (Tasks).
4. **controllers**: Implementação do CRUD e manipulação dos dados.
5. **views**: Templates HTML da interface, utilizando Bootstrap 5.

O arquivo `manage.py` inicializa a aplicação e configura as rotas do servidor.

<br>

## Tecnologias 
- Python
- SQLite3
- Bootstrap 5

<br>

## Inicializando o Projeto

Para executar o projeto, siga os passos abaixo:

### 1. Entrar no diretório
```bash
cd src
```

### 2. Criar e ativar o ambiente virtual
```bash
python -m venv env
env\Scripts\activate
```
### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Rodar o projeto
```bash
python manage.py
```