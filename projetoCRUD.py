import sqlite3

conn = sqlite3.connect("C:/Users/Aluno/Desktop/bancoCRUD.db")
cursor = conn.cursor()

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
        "UPDATE tarefas SET titulo = ?, descricao = ?, status = ? WHERE id = ?"
    )

    conn.commit()

    print("Tarefa atualizada com sucesso!")

def deletar():
    id = input("ID da tarefa: ")

    cursor.execute("DELETE FROM tarefas WHERE id = ?", (id))
    conn.commit()

    print("Tarefa removida")

while True:
    print ("\n1 Inserir")
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

conn.commit