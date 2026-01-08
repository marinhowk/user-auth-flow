from database.database import BancoDeDados
from database.repositories import UserRespository
from models.models import Users
from services.email_service import enviar_email

db = BancoDeDados()
repo = UserRespository(db)

def menu_principal():
    print("[ 1 ] Realizar Login")
    print("[ 2 ] Realizar Cadastro")
    print("[ 3 ] Redefinir senha")

def login():
    email = input("Email: ")
    senha = input("Senha: ")

    if repo.login(email, senha):
        pagina_inicial()
    else:
        print("Email ou senha inválidos.")
        login()

def cadastro():
    nome = input("Nome: ")
    email = input("E-mail: ")
    senha = input("Senha: ")
    confirmar_senha = input("Confirme a sua senha: ")

    usuario = Users(nome, email, senha)
    tentativas = 3

    codigo_gerado = enviar_email(email)

    if nome and email and senha and confirmar_senha:
        if confirmar_senha == senha:

            while tentativas > 0:
                codigo_digitado = input("Insira o código de confirmação enviado no email: ")

                if codigo_digitado == str(codigo_gerado):
                    repo.criar_usuario(usuario)
                    login()
                    return
                else:
                    tentativas -= 1
                    print(f"Código inválido. Tentativas restantes: {tentativas}")

            print("Número máximo de tentativas atingido. Código expirado.")

        else:
            print("As senhas são divergentes, insira das informações novamente.")
            cadastro()

    else:
        print("Preencha todos os campos.")
        cadastro()

def redefinir_senha():
    pass

def pagina_inicial():
    print("Bem Vindo.")

def escolha_menu():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        match opcao_escolhida:
            case 1:
                login()
            case 2:
                cadastro()
            case 3:
                redefinir_senha()
            case _:
                print("Opção inválida")
    except:
        escolha_menu()

def main():
    menu_principal()
    escolha_menu()

if __name__ == "__main__":
    main()