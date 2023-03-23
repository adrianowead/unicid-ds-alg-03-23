import numpy as np
import pandas as pd
from faker import Faker

# Definir o número de linhas
n = 1000

mean1 = [0.5, 0.4, 0.3, 0.8, 2] # média das colunas numérica

cov1 = [[7, 0, 0, 0, 0],
        [0, 3, 0, 0, 0],
        [0, 0, 8, 0, 0],
        [0, 0, 0, 10, 0],
        [0, 0, 0, 0, 4]] # matriz de covariância das colunas numéricas

noise_scale = 0.1 # escala do ruído a ser adicionado às colunas numéricas

# gerando os dados sintéticos
fake = Faker()
np.random.seed(42)

# gerando as colunas de dados categóricos
idades = np.random.randint(18, 80, size=n)
generos = np.random.choice(['Masculino', 'Feminino'], size=n)
estados_civis = np.random.choice(['Solteiro', 'Casado', 'Divorciado', 'Viúvo'], size=n)

# gerando as colunas de dados numéricos com uma distribuição normal
dados_numericos = np.abs(np.random.multivariate_normal(mean1, cov1, size=n))

# adicionando ruído às colunas numéricas
ruido = np.random.normal(0, noise_scale, size=(n, 5))
dados_numericos += ruido

# criando o DataFrame com todas as colunas
dados = pd.DataFrame({
    'idade': idades,
    'genero': generos, 
    'estado_civil': estados_civis,
    'email': dados_numericos[:, 0].astype(int),
    'sms': dados_numericos[:, 1].astype(int),
    'mala_direta': dados_numericos[:, 2].astype(int),
    'produtos_comprados': dados_numericos[:, 3].astype(int)
})

# salvando o DataFrame como arquivo CSV
dados.to_csv('dados_sinteticos.csv', index=False)