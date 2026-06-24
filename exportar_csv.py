import sqlite3
import csv

conn = sqlite3.connect("distribuidor.db")
cursor = conn.cursor()

# Exporta visão completa de vendas para o Power BI
cursor.execute("""
    SELECT
        v.id,
        v.data,
        c.nome AS cliente,
        c.cidade,
        c.estado,
        vd.nome AS vendedor,
        vd.regiao,
        p.nome AS produto,
        p.categoria,
        p.marca,
        p.preco_unitario,
        v.quantidade,
        v.valor_total
    FROM vendas v
    JOIN clientes c ON v.cliente_id = c.id
    JOIN vendedores vd ON v.vendedor_id = vd.id
    JOIN produtos p ON v.produto_id = p.id
    ORDER BY v.data
""")

colunas = [desc[0] for desc in cursor.description]
linhas = cursor.fetchall()

with open("vendas_distribuidor.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(colunas)
    writer.writerows(linhas)

conn.close()
print(f"✅ Exportado! {len(linhas)} registros salvos em vendas_distribuidor.csv")