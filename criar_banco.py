import sqlite3
import random
from datetime import datetime, timedelta

conn = sqlite3.connect("distribuidor.db")
cursor = conn.cursor()

# Criação das tabelas
cursor.executescript("""
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        categoria TEXT NOT NULL,
        marca TEXT NOT NULL,
        preco_unitario REAL NOT NULL
    );

    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        cidade TEXT NOT NULL,
        estado TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS vendedores (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        regiao TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS vendas (
        id INTEGER PRIMARY KEY,
        data TEXT NOT NULL,
        cliente_id INTEGER NOT NULL,
        vendedor_id INTEGER NOT NULL,
        produto_id INTEGER NOT NULL,
        quantidade INTEGER NOT NULL,
        valor_total REAL NOT NULL,
        FOREIGN KEY (cliente_id) REFERENCES clientes(id),
        FOREIGN KEY (vendedor_id) REFERENCES vendedores(id),
        FOREIGN KEY (produto_id) REFERENCES produtos(id)
    );
""")

# Dados fictícios
produtos = [
    ("Shampoo Hidratante 400ml", "Higiene", "Natura", 18.90),
    ("Condicionador Reparador 400ml", "Higiene", "Natura", 19.90),
    ("Perfume Floral 100ml", "Perfumaria", "O Boticário", 129.90),
    ("Perfume Masculino 50ml", "Perfumaria", "Avon", 89.90),
    ("Creme Hidratante Corporal 250ml", "Cosméticos", "Nivea", 24.90),
    ("Protetor Solar FPS 50 200ml", "Cosméticos", "Sundown", 39.90),
    ("Batom Matte", "Cosméticos", "Maybelline", 34.90),
    ("Base Líquida", "Cosméticos", "L'Oréal", 59.90),
    ("Desodorante Aerossol 150ml", "Higiene", "Rexona", 14.90),
    ("Sabonete Líquido 250ml", "Higiene", "Dove", 12.90),
    ("Sérum Facial 30ml", "Cosméticos", "Neutrogena", 89.90),
    ("Tônico Capilar 200ml", "Higiene", "Pantenê", 29.90),
    ("Perfume Feminino 75ml", "Perfumaria", "Eudora", 99.90),
    ("Esfoliante Corporal 200ml", "Cosméticos", "The Body Shop", 49.90),
    ("Creme para Mãos 75ml", "Cosméticos", "Hidra", 9.90),
]

clientes = [
    ("Farmácia Central", "São Paulo", "SP"),
    ("Drogaria Norte", "Campinas", "SP"),
    ("Beleza Total", "Rio de Janeiro", "RJ"),
    ("Cosméticos Bela", "Belo Horizonte", "MG"),
    ("Perfumaria Elite", "Curitiba", "PR"),
    ("Farmácia Sul", "Porto Alegre", "RS"),
    ("Loja da Beleza", "Salvador", "BA"),
    ("Distribuidora Leste", "Recife", "PE"),
    ("Mega Farma", "Fortaleza", "CE"),
    ("Beleza & Cia", "Manaus", "AM"),
]

vendedores = [
    ("Ana Silva", "Sudeste"),
    ("Carlos Mendes", "Sul"),
    ("Fernanda Lima", "Nordeste"),
    ("Roberto Costa", "Norte"),
    ("Patricia Souza", "Centro-Oeste"),
]

cursor.executemany("INSERT INTO produtos (nome, categoria, marca, preco_unitario) VALUES (?,?,?,?)", produtos)
cursor.executemany("INSERT INTO clientes (nome, cidade, estado) VALUES (?,?,?)", clientes)
cursor.executemany("INSERT INTO vendedores (nome, regiao) VALUES (?,?)", vendedores)

# Gera 500 vendas fictícias nos últimos 12 meses
data_inicio = datetime.now() - timedelta(days=365)
for _ in range(500):
    data = data_inicio + timedelta(days=random.randint(0, 365))
    cliente_id = random.randint(1, 10)
    vendedor_id = random.randint(1, 5)
    produto_id = random.randint(1, 15)
    quantidade = random.randint(1, 20)

    cursor.execute("SELECT preco_unitario FROM produtos WHERE id = ?", (produto_id,))
    preco = cursor.fetchone()[0]
    valor_total = round(preco * quantidade, 2)

    cursor.execute(
        "INSERT INTO vendas (data, cliente_id, vendedor_id, produto_id, quantidade, valor_total) VALUES (?,?,?,?,?,?)",
        (data.strftime("%Y-%m-%d"), cliente_id, vendedor_id, produto_id, quantidade, valor_total)
    )

conn.commit()
conn.close()
print("✅ Banco de dados criado com sucesso! 500 vendas geradas.")