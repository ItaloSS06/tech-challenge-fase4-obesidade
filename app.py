import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# ===============================
# CONFIGURAÇÃO DA PÁGINA
# ===============================
st.set_page_config(
  page_title="Predição de Obesidade",
  layout="wide"
)

# ===============================
# CARREGAMENTO DO MODELO
# ===============================
model = joblib.load("modelo_obesidade.pkl")

# ===============================
# TÍTULO E DESCRIÇÃO
# ===============================
st.title("Sistema Preditivo de Obesidade")
st.markdown("""
Este sistema utiliza um modelo de Machine Learning para auxiliar profissionais
da saúde na identificação do nível de obesidade com base em características
físicas e comportamentais dos indivíduos.
""")

# ===============================
# MENU LATERAL
# ===============================
menu = st.sidebar.radio(
  "Navegação",
  ["Visão Geral", "Predição", "Dashboard Analítico"]
)

# ===============================
# VISÃO GERAL
# ===============================
if menu == "Visão Geral":
  st.header("Visão Geral do Projeto")

  st.markdown("""
  ### Contexto
  A obesidade é uma condição de saúde multifatorial que pode trazer sérios
  riscos à saúde. Este projeto foi desenvolvido com o objetivo de apoiar
  equipes médicas por meio de um sistema preditivo baseado em dados.

  ### Objetivo
  - Analisar dados relacionados a hábitos, características físicas e
    comportamentais
  - Construir um modelo de Machine Learning
  - Disponibilizar uma aplicação interativa para apoio à decisão
  """)

  st.markdown("""
  **Modelo utilizado:** Random Forest  
  **Acurácia obtida:** 94,33%
  """)

# ===============================
# PREDIÇÃO
# ===============================
if menu == "Predição":
  st.header("Predição do Nível de Obesidade")

  col1, col2, col3 = st.columns(3)

  with col1:
      age = st.number_input("Idade", 0, 100)
      height = st.number_input("Altura (m)", 0.5, 2.5)
      weight = st.number_input("Peso (kg)", 10.0, 300.0)
      gender = st.selectbox("Gênero", ["Male", "Female"])
      family_history = st.selectbox("Histórico familiar de sobrepeso", ["yes", "no"])

  with col2:
      favc = st.selectbox("Consumo frequente de alimentos calóricos", ["yes", "no"])
      fcvc = st.slider("Consumo de vegetais", 0.0, 3.0)
      ncp = st.slider("Número de refeições diárias", 1.0, 4.0)
      caec = st.selectbox("Alimentação entre refeições", ["no", "Sometimes", "Frequently", "Always"])
      smoke = st.selectbox("Fuma", ["yes", "no"])

  with col3:
      ch2o = st.slider("Consumo diário de água", 1.0, 3.0)
      scc = st.selectbox("Monitora calorias", ["yes", "no"])
      faf = st.slider("Atividade física", 0.0, 3.0)
      tue = st.slider("Tempo em dispositivos tecnológicos", 0.0, 2.0)
      calc = st.selectbox("Consumo de álcool", ["no", "Sometimes", "Frequently", "Always"])
      mtrans = st.selectbox(
          "Meio de transporte",
          ["Public_Transportation", "Walking", "Automobile", "Motorbike", "Bike"]
      )

  if st.button("Prever nível de obesidade"):
      input_data = pd.DataFrame([{
          "Gender": gender,
          "Age": age,
          "Height": height,
          "Weight": weight,
          "family_history": family_history,
          "FAVC": favc,
          "FCVC": fcvc,
          "NCP": ncp,
          "CAEC": caec,
          "SMOKE": smoke,
          "CH2O": ch2o,
          "SCC": scc,
          "FAF": faf,
          "TUE": tue,
          "CALC": calc,
          "MTRANS": mtrans
      }])

      prediction = model.predict(input_data)
      st.success(f"Nível previsto de obesidade: **{prediction[0]}**")

# ===============================
# DASHBOARD ANALÍTICO
# ===============================
if menu == "Dashboard Analítico":
  st.header("Dashboard Analítico – Insights sobre Obesidade")

  df = pd.read_csv("Obesity.csv")
  df = df.rename(columns={"Obesity": "Obesity_level"})

  col1, col2 = st.columns(2)

  with col1:
      st.subheader("Distribuição dos níveis de obesidade")
      fig1, ax1 = plt.subplots()
      sns.countplot(x="Obesity_level", data=df, ax=ax1)
      ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45)
      st.pyplot(fig1)

  with col2:
      st.subheader("Peso por nível de obesidade")
      fig2, ax2 = plt.subplots()
      sns.boxplot(x="Obesity_level", y="Weight", data=df, ax=ax2)
      ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45)
      st.pyplot(fig2)

  st.markdown("""
  ### Principais insights
  - O peso corporal apresenta forte relação com o nível de obesidade.
  - Menor prática de atividade física está associada a níveis mais elevados.
  - Hábitos alimentares e comportamentais exercem influência significativa.
  """)
