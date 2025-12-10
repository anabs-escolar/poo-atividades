import time
import streamlit as st
from views import View


class VisitanteUI:
    def entrar():
        st.header("Entrar no sistema")
        email = st.text_input("Email:")
        senha = st.text_input("Senha:", type="password")
        if st.button("Entrar"):
            user = View.cliente_autenticar(email=email, senha=senha)
            if user == None:
                st.write("Email ou senha inválidos")
            else:
                if user.get_is_admin():
                    st.success(f"Bem vindo, Administrador {user.get_nome()}!")
                else:
                    st.success(f"Bem vindo, {user.get_nome()}!")
                time.sleep(2)
                st.session_state["user"] = user
                st.rerun()

    def criar_conta() -> None:
        st.subheader("Criar Conta")
        nome = st.text_input("Nome")
        fone = st.text_input("Telefone")
        email = st.text_input("E-mail")
        senha = st.text_input("Senha", type="password")

        if st.button("Cadastrar"):
            try:
                View.cliente_inserir(nome, email, senha, fone)
                st.success("Cliente cadastrado com sucesso")
                time.sleep(2)
                st.rerun()
            except ValueError as e:
                st.warning(e)
