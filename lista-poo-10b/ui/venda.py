import streamlit as st
import pandas as pd
from views import View


class VendaUI:
    def main():
        st.header("Listar vendas")
        VendaUI.listar()

    def listar():
        st.subheader("Vendas realizadas")
        vendas = View.vendas_listar()

        if not vendas:
            st.write("Nenhuma venda registrada")
            return

        ven_list = []
        for venda, items in vendas:
            ven_list.append(
                {
                    "Cliente": venda["cliente"],
                    "Data": venda["data"].strftime("%d/%m/%Y %H:%M"),
                    "Total (R$)": f"{venda['total']:.2f}",
                }
            )

        df = pd.DataFrame(ven_list)
        st.dataframe(
            df,
            hide_index=True,
            column_order=["Cliente", "Data", "Total (R$)"],
        )

        st.subheader("Detalhes de cada venda")

        for venda, items in vendas:
            with st.expander(
                f"Cliente: {venda['cliente']} - Data: {venda['data'].strftime('%d/%m/%Y %H:%M')}"
            ):
                item_list = []
                for i in items:
                    item_list.append(
                        {
                            "Descrição": i["descricao"],
                            "Preço Unit. (R$)": f"{i['preco_uni']:.2f}",
                            "Quantidade": i["qtd"],
                            "Total Item (R$)": f"{i['preco_qtd']:.2f}",
                        }
                    )

                df_item = pd.DataFrame(item_list)

                st.dataframe(
                    df_item,
                    hide_index=True,
                    column_order=[
                        "Descrição",
                        "Preço Unit. (R$)",
                        "Quantidade",
                        "Total Item (R$)",
                    ],
                )
