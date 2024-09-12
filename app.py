import streamlit as st
from datetime import datetime,time
from contrato import Vendas
from pydantic import ValidationError
from database import salvar_no_postgres

def main():

    st.title("Sistema de CRM")
    email = st.text_input("Insira o e-mail do cliente")
    data = st.date_input("Insira a data da venda",datetime.now())
    hora = st.time_input("Insira a hora da venda",value=time(9,0))
    valor = st.number_input("Insira o valor da venda",min_value=0.0, format="%.2f",step=1.0)
    quantidade = st.number_input("Insira a quantidade vendida",min_value=1,step=1)
    produto = st.selectbox("Selecione o serviço ofertado",["Curso Basico","Curso de Qualificação Profissional","Serviço de Academia","Clube de Esporte e Lazer","Atendimento de Saúde","Atendimento Odontologico"])
    

    if st.button("Cadastrar Venda"):

        try:
            data_hora =datetime.combine(data,hora)
            venda = Vendas(
                email=email,
                data=data_hora,
                valor=valor,
                quantidade=quantidade,
                produto=produto)
            

            salvar_no_postgres(venda)
            #st.write("**Os Dados da Venda Foram Cadastrados **")
            #st.write(f"Email do Cliente: {email}")
            #st.write(f"Data e Hora da Venda: {data_hora}")
            #st.write(f"Valor da Venda: R${valor}")
            #st.write(f"Quantidade Vendida: {quantidade}")
            #st.write(f"Produto: {produto}")



        except ValidationError as e:
            st.error(f"Erro de Validação: {e}")


if __name__ == "__main__":
    main()

