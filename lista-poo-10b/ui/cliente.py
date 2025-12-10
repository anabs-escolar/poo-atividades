import streamlit as st
import pandas as pd
from views import View
import time


class ClienteUI:
    def main():
        st.header("Cadastro de cliente")
        tab1, tab2, tab3, tab4 = st.tabs(
            ["Listar", "Cadastrar", "Atualizar", "Excluir"]
        )

        with tab1:
            ClienteUI.listar()
        with tab2:
            ClienteUI.cadastrar()
        with tab3:
            ClienteUI.atualizar()
        with tab4:
            ClienteUI.excluir()

    def listar():
        st.subheader("Clientes")
        clientes = View.cliente_listar()

        if len(clientes) == 0:
            st.write("Nenhum cliente cadastrado")
            return

        cli_list = []
        for obj in clientes:
            cli_list.append(obj.to_json())
        df = pd.DataFrame(cli_list)
        df = df.rename(
            columns={
                "id": "ID",
                "is_admin": "Admin?",
                "nome": "Nome",
                "email": "E-mail",
                "fone": "Telefone",
            }
        )
        st.dataframe(
            df,
            hide_index=True,
            column_order=["ID", "Admin?", "Nome", "E-mail", "Telefone"],
        )

    def cadastrar():
        st.subheader("Cadastrar")
        nome = st.text_input("Nome")
        email = st.text_input("E-mail")
        senha = st.text_input("Senha", type="password")
        telefone = st.text_input("Telefone")
        is_admin = st.checkbox("Administrador?")

        if st.button("Cadastrar"):
            try:
                View.cliente_inserir(nome, email, senha, telefone, is_admin)
                st.success("Cliente cadastrado com sucesso")
                time.sleep(2)
                st.rerun()
            except ValueError as e:
                st.warning(e)

    def atualizar():
        clientes = View.cliente_listar()
        if len(clientes) == 0:
            st.write("Nenhum cliente cadastrado")
        op = st.selectbox(
            "Cliente para Atualizar (ID, Nome)",
            clientes,
            format_func=lambda c: f"{c.get_id()}, {c.get_nome()}",
        )
        nome = st.text_input("Nome", op.get_nome())
        email = st.text_input("Email", op.get_email())
        telefone = st.text_input("Telefone", op.get_fone())

        if st.button("Atualizar"):
            c_id = op.get_id()
            View.cliente_atualizar(c_id, nome, email, telefone)
            st.success("Cliente atualizado com sucesso")
            time.sleep(2)
            st.rerun()

    def excluir():
        clientes = View.cliente_listar()
        op = st.selectbox(
            "Cliente para Excluir (ID, Nome)",
            clientes,
            format_func=lambda c: f"{c.get_id()}, {c.get_nome()}",
        )

        if st.button("Excluir"):
            c_id = op.get_id()
            View.cliente_excluir(c_id)
            st.success("Cliente excluído com sucesso")
            time.sleep(2)
            st.rerun()

    def adiciona_admin():
        pass

    def remover_admin():
        pass
