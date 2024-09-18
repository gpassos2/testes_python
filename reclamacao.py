import streamlit as st
import pandas as pd


st.title("Um novo lugar para vc depositar todas as suas reclamações. Aproveite.")

reclamacao = str(st.chat_input("digite aqui a sua reclamação" ))

with open('respostas.csv', 'a') as respostas:
    respostas.write(f'\n{reclamacao}')


with st.chat_message("user"):
    df = pd.read_csv("respostas.csv")
    st.dataframe(df)