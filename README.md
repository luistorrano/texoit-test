# Texo IT Development test
API RESTful para possibilitar a leitura da lista de indicados e vencedores
da categoria Pior Filme do Golden Raspberry Awards
## Instruções para execução do projeto

Clone o projeto para o diretório desejado:
```
git clone https://github.com/luistorrano/texoit-test.git
```

Execute o comando para instalação dos pacotes python necessários para execução do projeto:
```
pip3 install -r requirements.txt
```

Execute o comando para criação da database SQLite:
```
python3 create_database.py
```
Execute o comando para popular a database:
```
python3 populate_database.py
```
Execute o comando para execução dos testes:
```
python3 -m pytest
```
Execute o servidor de desenvolvimento da api:
```
python3 app.py
```
