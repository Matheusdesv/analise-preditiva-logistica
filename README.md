# 🚚 Análise Preditiva de Entregas Logísticas (OTIF)

Projeto de ponta a ponta desenvolvido para identificar padrões de atraso e prever a pontualidade de entregas utilizando Machine Learning.

## 🎯 Objetivo do Projeto
Transformar dados brutos de logística em insights estratégicos, saindo de uma análise descritiva (o que aconteceu) para uma preditiva (o que pode acontecer).

## 🛠️ Tecnologias e Habilidades
* **SQL:** Extração e tratamento de dados (ETL) via CTEs.
* **Python (Pandas, Scikit-Learn):** Ciência de Dados aplicada com foco em desbalanceamento de classes.
* **Machine Learning:** Implementação de modelo Random Forest Classifier.
* **Power BI:** Dashboard executivo para monitoramento de KPIs (OTIF e Frete).

## 🧠 O Diferencial Técnico
Neste projeto, identifiquei que o modelo inicial ignorava os atrasos por serem a minoria nos dados (85% de acertos "fáceis"). Apliquei a técnica de **pesos balanceados (`class_weight='balanced'`)**, permitindo que a IA realmente aprendesse a identificar os gargalos logísticos.

### Performance do Modelo (Antes vs Depois)

<img width="353" height="77" alt="teste 1" src="https://github.com/user-attachments/assets/f16acd1b-66c9-4cd8-a637-929137f5d07f" />
<img width="512" height="209" alt="teste 2" src="https://github.com/user-attachments/assets/527fadcb-555b-4ca9-99b4-db8bbd45bf84" />

### Visualização de Erros (Matriz de Confusão)
<img width="800" height="600" alt="Figure_2" src="https://github.com/user-attachments/assets/fa27b8aa-b500-44bd-9044-88115792ff0e" />

## 📊 Business Intelligence (Power BI)

A etapa final consistiu na criação de um dashboard estratégico para monitorização dos KPIs logísticos em tempo real.

### 📌 Principais Indicadores (KPIs):
* **OTIF (On-Time In Full):** Percentual de entregas feitas no prazo e sem avarias.
* **Lead Time Médio:** Tempo médio de ciclo do pedido até à entrega final.
* **Análise de Custos:** Visibilidade total sobre o gasto com fretes por transportadora.

### 🧠 Diferenciais Técnicos no Power BI:
* **Modelagem Star Schema:** Estruturação eficiente das tabelas para performance.
* **DAX Avançado:** Criação de medidas dinâmicas para análise de tendências.
* **Storytelling:** Visuals focados na tomada de decisão executiva.

<img width="1484" height="834" alt="image" src="https://github.com/user-attachments/assets/204b07be-c7a1-4a9c-92dc-a22fa9adb071" />

**Formação:** Tecnólogo em Ciência de Dados - Mackenzie (2025)
