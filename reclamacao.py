import streamlit as st


reclamacao = "sem reclamações ainda"

st.title("Um novo lugar para vc depositar todas as suas reclamações. Aproveite.")

reclamacao = str(st.chat_input("digite aqui a sua reclamação" ))

with st.chat_message("user"):
    st.write(reclamacao)