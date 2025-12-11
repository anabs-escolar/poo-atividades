import streamlit as st
import pandas as pd
from views import View
import time


class CategoriaUI:
    def main():
        st.header("Manter categorias")
        tab1, tab2, tab3, tab4 = st.tabs(
            ["Listar", "Cadastrar", "Atualizar", "Excluir"]
        )

        with tab1:
            CategoriaUI.listar()
        with tab2:
            CategoriaUI.cadastrar()
        with tab3:
            CategoriaUI.atualizar()
        with tab4:
            CategoriaUI.excluir()

    def listar():
        st.subheader("Categorias")
        categorias = View.categoria_listar()

        if not categorias:
            st.write("Nenhuma categoria cadastrada")
            return

        cat_list = []
        for obj in categorias:
            cat_list.append(obj.to_json())
        df = pd.DataFrame(cat_list)
        df = df.rename(
            columns={
                "id": "ID",
                "descricao": "Descrição",
            }
        )

        st.dataframe(
            df,
            hide_index=True,
            column_order=["ID", "Descrição"],
        )

    def cadastrar():
        st.subheader("Cadastrar categoria")
        nome = st.text_input("Nome")

        if st.button("Cadastrar"):
            try:
                View.categoria_inserir(nome)
                st.success("Categoria cadastrada com sucesso")
                time.sleep(2)
                st.rerun()
            except ValueError as e:
                st.warning(e)

    def atualizar():
        categorias = View.categoria_listar()
        if not categorias:
            st.write("Nenhuma categoria cadastrada")
            return

        op = st.selectbox(
            "Categoria para Atualizar (ID, Nome)",
            categorias,
            format_func=lambda c: f"{c.get_id()}, {c.get_descricao()}",
        )
        nome = st.text_input("Nome", op.get_descricao())
        if st.button("Atualizar"):
            try:
                View.categoria_atualizar(op.get_id(), nome)
                st.success("Categoria atualizada com sucesso")
                time.sleep(2)
                st.rerun()
            except ValueError as e:
                st.warning(e)

    def excluir():
        categorias = View.categoria_listar()

        if not categorias:
            st.write("Nenhuma categoria cadastrada")
            return

        op = st.selectbox(
            "Categoria para Excluir (ID, Nome)",
            categorias,
            format_func=lambda c: f"{c.get_id()}, {c.get_descricao()}",
        )

        if st.button("Excluir"):
            cat_id = op.get_id()
            try:
                View.categoria_excluir(cat_id)
                st.success("Categoria excluída com sucesso")
                time.sleep(2)
                st.rerun()

            except ValueError as e:
                st.warning(e)
