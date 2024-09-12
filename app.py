import streamlit as st
from datetime import datetime,time


def main():

    st.title("Sistema de CRM")
    email = st.text_input("Insira o e-mail do cliente")
    data = st.date_input("Insira a data da venda",datetime.now())
    hora = st.time_input("Insira a hora da venda",value=time(9,0))
    valor = st.number_input("Insira o valor da venda",min_value=0.0, format="%.2f",step=1.0)
    quantidade = st.number_input("Insira a quantidade vendida",min_value=1,step=1)
    st.selectbox("Selecione o serviço ofertado",["Curso Basico","Curso de Qualificação Profissional","Serviço de Academia","Clube de Esporte e Lazer","Atendimento de Saúde","Atendimento Odontologico"])
    
    st.button("Cadastrar Venda")

if __name__ == "__main__":
    main()

