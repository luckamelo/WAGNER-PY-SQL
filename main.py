from student_database import Student,StudentDatabase
import sqlite3

def main():
    # Conectar ao banco de dados SQLite
    connection = sqlite3.connect("student_database.db")

    # Criação de uma instância de StudentDatabase associada ao banco de dados
    student_db = StudentDatabase(connection)

    while True:
        print("-------CRUD WAGUINHO (LISTA DE ESTUDANTE)--------")
        print("\nEscolha uma opção:")
        print("1. Adicionar estudante")
        print("2. Listar estudantes")
        print("3. Atualizar estudante")
        print("4. Excluir estudante")
        print("5. Sair")

        user_choice = input("Digite o número da opção: ")

        if user_choice == '1':
            # Adiciona um novo estudante ao banco de dados
            student_id = input("Digite o ID do estudante: ")
            nome = input("Digite o nome do estudante: ")
            idade = input("Digite a idade do estudante: ")
            mae = input("Digite o nome da mae: ")
            pai = input("Digite o nome do pai: ")
            student_db.create_student(student_id, nome, idade, mae, pai)
            print("Estudante adicionado com sucesso!")

        elif user_choice == '2':
            # Lista todos os estudantes no banco de dados
            print("\nLista de Estudantes:")
            students = student_db.cursor.execute('SELECT * FROM students').fetchall()
            for student in students:
                print(f"ID: {student[0]}, Nome: {student[1]}, Idade: {student[2]}, Mae: {student[3]}, Pai: {student[4]}")

        elif user_choice == '3':
            # Atualiza os detalhes de um estudante existente
            student_id = input("Digite o ID do estudante que deseja atualizar: ")
            name = input("Digite o novo nome do estudante: ")
            age = input("Digite a nova idade do estudante: ")
            mae = input("Digite o novo nome da mae: ") 
            pai = input("Digite o novo nome do pai: ")
            student_db.update_student(student_id, name, age, mae, pai)
            print("Estudante atualizado com sucesso!")

        elif user_choice == '4':
            # Exclui um estudante do banco de dados
            student_id = input("Digite o ID do estudante que deseja excluir: ")
            student_db.delete_student(student_id)
            print("Estudante excluído com sucesso!")

        elif user_choice == '5':
            # Sai do programa
            print("Saindo do programa.")
            break

        else:
            # Mensagem para opção inválida
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()