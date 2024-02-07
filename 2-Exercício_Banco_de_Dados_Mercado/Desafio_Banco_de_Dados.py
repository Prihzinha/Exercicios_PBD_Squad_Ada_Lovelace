#Exercício Gerenciamento Mercado:

import sqlite3

conexao = sqlite3.connect('Banco')
cursor = conexao.cursor()

#1. Criação das tabelas
# Utilizando SQL, crie as tabelas necessárias para armazenar as informações do sistema. Defina as chaves primárias e estrangeiras conforme apropriado.

cursor.execute('CREATE TABLE Clientes (id INT PRIMARY KEY, nome VARCHAR(100), telefone VARCHAR(15), endereco VARCHAR(255));')
cursor.execute('CREATE TABLE Fornecedores (id INT PRIMARY KEY, nome VARCHAR(100));')   
cursor.execute('CREATE TABLE Produtos (id INT PRIMARY KEY, nome VARCHAR(100), quantidade INT, fornecedor_id INT, FOREIGN KEY (fornecedor_id) REFERENCES Fornecedores(id));')
cursor.execute('CREATE TABLE Categorias (id INT PRIMARY KEY, nome VARCHAR(100));')
cursor.execute('CREATE TABLE Produto_Categoria (produto_id INT, categoria_id INT, PRIMARY KEY (produto_id, categoria_id), FOREIGN KEY (produto_id) REFERENCES Produtos(id), FOREIGN KEY (categoria_id) REFERENCES Categorias(id));')
cursor.execute('CREATE TABLE Transacoes (id INT PRIMARY KEY, data DATE, cliente_id INT, produto_id INT, quantidade INT, FOREIGN KEY (cliente_id) REFERENCES Clientes(id), FOREIGN KEY (produto_id) REFERENCES Produtos(id));')

#2. Inserção de Dados:
# Insira dados de exemplo nas tabelas para simular um ambiente de venda de eletrônicos. Certifique-se de incluir uma variedade de produtos e clientes;

cursor.execute('INSERT INTO Clientes (id,nome,telefone,endereco) VALUES (1, "Brunna", 123456789, "Rua A, 123")')
cursor.execute('INSERT INTO Clientes (id,nome,telefone,endereco) VALUES (2, "Jaqueline", 98989898, "Rua B, 456")')
cursor.execute('INSERT INTO Clientes (id,nome,telefone,endereco) VALUES (3, "Kássia", 87878787, "Rua C, 789")')
cursor.execute('INSERT INTO Clientes (id,nome,telefone,endereco) VALUES (4, "Luana", 16565656, "Rua D, 1010")')
cursor.execute('INSERT INTO Clientes (id,nome,telefone,endereco) VALUES (5, "Juliana", 45454545, "Rua E, 2020")')
cursor.execute('INSERT INTO Clientes (id,nome,telefone,endereco) VALUES (6, "Priscila", 121212121, "Rua F, 3030")')
cursor.execute('INSERT INTO Clientes (id,nome,telefone,endereco) VALUES (7, "Caroline", 232323233, "Rua G, 4040")')
cursor.execute('INSERT INTO Clientes (id,nome,telefone,endereco) VALUES (8, "Amanda", 123456654, "Rua H, 5050")')
cursor.execute('INSERT INTO Clientes (id,nome,telefone,endereco) VALUES (9, "Lorrane", 78998745, "Rua I, 6060")')
cursor.execute('INSERT INTO Clientes (id,nome,telefone,endereco) VALUES (10, "Shomara", 147852369, "Rua J, 7070")')
cursor.execute('INSERT INTO Clientes (id,nome,telefone,endereco) VALUES (11, "Melissa", 963258741, "Rua K, 8080")')

# Check de dados inseridos
dados = cursor.execute('SELECT * FROM Clientes')
for Cliente in dados:
    print(Cliente)

# Inserir dados de produtos com id, nome do produto, quantidade e id do fornecedor
cursor.execute('INSERT INTO Produtos VALUES (1, "PenDrive", 100, 1)')
cursor.execute('INSERT INTO Produtos VALUES (2, "Fone de Ouvido", 100, 2)')
cursor.execute('INSERT INTO Produtos VALUES (3, "Mouse", 100, 3)')
cursor.execute('INSERT INTO Produtos VALUES (4, "Teclado", 100, 4)')
cursor.execute('INSERT INTO Produtos VALUES (5, "Microfone", 100, 5)')

# Inserir dados dos fornecedores com id e nome do fornecedor
cursor.execute('INSERT INTO Fornecedores VALUES (1, "Queengston")')
cursor.execute('INSERT INTO Fornecedores VALUES (2, "Filcon")')
cursor.execute('INSERT INTO Fornecedores VALUES (3, "longetek")')
cursor.execute('INSERT INTO Fornecedores VALUES (4, "redifogo")')
cursor.execute('INSERT INTO Fornecedores VALUES (5, "raiperex")')

# Inserir categorias dos produtos com id e nome da categoria
cursor.execute('INSERT INTO Categorias VALUES (1, "HomeOffice");')
cursor.execute('INSERT INTO Categorias VALUES (2, "Gamer");')

# Inserir produtos em suas categorias
cursor.execute('INSERT INTO Produto_Categoria VALUES (1, 1)')
cursor.execute('INSERT INTO Produto_Categoria VALUES (2, 1)')
cursor.execute('INSERT INTO Produto_Categoria VALUES (3, 1)')
cursor.execute('INSERT INTO Produto_Categoria VALUES (4, 1)')
cursor.execute('INSERT INTO Produto_Categoria VALUES (5, 1)')
cursor.execute('INSERT INTO Produto_Categoria VALUES (1, 2)')
cursor.execute('INSERT INTO Produto_Categoria VALUES (2, 2)')
cursor.execute('INSERT INTO Produto_Categoria VALUES (3, 2)')
cursor.execute('INSERT INTO Produto_Categoria VALUES (4, 2)')
cursor.execute('INSERT INTO Produto_Categoria VALUES (5, 2)')

# Inserir uma transação de compras teste
# id da transação, data da compra, id do cliente, id do produto, quantidade, categoria
cursor.execute('INSERT INTO Transacoes VALUES (1, "2024-02-07", 1, 1, 10, 2)')

#3. Consultas SQL:
# Escrever consultas SQL para realizar as seguintes operações:
# Listar todos os produtos em estoque
estoque = cursor.execute('SELECT * FROM Produtos')
for Produtos in estoque:
    print(Produtos)

# Encontrar a venda teste realidas por pelo cliente 2
pesquisa = cursor.execute('SELECT * FROM Transacoes WHERE cliente_id = 1')
for Transacoes in pesquisa:
    print(Transacoes)

# Calcular o total de vendas por categoria de produto


# Identificar os produtos mais vendidos.



#4. Atualizações e Exclusões:
# Escreva consultas SQL para atualizar e excluir registros do banco de dados, por exemplo, para atualizar a quantidade em estoque após uma venda ou remover um cliente

# alterar tabela Transações adicionando uma coluna
cursor.execute('ALTER TABLE Transacoes ADD COLUMN categoria INT')

# alterar o primeiro registro de cliente de João para Brunna
cursor.execute('UPDATE Clientes SET nome="Brunna" WHERE nome="João"')

# alterar quantidade em estoque do Produto "PenDrive" usando id
cursor.execute('UPDATE Produtos SET quantidade=110 WHERE id=1')

# exclusão do id = 1
cursor.execute('DELETE FROM Clientes WHERE id = 1')

