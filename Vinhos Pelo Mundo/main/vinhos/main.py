import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Criando DataFrame fictício
dados = {
    "id": [1, 2, 3, 4, 5],
    "pais": ["Brasil", "França", "Itália", "EUA", "Chile"],
    "descricao": ["Vinho suave", "Aromático", "Encorpado", "Frutado", "Seco"],
    "designacao": ["Reserva", "Premium", "Clássico", "Especial", "Tradicional"],
    "pontos": [88, 92, 95, 90, 87],
    "preco": [50, 120, 200, 80, 60],
    "provincia": ["São Paulo", "Bordeaux", "Toscana", "California", "Valle Central"],
    "regiao1": ["Sudeste", "Bordeaux", "Chianti", "Napa", "Maipo"],
    "regiao2": ["Interior", "Gironde", "Florence", "Sonoma", "Santiago"],
    "nome_provador": ["Ana", "Pierre", "Giovanni", "John", "Maria"],
    "twitter_provador": ["@ana", "@pierre", "@giovanni", "@john", "@maria"],
    "nome_vinho": ["Reserva 2018", "Château 2015", "Chianti 2020", "Napa Valley 2019", "Maipo 2017"],
    "variedade": ["Cabernet", "Merlot", "Sangiovese", "Chardonnay", "Carmenere"],
    "vinicola": ["Vinícola SP", "Château Bordeaux", "Cantina Toscana", "Napa Wines", "Viña Maipo"]
}
vinhos = pd.DataFrame(dados)

# Conferindo colunas
print(vinhos.columns)

# Tratamento de nulos
for col in ["preco", "pontos"]:
    if col in vinhos.columns:
        vinhos[col] = vinhos[col].fillna(vinhos[col].median())
vinhos.fillna("Desconhecido", inplace=True)

sns.set_style("whitegrid")

# 1 País com maior número de vinhos
contagem = vinhos['pais'].value_counts().head(5).reset_index()
contagem.columns = ['pais', 'total']
plt.figure(figsize=(8,5))
sns.barplot(x='total', y='pais', data=contagem, palette='rocket')
plt.title('(TOP 5) - Total de Vinhos por País', color="firebrick", fontsize=16)
plt.tight_layout()
plt.show()

# 2 Média de pontos por país
media = vinhos.groupby('pais')['pontos'].mean().sort_values(ascending=False).reset_index()
plt.figure(figsize=(8,6))
sns.barplot(data=media, x='pontos', y='pais', palette='rocket')
plt.title('Média de Pontos por País', color="firebrick", fontsize=16)
plt.tight_layout()
plt.show()

# 3 Correlação preço x pontos
sns.scatterplot(data=vinhos, x='pontos', y='preco', color="midnightblue", alpha=0.6)
sns.regplot(data=vinhos, x='pontos', y='preco', scatter=False, color="firebrick")
plt.title('Correlação Preço x Pontos', color="firebrick", fontsize=16)
plt.tight_layout()
plt.show()

# 4 Variedade mais comum
contagem_var = vinhos['variedade'].value_counts().head(3).reset_index()
contagem_var.columns = ['variedade', 'total']
plt.figure(figsize=(8,5))
sns.barplot(data=contagem_var, x='variedade', y='total', palette='rocket')
plt.title('(TOP 3) - Variedades Mais Comuns', color="firebrick", fontsize=16)
plt.tight_layout()
plt.show()

# 5 Ranking custo-benefício (pontos/preço)
vinhos['ratio'] = vinhos['pontos'] / vinhos['preco']
melhores = vinhos[['nome_vinho','ratio']].sort_values(by='ratio', ascending=False).head(5)
print(melhores)
plt.figure(figsize=(10,5))
sns.barplot(data=melhores, x='ratio', y='nome_vinho', palette='rocket')
plt.title('(TOP 5) - Melhor Custo-Benefício (Pontos/Preço)', color="firebrick", fontsize=16)
plt.tight_layout()
plt.show()
