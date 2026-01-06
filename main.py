import streamlit as st
from database.database import BancoDeDados
from database.repositories import UserRespository
from models.models import Users
from services.email_service import enviar_email, codigo_de_confirmacao

db = BancoDeDados()
repo = UserRespository(db)

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="User Auth Flow", layout="wide")

# --- CONTROLE DE NAVEGAÇÃO
if "tela" not in st.session_state:
    st.session_state.tela = "login"

# --- CONTROLE DE SESSÃO DAS PÁGINAS ---
def tela_de_login():
    st.session_state.tela = "login"

def tela_de_cadastro():
    st.session_state.tela = "cadastro"

def tela_codigo_de_confirmacao():
    st.session_state.tela = "codigo"

def pagina_principal():
    st.session_state.tela = "pagina_principal"

# --- TELA DE LOGIN ---
if st.session_state.tela == "login":
    col1, col2, col3 = st.columns([1, 1, 1])

    with col2:
        st.title("Olá!")
        st.subheader("Seja bem vindo de volta!")

        msg_login = st.empty()

        email = st.text_input("Email")
        senha = st.text_input("Password", type="password")

        col_cadastro, col_entrar = st.columns([1, 1])

        with col_cadastro:
            if st.button("Criar Conta", use_container_width= True):
                st.session_state.tela = "cadastro"
                st.rerun()

        with col_entrar:
            if st.button("Entrar", use_container_width= True):
                if repo.login(email, senha):
                    st.session_state.tela = "pagina_principal"
                    st.rerun()
                else:
                    msg_login.error("Email ou senha inválidos")

        st.divider()

        st.button("Esqueceu a senha? Clique aqui", use_container_width= True)

# --- TELA DE CADASTRO ---
elif st.session_state.tela == "cadastro":
    col1, col2, col3 = st.columns([1, 1, 1])

    msg = st.empty()

    with col2:
        st.title("Crie uma nova conta")
        nome_cadastro = st.text_input("Nome")
        email_cadastro = (st.text_input("E-mail"))
        senha_cadastro = st.text_input("Senha", type="password")
        confirmacao_de_senha = st.text_input("Confirme a senha", type= "password")

        if st.button("Registrar", use_container_width= True):
            if senha_cadastro == confirmacao_de_senha:
                enviar_email(email_cadastro)
                st.session_state.tela = "codigo"
                st.rerun()
            else:
                msg.error("A senha de confirmação diverge da senha informada")

# --- TELA DE CONFIRMAÇÃO DE EMAIL ---
elif st.session_state.tela == "codigo":
    col1, col2, col3 = st.columns([1, 1, 1])

    with col2:
        msg = st.empty()
        st.subheader(f"Insira o código de verificação enviado no email informado")
        codigo_de_verificação = st.number_input("Codigo de Verificação", max_value= 9999)

        if st.button("Confirmar", use_container_width= True):
            if codigo_de_verificação == codigo_de_confirmacao():
                st.session_state.tela = "login"
                st.rerun()
            else:
                msg.error("Código inválido")

# --- TELA PAGINA PRINCIPAL ---
elif st.session_state.tela == "pagina_principal":
    st.text("BemVindo.")
