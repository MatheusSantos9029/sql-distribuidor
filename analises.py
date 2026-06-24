import sqlite3

conn = sqlite3.connect("distribuidor.db")
cursor = conn.cursor()

print("=" * 50)
print("📊 ANÁLISES - DISTRIBUIDORA DE COSMÉTICOS")
print("=" * 50)

# 1. Faturamento total
cursor.execute("SELECT SUM(valor_total) FROM vendas")
total = cursor.fetchone()[0]
print(f"\n💰 Faturamento total: R$ {total:,.2f}")

# 2. Faturamento por categoria
print("\n📦 Faturamento por categoria:")
cursor.execute("""
    SELECT p.categoria, SUM(v.valor_total) AS total
    FROM vendas v
    JOIN produtos p ON v.produto_id = p.id
    GROUP BY p.categoria
    ORDER BY total DESC
""")
for row in cursor.fetchall():
    print(f"   {row[0]}: R$ {row[1]:,.2f}")

# 3. Top 5 produtos mais vendidos
print("\n🏆 Top 5 produtos mais vendidos (em quantidade):")
cursor.execute("""
    SELECT p.nome, SUM(v.quantidade) AS qtd
    FROM vendas v
    JOIN produtos p ON v.produto_id = p.id
    GROUP BY p.nome
    ORDER BY qtd DESC
    LIMIT 5
""")
for row in cursor.fetchall():
    print(f"   {row[0]}: {row[1]} unidades")

# 4. Faturamento por vendedor
print("\n👤 Faturamento por vendedor:")
cursor.execute("""
    SELECT vd.nome, SUM(v.valor_total) AS total
    FROM vendas v
    JOIN vendedores vd ON v.vendedor_id = vd.id
    GROUP BY vd.nome
    ORDER BY total DESC
""")
for row in cursor.fetchall():
    print(f"   {row[0]}: R$ {row[1]:,.2f}")

# 5. Top 5 clientes por faturamento
print("\n🏪 Top 5 clientes por faturamento:")
cursor.execute("""
    SELECT c.nome, c.cidade, SUM(v.valor_total) AS total
    FROM vendas v
    JOIN clientes c ON v.cliente_id = c.id
    GROUP BY c.nome
    ORDER BY total DESC
    LIMIT 5
""")
for row in cursor.fetchall():
    print(f"   {row[0]} ({row[1]}): R$ {row[2]:,.2f}")

# 6. Faturamento por mês
print("\n📅 Faturamento por mês:")
cursor.execute("""
    SELECT strftime('%Y-%m', data) AS mes, SUM(valor_total) AS total
    FROM vendas
    GROUP BY mes
    ORDER BY mes
""")
for row in cursor.fetchall():
    print(f"   {row[0]}: R$ {row[1]:,.2f}")

# 7. Faturamento por região
print("\n🗺️  Faturamento por região:")
cursor.execute("""
    SELECT vd.regiao, SUM(v.valor_total) AS total
    FROM vendas v
    JOIN vendedores vd ON v.vendedor_id = vd.id
    GROUP BY vd.regiao
    ORDER BY total DESC
""")
for row in cursor.fetchall():
    print(f"   {row[0]}: R$ {row[1]:,.2f}")

conn.close()
print("\n" + "=" * 50)