#Aula(18-3)

#Crie um Sistema de cadastro de visitantes para agendar consultas médicas. O sistema deve permitir a criação de uma tabela para armazenar os dados dos visistantes, bem como fornecer funcionalidades para consulta. 
#Atualização e exclusão desses dados. Abaixo estão os requisistos detalhados.
#Você deve criar a modelagem de uma tabela chamada visitantes para armazenar as informações dos visitantes incluindo os campos id, nome, telefone, email, idade, sexo, data_agendamente e especialidade

import sqlite3

def criar_tabela_visitantes():
    conn = sqlite3.connect('cadastro_visitantes.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS visitantes (
                      id INTEGER PRIMARY KEY,
                      nome TEXT,
                      telefone TEXT,
                      email TEXT,
                      idade INTEGER,
                      sexo TEXT,
                      data_agendamento TEXT,
                      especialidade TEXT)''')
    conn.commit()
    conn.close()

def adicionar_visitante(nome, telefone, email, idade, sexo, data_agendamento, especialidade):
    conn = sqlite3.connect('cadastro_visitantes.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO visitantes (nome, telefone, email, idade, sexo, data_agendamento, especialidade)
                      VALUES (?, ?, ?, ?, ?, ?, ?)''', (nome, telefone, email, idade, sexo, data_agendamento, especialidade))
    conn.commit()
    conn.close()

def listar_visitantes():
    conn = sqlite3.connect('cadastro_visitantes.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM visitantes")
    visitantes = cursor.fetchall()
    conn.close()

    if visitantes:
        print("\nLista de visitantes:")
        for visitante in visitantes:
            print("ID:", visitante[0])
            print("Nome:", visitante[1])
            print("Telefone:", visitante[2])
            print("Email:", visitante[3])
            print("Idade:", visitante[4])
            print("Sexo:", visitante[5])
            print("Data de Agendamento:", visitante[6])
            print("Especialidade:", visitante[7])
            print("-----------------------------")

    else:
        print("Não há visitantes cadastrados.")

def atualizar_visitante(id_visitante, novo_telefone, novo_email, nova_data_agendamento):
    conn = sqlite3.connect('cadastro_visitantes.db')
    cursor = conn.cursor()
    cursor.execute('''UPDATE visitantes
                      SET  telefone = ?, email = ?, data_agendamento = ?
                      WHERE id = ?''', ( novo_telefone, novo_email, nova_data_agendamento, id_visitante))
    conn.commit()
    conn.close()

def excluir_visitante(id_visitante):
    conn = sqlite3.connect('cadastro_visitantes.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM visitantes WHERE id = ?", (id_visitante,))
    conn.commit()
    conn.close()

def main():
    criar_tabela_visitantes()

    while True:
        print("\n1. Adicionar visitante")
        print("2. Listar visitantes")
        print("3. Atualizar dados de visitante")
        print("4. Excluir visitante")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            idade = int(input("Idade: "))
            sexo = input("Sexo: ")
            data_agendamento = input("Data de agendamento (AAAA-MM-DD): ")
            especialidade = input("Especialidade: ")
            adicionar_visitante(nome, telefone, email, idade, sexo, data_agendamento, especialidade)
            print("Visitante adicionado com sucesso!")

        elif opcao == "2":
            listar_visitantes()

        elif opcao == "3":
            id_visitante = int(input("Digite o ID do visitante que deseja atualizar: "))
            novo_telefone = input("Novo telefone: ")
            novo_email = input("Novo email: ")
            nova_data_agendamento = input("Nova data de agendamento (AAAA-MM-DD): ")
            atualizar_visitante(id_visitante,  novo_telefone, novo_email, nova_data_agendamento)
            print("Dados do visitante atualizados com sucesso!")

        elif opcao == "4":
            id_visitante = int(input("Digite o ID do visitante que deseja excluir: "))
            excluir_visitante(id_visitante)
            print("Visitante excluído com sucesso!")

        elif opcao == "5":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
