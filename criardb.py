import sqlite3

# Conecta (ou cria) o banco de dados
conn = sqlite3.connect('studio.db')
cursor = conn.cursor()

# Cria a tabela 'planos'
cursor.execute('''
CREATE TABLE IF NOT EXISTS planos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT NOT NULL,
    valor REAL NOT NULL
)
''')

# Salva as alterações e fecha a conexão
conn.commit()
conn.close()

print("Banco de dados e tabela 'planos' criados com sucesso.")
