import streamlit as st
import random


def realizar_sorteio(minimo, maximo, quantidade):
    if maximo - minimo + 1 < quantidade:
        return "Intervalo insuficiente para a quantidade desejada."

    numeros_sorteados = []

    while len(numeros_sorteados) < quantidade:
        numero_sorteado = random.randint(minimo, maximo)
        numeros_sorteados.append(numero_sorteado)

    return numeros_sorteados


st.title("Sorteio de Números")

minimo = st.number_input("Menor número:")
maximo = st.number_input("Maior número:")
quantidade = st.number_input("Quantidade:")

if st.button("Sortear"):
    resultado = realizar_sorteio(int(minimo), int(maximo), int(quantidade))

    st.write("Números sorteados:")

    # Exibir números em caixas individuais
    col1, col2, col3, col4, col5 = st.columns(5)

    for i, numero in enumerate(resultado, start=1):
        col_num = i % 5
        if col_num == 1:
            col1.write(f"Número {i}: {numero}")
        elif col_num == 2:
            col2.write(f"Número {i}: {numero}")
        elif col_num == 3:
            col3.write(f"Número {i}: {numero}")
        elif col_num == 4:
            col4.write(f"Número {i}: {numero}")
        else:
            col5.write(f"Número {i}: {numero}")


