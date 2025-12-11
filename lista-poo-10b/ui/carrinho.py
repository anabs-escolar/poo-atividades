import streamlit as st
import pandas as pd
from views import View
import time


class CarrinhoUI:
    def main():
        st.header("Loja")
        tab1, tab2, tab3 = st.tabs(
            [
                "Visualizar Produtos",  # listar produtos e inserir no carrinho
                "Visualizar Carrinho",  # visualizar carrinho e comprar carrinho
                "Minhas Compras",
            ]
        )

        with tab1:
            CarrinhoUI.produtos()
        with tab2:
            CarrinhoUI.carrinho()
        with tab3:
            CarrinhoUI.compras()

    def produtos():
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
                "descricao": "Descrição",
                "preco": "Preço",
                "estoque": "Estoque",
                "categoria": "Categoria",
            }
        )
        st.dataframe(
            df,
            hide_index=True,
            column_order=["Descrição", "Preço", "Estoque", "Categoria"],
        )

        st.subheader("Adicionar Produto ao Carrinho")
        produtos = View.produto_listar()
        if len(produtos) == 0:
            st.write("Nenhum produto cadastrado")

        op = st.selectbox(
            "Seleciona um Produto",
            produtos,
            format_func=lambda p: f"{p.get_descricao()}",
        )
        qtd = st.number_input("Quantidade", step=1)
        if st.button("Adicionar ao Carrinho"):
            p_id = op.get_id()
            user = st.session_state["user"].get_id()
            try:
                View.produto_inserir_carrinho(p_id, user, qtd)
                st.success("Produto adicionado com sucesso!")
                time.sleep(2)
                st.rerun()
            except ValueError as e:
                st.warning(e)

    def carrinho():
        st.subheader("Meu Carrinho")
        user_id = st.session_state["user"].get_id()
        items, total = View.carrinho_listar(user_id)

        if not items:
            st.info("Seu carrinho está vazio.")
            return

        df = pd.DataFrame(items)
        df = df.rename(
            columns={
                "descricao": "Descrição",
                "preco_unitario": "Preço Unitário (R$)",
                "qtd": "Quantidade",
                "total_item": "Total Item (R$)",
            }
        )

        st.dataframe(
            df,
            hide_index=True,
            column_order=[
                "Descrição",
                "Preço Unitário (R$)",
                "Quantidade",
                "Total Item (R$)",
            ],
        )

        st.markdown(f"### Total da Compra: R$ {total:.2f}")
        if st.button("Confirmar Compra"):
            try:
                View.carrinho_comprar(user_id)
                st.success("Compra realizada com sucesso!")
                time.sleep(2)
                st.rerun()
            except ValueError as e:
                st.error(e)

    def compras():
        st.subheader("Minhas Compras")

        user_id = st.session_state["user"].get_id()
        compras = View.compras_listar(user_id)

        if not compras:
            st.info("Você ainda não fez nenhuma compra.")
            return

        for venda, itens in compras:
            data = venda.get_data().strftime("%d/%m/%Y %H:%M")
            total = venda.get_total()

            # Título de cada compra
            st.markdown(f"#### Compra em {data} - Total: R$ {total:.2f}")

            # Montar tabela de itens
            df = pd.DataFrame(itens)
            df = df.rename(
                columns={
                    "descricao": "Descrição",
                    "preco_uni": "Preço Unitário (R$)",
                    "qtd": "Quantidade",
                    "preco_qtd": "Total Item (R$)",
                }
            )

            st.dataframe(
                df,
                hide_index=True,
                column_order=[
                    "Descrição",
                    "Preço Unitário (R$)",
                    "Quantidade",
                    "Total Item (R$)",
                ],
            )
