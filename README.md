# 📊 SQL Distribuidor

> *"São pequenos passos que nos fazem trilhar grandes caminhos."*

## 🇧🇷 Português

### Sobre o projeto

Projeto de análise de dados desenvolvido com Python e SQL, simulando o ambiente de uma distribuidora de cosméticos, perfumaria e higiene pessoal. Os dados são armazenados em um banco de dados SQLite, analisados via queries SQL e visualizados em um dashboard interativo no Power BI.

Desenvolvido como parte do meu aprendizado prático em análise de dados, com foco em SQL, manipulação de dados e visualização com Power BI.

### Funcionalidades

- 🗄️ Banco de dados relacional com 4 tabelas (produtos, clientes, vendedores e vendas)
- 📦 500 registros de vendas fictícios gerados automaticamente
- 🔍 Queries SQL para análise de faturamento, produtos, clientes e vendedores
- 📤 Exportação dos dados para CSV
- 📊 Dashboard interativo no Power BI com visuais, filtros e layout profissional

### Análises realizadas

- 💰 Faturamento total
- 📦 Faturamento por categoria (Cosméticos, Perfumaria, Higiene)
- 🏆 Produtos mais vendidos em quantidade
- 👤 Faturamento por vendedor e participação percentual
- 🏪 Top clientes por faturamento com cidade e estado
- 📅 Evolução do faturamento mês a mês
- 🗺️ Faturamento por região do Brasil

### Dashboard Power BI

O dashboard conta com layout profissional, tema escuro, bordas e filtros interativos:

**Visuais:**
- **Cartão** — Faturamento Total
- **Cartão** — Total de Itens Vendidos
- **Gráfico de barras** — Faturamento por Categoria
- **Gráfico de linhas** — Evolução Mensal
- **Gráfico de pizza** — Participação por Vendedor
- **Gráfico de barras** — Produtos Mais Vendidos
- **Tabela** — Top Clientes com cidade e estado

**Filtros interativos:**
- 📅 Por período (data)
- 📦 Por categoria
- 👤 Por vendedor

### Tecnologias utilizadas

- Python 3.12
- SQLite — banco de dados relacional
- Power BI Desktop — visualização e dashboard
- `csv` — exportação dos dados

### Como usar

**1. Clone o repositório**
```bash
git clone https://github.com/MatheusSantos9029/sql-distribuidor.git
cd sql-distribuidor
```

**2. Crie o banco de dados**
```bash
python criar_banco.py
```

**3. Execute as análises SQL**
```bash
python analises.py
```

**4. Exporte os dados para CSV**
```bash
python exportar_csv.py
```

**5. Abra o dashboard**

Abra o arquivo `dashboard_distribuidor.pbix` no Power BI Desktop.

### Estrutura do projeto

```
sql-distribuidor/
│
├── criar_banco.py              # Cria o banco e gera os dados fictícios
├── analises.py                 # Queries SQL de análise
├── exportar_csv.py             # Exporta os dados para CSV
├── vendas_distribuidor.csv     # Dados exportados para o Power BI
├── dashboard_distribuidor.pbix # Dashboard no Power BI
└── .gitignore                  # Arquivos ignorados pelo Git
```

---

## 🇺🇸 English

### About

A data analysis project built with Python and SQL, simulating the environment of a cosmetics, perfumery, and personal care distributor. Data is stored in a SQLite database, analyzed via SQL queries, and visualized in an interactive Power BI dashboard.

Built as part of my hands-on learning journey in data analysis, focusing on SQL, data manipulation, and Power BI visualization.

### Features

- 🗄️ Relational database with 4 tables (products, customers, salespeople, and sales)
- 📦 500 automatically generated fictional sales records
- 🔍 SQL queries for revenue, product, customer, and salesperson analysis
- 📤 Data export to CSV
- 📊 Interactive Power BI dashboard with visuals, filters, and professional layout

### Analyses performed

- 💰 Total revenue
- 📦 Revenue by category (Cosmetics, Perfumery, Hygiene)
- 🏆 Best-selling products by quantity
- 👤 Revenue by salesperson and percentage share
- 🏪 Top customers by revenue with city and state
- 📅 Monthly revenue evolution
- 🗺️ Revenue by Brazilian region

### Power BI Dashboard

The dashboard features a professional layout, dark theme, borders, and interactive filters:

**Visuals:**
- **Card** — Total Revenue
- **Card** — Total Items Sold
- **Bar chart** — Revenue by Category
- **Line chart** — Monthly Evolution
- **Pie chart** — Salesperson Share
- **Bar chart** — Best-Selling Products
- **Table** — Top Customers with city and state

**Interactive filters:**
- 📅 By period (date)
- 📦 By category
- 👤 By salesperson

### Technologies

- Python 3.12
- SQLite — relational database
- Power BI Desktop — visualization and dashboard
- `csv` — data export

### How to use

**1. Clone the repository**
```bash
git clone https://github.com/MatheusSantos9029/sql-distribuidor.git
cd sql-distribuidor
```

**2. Create the database**
```bash
python criar_banco.py
```

**3. Run SQL analyses**
```bash
python analises.py
```

**4. Export data to CSV**
```bash
python exportar_csv.py
```

**5. Open the dashboard**

Open `dashboard_distribuidor.pbix` in Power BI Desktop.

### Project structure

```
sql-distribuidor/
│
├── criar_banco.py              # Creates the database and generates fictional data
├── analises.py                 # SQL analysis queries
├── exportar_csv.py             # Exports data to CSV
├── vendas_distribuidor.csv     # Exported data for Power BI
├── dashboard_distribuidor.pbix # Power BI dashboard
└── .gitignore                  # Git ignored files
```

---

*Developed by [Matheus Santos](https://github.com/MatheusSantos9029)*
