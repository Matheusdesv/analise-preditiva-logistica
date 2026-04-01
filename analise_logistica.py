import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# 1. CARREGAMENTO DOS DADOS
arquivo = 'Logistica1000.xlsx.csv'

try:
    # O sep=None com engine='python' detecta se o CSV usa vírgula ou ponto-e-vírgula
    df = pd.read_csv(arquivo, sep=None, engine='python') 
    print(f"✅ Arquivo '{arquivo}' carregado com sucesso!")
except Exception as e:
    print(f"❌ Erro ao carregar o arquivo: {e}")
    exit()

# 2. TRATAMENTO (Ajustado com os nomes reais das suas colunas)
df['Prazo_Prometido'] = pd.to_datetime(df['Prazo_Prometido'], dayfirst=True)
df['Data_Entrega_Real'] = pd.to_datetime(df['Data_Entrega_Real'], dayfirst=True)

# Preenchendo entregas vazias com a data de hoje para cálculo de atraso
df['Data_Entrega_Real'] = df['Data_Entrega_Real'].fillna(pd.Timestamp.now())

# 3. CRIAÇÃO DO ALVO (Target)
# Atrasou = 1 se a entrega real passou do prazo prometido, senão 0
df['Atrasou'] = (df['Data_Entrega_Real'] > df['Prazo_Prometido']).astype(int)

# 4. PREPARAÇÃO DAS FEATURES
# Selecionando o que influencia o atraso
features = ['Transportadora', 'Valor_Frete']
X = pd.get_dummies(df[features], drop_first=True)
y = df['Atrasou']

# Dividindo 70% treino e 30% teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 5. TREINAMENTO COM RANDOM FOREST (O "Cérebro" do Projeto)
# O segredo está no class_weight='balanced'
modelo = RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42)
modelo.fit(X_train, y_train)

# 6. EXIBIÇÃO DOS RESULTADOS
y_pred = modelo.predict(X_test)

print("\n--- RELATÓRIO DE PERFORMANCE (MODELO BALANCEADO) ---")
print(classification_report(y_test, y_pred))

# Gerando a nova Matriz de Confusão
plt.figure(figsize=(8, 6))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Greens')
plt.title('Matriz de Confusão Balanceada: Previsão de Atrasos')
plt.xlabel('Previsão do Modelo (IA)')
plt.ylabel('Realidade (Dados Reais)')
plt.show()