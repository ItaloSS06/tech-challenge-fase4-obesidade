# Tech Challenge – Fase 4 | Predição de Obesidade

## Contexto
Este projeto foi desenvolvido no contexto do **Tech Challenge – Fase 4** da Pós Tech, 
com o objetivo de aplicar os conhecimentos adquiridos ao longo da fase em um problema
real de negócio.

O desafio consiste em desenvolver um sistema preditivo capaz de auxiliar equipes
médicas na identificação do nível de obesidade de indivíduos, a partir de dados
demográficos, físicos e comportamentais.

---

## Objetivo
- Construir uma pipeline completa de Machine Learning
- Desenvolver um modelo preditivo para classificação dos níveis de obesidade
- Disponibilizar uma aplicação interativa para apoio à tomada de decisão
- Criar um dashboard analítico com insights relevantes para a área da saúde

---

## Base de Dados
O conjunto de dados utilizado contém informações como:
- Idade, altura e peso
- Hábitos alimentares
- Prática de atividade física
- Consumo de álcool
- Uso de dispositivos tecnológicos
- Histórico familiar de sobrepeso

A variável alvo representa os **níveis de obesidade**, classificados em diferentes
categorias, desde peso insuficiente até obesidade grau III.

---

## Modelo de Machine Learning
- **Algoritmo:** Random Forest
- **Tipo de problema:** Classificação multiclasse
- **Acurácia obtida:** **94,33%**

O modelo foi treinado a partir de uma pipeline que inclui:
- Tratamento de variáveis categóricas e numéricas
- Padronização dos dados
- Treinamento e avaliação do modelo

---

## Aplicação
A solução foi implementada por meio de uma aplicação desenvolvida em **Streamlit**,
integrando:

- Sistema preditivo para classificação do nível de obesidade
- Exibição das probabilidades por classe, aumentando a transparência do modelo
- Dashboard analítico com visualizações e insights relevantes

**Link da aplicação Streamlit:**  
https://tech-challenge-fase4-obesidade-6w5agnvl7bpoultcqxsr2h.streamlit.app

---

## Dashboard Analítico
O dashboard apresenta visualizações que permitem identificar padrões importantes
relacionados à obesidade, como:
- Distribuição dos níveis de obesidade
- Relação entre peso corporal e classificação de obesidade
- Insights que podem apoiar estratégias de prevenção e acompanhamento clínico

---

## Deploy e Produção
O modelo foi disponibilizado em produção utilizando o **Streamlit Cloud**, com controle
explícito do ambiente de execução, garantindo estabilidade, reprodutibilidade e
facilidade de acesso.
