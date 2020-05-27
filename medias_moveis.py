#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
dados = pd.read_csv("coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv")
dados.info()


# # Médias Móveis
# 
# Média Móvel é uma media do preço dos ultimos N fechamentos de um ativo.
# 
# Sendo que o N é chamado de periodo, e esta sendo utilizando um periodo de 20. Dependendo do dataset, 20 periodos podem ser 20 minutos, 20 horas, 20 dias ou 20 anos.
# 
# No dataset utilizado 20 periodos representam 20 minutos.

# In[3]:


medias_moveis=dados['Close'].rolling(window=20).mean()
print(media_moveis)


# # Médias Móveis Exponenciais
# 
# Média Móvel Exponencial é uma media ponderada do preço dos ultimos N fechamentos de um ativo, dando mais peso para os fechamentos mais próximos.
# 
# Sendo que o N é chamado de periodo, e esta sendo utilizando um periodo de 20. Dependendo do dataset, 20 periodos podem ser 20 minutos, 20 horas, 20 dias ou 20 anos.
# 
# No dataset utilizado 20 periodos representam 20 minutos.

# In[4]:


media_movel_exponencial = dados['Close'].ewm(span=20, adjust=False).mean()
print(media_movel_exponencial)

