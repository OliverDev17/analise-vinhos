import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Criando DataFrame fictício (sem depender de CSV)
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
print(vinhos.info())
print(vinhos.isna().sum())

# Tratamento de nulos (não vai alterar nada aqui, mas mantém robustez)
for col in ["preco", "pontos"]:
    vinhos[col] = vinhos[col].fillna(vinhos[col].median())
vinhos.fillna("Desconhecido", inplace=True)

# Exemplo de gráfico simples para validar
sns.set_style("whitegrid")
plt.figure(figsize=(8,5))
sns.barplot(x="pais", y="pontos", data=vinhos, palette="rocket")
plt.title("Pontuação média por país (dataset fictício)", color="firebrick", fontsize=16)
plt.xlabel("País", fontsize=14, color="firebrick")
plt.ylabel("Pontos", fontsize=14, color="firebrick")
plt.tight_layout()
plt.show()
