import streamlit as st
import pandas as pd
from views import View
import time


class ClienteUI:
    def main():
        st.header("Cadastro de cliente")
        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
            [
                "Listar",
                "Cadastrar",
                "Atualizar",
                "Adicionar Admin",
                "Remover Admin",
                "Excluir",
            ]
        )

        with tab1:
            ClienteUI.listar()
        with tab2:
            ClienteUI.cadastrar()
        with tab3:
            ClienteUI.atualizar()
        with tab4:
            ClienteUI.adiciona_admin()
        with tab5:
            ClienteUI.remover_admin()
        with tab6:
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
            try:
                c_id = op.get_id()
                View.cliente_atualizar(c_id, nome, email, telefone)
                st.success("Cliente atualizado com sucesso")
                time.sleep(2)
                st.rerun()
            except ValueError as e:
                st.warning(e)

    def excluir():
        clientes = View.cliente_listar()
        op = st.selectbox(
            "Cliente para Excluir (ID, Nome)",
            clientes,
            format_func=lambda c: f"{c.get_id()}, {c.get_nome()}",
        )

        if st.button("Excluir"):
            try:
                c_id = op.get_id()
                View.cliente_excluir(c_id)
                st.success("Cliente excluído com sucesso")
                time.sleep(2)
                st.rerun()
            except ValueError as e:
                st.warning(e)

    def adiciona_admin():
        clientes = View.cliente_listar()
        if len(clientes) == 0:
            st.write("Nenhum cliente cadastrado")

        op = st.selectbox(
            "Cliente para Admin (ID, Nome)",
            clientes,
            format_func=lambda c: f"{c.get_id()}, {c.get_nome()}",
        )
        if st.button("Adicionar Permissão"):
            try:
                c_id = op.get_id()
                View.adicionar_admin(c_id)
                st.success(
                    f"Permissão de Administrador adicionada ao Cliente {op.get_nome()}"
                )
                time.sleep(2)
                st.rerun()
            except ValueError as e:
                st.warning(e)

    def remover_admin():
        clientes = View.cliente_listar()
        if len(clientes) == 0:
            st.write("Nenhum cliente cadastrado")

        op = st.selectbox(
            "Cliente para Usuário Comum (ID, Nome)",
            clientes,
            format_func=lambda c: f"{c.get_id()}, {c.get_nome()}",
        )
        if st.button("Remover Permissão"):
            try:
                c_id = op.get_id()
                View.remover_admin(c_id)
                st.success(
                    f"Permissão de Administrador removida de Cliente {op.get_nome()}"
                )
                time.sleep(2)
                st.rerun()
            except ValueError as e:
                st.warning(e)
