from models.models import Users

class UserRespository:
    def __init__(self, db):
        self.conn = db.get_conexao()
        self.cursor = self.conn.cursor(dictionary = True)

    def criar_usuario(self, user: Users):
        query = """
        INSERT INTO users (nome, email, senha)
        VALUES (%s, %s, %s)
        """

        valores = (user.nome, user.email, user.senha)
        self.cursor.execute(query, valores)
        self.conn.commit()

    def buscar_email(self, email):
        query = """
        SELECT * FROM users WHERE email = %s
        """

        self.cursor.execute(query, (email,))
        return self.cursor.fetchone()

    def login(self, email, senha):
        usuario = self.buscar_email(email)

        if not usuario:
            return False

        return Users.verificar_senha(senha, usuario["senha"])