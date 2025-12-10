import streamlit as st
import pandas as pd
from views import View
import time


class ProdutoUI:
    def main():
        st.header("Manter produto")
        tab1, tab2, tab3, tab4 = st.tabs(
            ["Listar", "Cadastrar", "Atualizar", "Excluir"]
        )

        with tab1:
            ProdutoUI.listar()
        with tab2:
            ProdutoUI.cadastrar()
        with tab3:
            ProdutoUI.atualizar()
        with tab4:
            ProdutoUI.excluir()

    def listar():
        st.subheader("Produtos")
        produtos = View.produto_listar()
        categorias = View.categoria_listar()

        if not produtos:
            st.write("Nenhum produto cadastrado")
            return

        prod_list = [p.to_json() for p in produtos]
        cat_list = [c.to_json() for c in categorias]
        cat_map = {c["id"]: c["descricao"] for c in cat_list}
        for p in prod_list:
            cat_id = (
                p.get("categoria") or p.get("id_categoria") or p.get("categoria_id")
            )
            p["categoria"] = cat_map.get(cat_id, "Sem categoria")

        df = pd.DataFrame(prod_list)
        df = df.rename(
            columns={
                "id": "ID",
                "descricao": "Descrição",
                "preco": "Preço",
                "estoque": "Estoque",
                "categoria": "Categoria",
            }
        )
        st.dataframe(
            df,
            hide_index=True,
            column_order=["ID", "Descrição", "Preço", "Estoque", "Categoria"],
        )

    def cadastrar():
        st.subheader("Cadastrar produto")
        categorias = View.categoria_listar()
        descricao = st.text_input("Nome")
        preco = st.number_input("Preco")
        estoque = st.number_input("Estoque", value=0)
        categoria = st.selectbox(
            "Categoria", categorias, format_func=lambda c: f"{c.get_descricao()}"
        )

        if st.button("Cadastrar"):
            for c in View.produto_listar():
                if c.get_descricao() == descricao:
                    st.warning("Produto já existe")
                    time.sleep(2)
                    st.rerun()

            try:
                View.produto_inserir(descricao, preco, estoque, categoria.get_id())
                st.success("Produto cadastrado com sucesso")
                time.sleep(2)
                st.rerun()
            except ValueError as e:
                st.warning(e)

    def atualizar():
        produtos = View.produto_listar()
        if len(produtos) == 0:
            st.write("Nenhum produto cadastrado")

        op = st.selectbox(
            "Produto para Atualizar (ID, Descrição)",
            produtos,
            format_func=lambda p: f"{p.get_id()}, {p.get_descricao()}",
        )
        categorias = View.categoria_listar()
        descricao = st.text_input("Descrição", op.get_descricao())
        preco = st.number_input("Preço", op.get_preco())
        estoque = st.number_input("Estoque", op.get_estoque())
        categoria = st.selectbox(
            "Categoria",
            options=categorias,
            index=None,
            format_func=lambda c: f"{c.get_descricao()}",
        )

        if st.button("Atualizar"):
            p_id = op.get_id()
            c_id = categoria.get_id()
            if categoria == None:
                c_id = op.get_categoria()

            try:
                View.produto_atualizar(p_id, descricao, preco, estoque, c_id)
                st.success("Produto atualizado com sucesso")
                time.sleep(2)
                st.rerun()
            except ValueError as e:
                st.warning(e)

    def excluir():
        produtos = View.produto_listar()
        vendas = View.vendas_listar()

        op = st.selectbox(
            "Produto para Excluir (ID, Descrição)",
            produtos,
            format_func=lambda p: f"{p.get_id()}, {p.get_descricao()}",
        )
        if st.button("Excluir"):
            p_id = op.get_id()
            for venda, itens in vendas:
                for item in itens:
                    if item["id_produto"] == p_id:
                        st.error(
                            "Esse produto está associado a uma venda e não pode ser excluído."
                        )
                        time.sleep(2)
                        st.rerun()

            View.produto_excluir(p_id)
            st.success("Produto excluído com sucesso")
            time.sleep(2)
            st.rerun()

    def reajustar():
        pass
