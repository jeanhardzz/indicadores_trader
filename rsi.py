#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd
dados = pd.read_csv("coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv")
dados.dropna(subset=dados.columns,inplace=True)
dados.index = range(dados.shape[0])
dados.info()




# # Índices de Força Relativa
# O indice de força relativa (RSI em inglês) foi desenvolvido por J. Welles Wilder. É um indice com escala de variação fixa, ou seja, varia entre 0 e 100.
# 
# É usado para identificar a subvalorização ou sobrevalorização de um ativo. Exemplo: Quanto maior o indice (>70) mais sobrevalorizada o ativo esta, e quanto menor o indice (<30) mais subvalorizada o ativo esta.
# 
# **IFR = 100 – (100 ÷ (1+ (U/D))**
# 
# 
# * IFR = Índice de Força Relativa
# * U = Média das cotações dos últimos n dias em que a cotação da ação subiu. Trata-se da soma das cotações dos últimos n dias em que a cotação da ação subiu, dividido por n.
# * D = Média das cotações dos últimos n dias em que a cotação da ação caiu. Trata-se da soma das cotações dos últimos n dias em que a cotação da ação caiu, dividido por n.
# * n = O numero de dias mais utilizado pelo mercado é 14, e recomendado por Wilder quando da publicação de seu livro. Por isso, esse é o default da plataforma gráfica de análise técnica do Bússola do Investidor. Mas também é comum usar um IFR de 9 ou 25 dias, e você pode customizar o indicador para quantos períodos desejar.

# In[28]:


import numpy as np

def calcula_indices_de_força_relativa(precos, n=14):
        """Retorna uma lista com os índices de força relativa dado uma Serie de preços"""
        # Qual que é a ideia
        # Calcular os deltas, que sao a diferença entre o preço[0] e o preço[1]
        # Calcular o rsi pros n primeiros deltas;
        # Esses n-rsi primeiros serao iguais obviamente;
        # Depois vou percorrer os deltas faltantes pra calcular os rsi faltantes
        # Dentro do for vou corrigindo os valores da media da taxa de cotação quando ela sobe e quando ela desce
        # Depois calculo o RSI usando a media da taxa de cotação corrigida

        
        # fazendo o calculo dos n primeiros pra inicializar a conta

        deltas = np.diff(precos)  # pegando a diferença preco[0]-preco[1] e guardando em deltas[0]
        primeiros = deltas[:n]  # pegando as diferença 14 primeiras diferenças
                
        ganho = primeiros[primeiros >= 0].sum() / n  # media das diferenças positivas dentre as 14 iniciais
        perda = -primeiros[primeiros < 0].sum() / n  # media das diferenças negativas dentre as 14 iniciais

        forca_relativa = ganho / perda  # calculando a força relativa

        rsi = np.zeros_like(precos)  # criando uma copia de precos só com zeros

        rsi[:n] = 100. - 100. / (1. + forca_relativa)  # calculando rsi para os 14 primeiros precos, serao iguais

        # print(deltas,primeiros,ganho,perda,rsi[:n+1], sep='\n')
        # print(deltas[:n+1])

        # for pra calcular o resto dos rsi
        for i in range(n, len(precos)):
            delta = deltas[i - 1]
            # tem que ser deltas[i-1] porque é a diferença do preço anterior com o preço atual
            # se fosse deltas[i] seria a diferença do preço atual com o proximo preço

            if (delta >= 0):
                ganho_variacao = delta
                perda_variacao = 0.
            else:
                ganho_variacao = 0.
                perda_variacao = -delta

            # corrigindo
            ganho = (ganho * (n - 1) + ganho_variacao) / n
            perda = (perda * (n - 1) + perda_variacao) / n

            forca_relativa = ganho / perda

            rsi[i] = 100. - 100. / (1. + forca_relativa)

        return rsi


# In[31]:


indice_rsi = calcula_indices_de_força_relativa(dados['Close'])
indice_rsi = pd.DataFrame(data=indice_rsi)
indice_rsi




