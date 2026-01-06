import hashlib

class Users:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = self._hash_senha(senha)
        # inserir se o status do usuário é true ou false

    def _hash_senha(self, senha):
        return hashlib.sha256(senha.encode()).hexdigest()

    @staticmethod
    def verificar_senha(senha_inserida, senha_banco):
        senha_hash = hashlib.sha256(senha_inserida.encode()).hexdigest()
        return senha_hash == senha_banco