import sqlite3

class Student:
    def __init__(self, student_id, nome, idade, mae, pai):
        self.student_id = student_id
        self.nome = nome
        self.idade = idade
        self.mae = mae
        self.pai = pai

class StudentDatabase:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

        # Criação da tabela de estudantes
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                student_id TEXT PRIMARY KEY,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL,
                mae TEXT NOT NULL,
                pai TEXT NOT NULL
            )
        ''')
        self.connection.commit()

    def create_student(self, student_id, nome, idade, mae, pai):
        # Adiciona um novo estudante ao banco de dados
        self.cursor.execute('''
            INSERT INTO students (student_id, nome, idade, mae, pai)
            VALUES (?, ?, ?, ?, ?)
        ''', (student_id, nome, idade, mae, pai))
        self.connection.commit()

    def read_student(self, student_id):
        # Busca um estudante no banco de dados pelo ID
        self.cursor.execute('SELECT * FROM students WHERE student_id = ?', (student_id,))
        result = self.cursor.fetchone()
        if result:
            student_id, nome, idade, mae, pai = result
            return Student(student_id, nome, idade, mae, pai)
        else:
            return None

    def update_student(self, student_id, nome, idade, mae, pai):
        # Atualiza os detalhes de um estudante existente
        self.cursor.execute('''
            UPDATE students
            SET nome = ?, idade = ?, mae = ?, pai = ?
            WHERE student_id = ?
        ''', (nome, idade, mae, pai, student_id))
        self.connection.commit()

    def delete_student(self, student_id):
        # Exclui um estudante do banco de dados pelo ID
        self.cursor.execute('DELETE FROM students WHERE student_id = ?', (student_id,))
        self.connection.commit()

    def __del__(self):
        # Fecha a conexão com o banco de dados quando o objeto é destruído
        self.connection.close()