# ============================================================================
# TRABALHO PRÁTICO DGT2823 - TECNOLOGIAS PARA DESENVOLVIMENTO DE BIG DATA
# MICRO ATIVIDADES
# Aluno: ALEX BARROSO PAZ
# Data: 12/06/2025
# ============================================================================

import pandas as pd
from io import StringIO

print("="*80)
print("TRABALHO PRÁTICO - PANDAS PARA ANÁLISE DE DADOS")
print("="*80)

# ============================================================================
# PREPARAÇÃO DO DATASET
# ============================================================================

print("\n1. CRIANDO O DATASET...")

# Dataset fornecido no trabalho
data_csv = """ID;Duration;Date;Pulse;Maxpulse;Calories
0;60;'2020/12/01';110;130;4091
1;60;'2020/12/02';117;145;4790
2;60;'2020/12/03';103;135;3400
3;45;'2020/12/04';109;175;2824
4;45;'2020/12/05';117;148;4060
5;60;'2020/12/06';102;127;3000
6;60;'2020/12/07';110;136;3740
7;450;'2020/12/08';104;134;2533
8;30;'2020/12/09';109;133;1951
9;60;'2020/12/10';98;124;2690
10;60;'2020/12/11';103;147;3293
11;60;'2020/12/12';100;120;2507
12;60;'2020/12/12';100;120;2507
13;60;'2020/12/13';106;128;3453
14;60;'2020/12/14';104;132;3793
15;60;'2020/12/15';98;123;2750
16;60;'2020/12/16';98;120;2152
17;60;'2020/12/17';100;120;3000
18;45;'2020/12/18';90;112;NaN
19;60;'2020/12/19';103;123;3230
20;45;'2020/12/20';97;125;2430
21;60;'2020/12/21';108;131;3642
22;45;NaN;100;119;2820
23;60;'2020/12/23';130;101;3000
24;45;'2020/12/24';105;132;2460
25;60;'2020/12/25';102;126;3345
26;60;20201226;100;120;2500
27;60;'2020/12/27';92;118;2410
28;60;'2020/12/28';103;132;NaN
29;60;'2020/12/29';100;132;2800
30;60;'2020/12/30';102;129;3803
31;60;'2020/12/31';92;115;2430"""

# Salvar como arquivo CSV
with open('dados_exercicio.csv', 'w') as f:
    f.write(data_csv)

print("✅ Dataset criado com sucesso!")

######
# Importar a biblioteca pandas
# Micro atividade 1 leitura de csv
import pandas as pd

# Criar uma variável para armazenar os dados
df_original = pd.read_csv('dados_exercicio.csv',
                         sep=';',           # Separador de colunas
                         engine='python',   # Engine de processamento
                         encoding='utf-8')  # Codificação

# Exibir os dados
print("Dataset carregado:")
print(df_original)

######
# Criar uma nova variável com subconjunto (3 colunas)
# Micro atividade 2
df_subconjunto = df_original[['ID', 'Duration', 'Pulse']]

# Exibir o subconjunto
print("Subconjunto com 3 colunas:")
print(df_subconjunto)

#####
# Configurar número máximo de linhas para exibição
# Micro atividade 3
pd.set_option('display.max_rows', 9999)

# Exibir dataset original usando to_string()
print("Dataset original com configuração de max_rows:")
print(df_original.to_string())
######
# Exibir primeiras 10 linhas
# Micro atividade 4
print("Primeiras 10 linhas:")
print(df_original.head(10))

print("\n" + "="*50 + "\n")

# Exibir últimas 10 linhas
print("Últimas 10 linhas:")
print(df_original.tail(10))
#####
# Exibir informações gerais sobre o dataset
# Micro atividade 5
print("Informações gerais do dataset:")
print(df_original.info())

print("\n" + "="*50 + "\n")

# Informações específicas solicitadas:
print("ANÁLISE DETALHADA:")
print(f"Total de linhas: {len(df_original)}")
print(f"Total de colunas: {len(df_original.columns)}")
print(f"Valores nulos por coluna:")
print(df_original.isnull().sum())
print(f"\nTipos de dados:")
print(df_original.dtypes)
print(f"\nMemória utilizada:")
print(df_original.memory_usage(deep=True))