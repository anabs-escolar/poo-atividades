from .visitante import VisitanteUI
from .cliente import ClienteUI
from .produto import ProdutoUI
from .categoria import CategoriaUI
from .venda import VendaUI
from views import View
import streamlit as st


class IndexUI:

    def main():
        View.abrir_todos()
        IndexUI.sidebar()

    def sidebar():
        if "user" in st.session_state:
            user = st.session_state["user"]
            st.write(f"Bem-vindo(a), {user.get_nome()}")
            if user.get_is_admin():
                IndexUI.menu_admin()
            else:
                IndexUI.menu_cliente()
        else:
            IndexUI.menu_visitante()

    def menu_visitante():
        op = st.sidebar.selectbox(
            "Menu",
            [
                "Entrar no sistema",
                "Criar conta",
            ],
        )

        if op == "Entrar no sistema":
            VisitanteUI.entrar()
        if op == "Criar conta":
            VisitanteUI.criar_conta()

    def menu_cliente():
        op = st.sidebar.selectbox(
            "Menu", ["Listar produtos", "Carrinho", "Listar minhas compras", "Sair"]
        )

        if op == "Listar produtos":
            # ManterProdutoUI.listar()
            pass
        if op == "Carrinho":
            # ClienteUI.carrinho()
            pass
        if op == "Listar minhas compras":
            # ClienteUI.listar_minhas_compras()
            pass
        if op == "Sair":
            IndexUI.logout()

    def menu_admin():
        op = st.sidebar.selectbox(
            "Menu",
            [
                "Cadastro de clientes",
                "Cadastro de categorias",
                "Cadastro de produtos",
                "Listar Vendas",
                "Sair",
            ],
        )

        if op == "Cadastro de categorias":
            CategoriaUI.main()
        if op == "Cadastro de clientes":
            ClienteUI.main()
        if op == "Cadastro de produtos":
            ProdutoUI.main()
        if op == "Listar Vendas":
            VendaUI.main()
        if op == "Sair":
            IndexUI.logout()

    def logout():
        del st.session_state["user"]
        st.rerun()
