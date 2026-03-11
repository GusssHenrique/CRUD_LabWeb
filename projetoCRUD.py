import sqlite3
import os

caminho = os.path.join(os.getcwd(), "bancoCRUD.db")
print("Banco sendo usado:", caminho)

conn = sqlite3.connect(caminho)
cursor = conn.cursor()

def criar_tabela():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tarefas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT,
        descricao TEXT,
        status TEXT
    )
    """)
    conn.commit()

criar_tabela()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tabelas no banco:", cursor.fetchall())

def inserir():
    titulo = input("Titulo: ")
    descricao = input("Descrição: ")
    status = input("Status: ")

    cursor.execute(
        "INSERT INTO tarefas (titulo, descricao, status) VALUES (?, ?, ?)",
        (titulo, descricao, status)
    )

    conn.commit()
    print("Tarefa inserida!")


def listar():
    cursor.execute("SELECT * FROM tarefas")
    tarefas = cursor.fetchall()

    for t in tarefas:
        print(t)


def atualizar():
    id = input("ID da tarefa para atualizar: ")

    titulo = input("Novo titulo: ")
    descricao = input("Nova descrição: ")
    status = input("Novo status: ")

    cursor.execute(
        "UPDATE tarefas SET titulo = ?, descricao = ?, status = ? WHERE id = ?",
        (titulo, descricao, status, id)
    )

    conn.commit()
    print("Tarefa atualizada com sucesso!")


def deletar():
    id = input("ID da tarefa: ")

    cursor.execute("DELETE FROM tarefas WHERE id = ?", (id,))
    conn.commit()

    print("Tarefa removida")


while True:
    print("\n1 Inserir")
    print("2 Listar")
    print("3 Atualizar")
    print("4 Deletar")
    print("5 Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        inserir()

    elif opcao == "2":
        listar()

    elif opcao == "3":
        atualizar()

    elif opcao == "4":
        deletar()

    elif opcao == "5":
        break


conn.close()