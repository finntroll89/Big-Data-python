# ============================================================================
# TRABALHO PRÁTICO DGT2823 - TECNOLOGIAS PARA DESENVOLVIMENTO DE BIG DATA
# Limpeza de Dados com Pandas codigo principal 
# ============================================================================

import pandas as pd
from io import StringIO

print("="*80)
print("TRABALHO PRÁTICO - LIMPEZA DE DADOS COM PANDAS")
print("="*80)

# ============================================================================
# PASSO 1: PREPARAÇÃO DO DATASET OBRIGATÓRIO
# ============================================================================

# Dataset fornecido obrigatoriamente no trabalho
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

print("✅ Dataset obrigatório criado!")

# ============================================================================
# PASSOS 2-4: LEITURA DO CSV E ATRIBUIÇÃO A VARIÁVEL
# ============================================================================

print("\n📋 PASSOS 2-4: LEITURA DO ARQUIVO CSV")

# Lendo o CSV com os parâmetros necessários
df_original = pd.read_csv('dados_exercicio.csv',
                         sep=';',           # Separador de colunas
                         engine='python',   # Engine de processamento
                         encoding='utf-8')  # Codificação

print("✅ Dados lidos e atribuídos à variável 'df_original'")

# ============================================================================
# PASSO 5: VERIFICAÇÃO DOS DADOS IMPORTADOS
# ============================================================================

print("\n📋 PASSO 5: VERIFICAÇÃO DOS DADOS IMPORTADOS")

print("\n5a. Informações gerais sobre o conjunto de dados:")
print(df_original.info())

print("\n5b. Primeiras 5 linhas:")
print(df_original.head())

print("\n5b. Últimas 5 linhas:")
print(df_original.tail())

# ============================================================================
# PASSO 6: CRIAR CÓPIA DO CONJUNTO ORIGINAL
# ============================================================================

print("\n📋 PASSO 6: CRIANDO CÓPIA DOS DADOS ORIGINAIS")

df_limpo = df_original.copy()
print("✅ Cópia criada na variável 'df_limpo'")

# ============================================================================
# PASSO 7: TRATAR VALORES NULOS EM 'CALORIES'
# ============================================================================

print("\n📋 PASSO 7: TRATAMENTO DE VALORES NULOS EM 'CALORIES'")

print("7a. Substituindo valores nulos da coluna 'Calories' por 0:")
df_limpo['Calories'] = df_limpo['Calories'].fillna(0)

print("7b. Verificando se a mudança foi aplicada:")
print(df_limpo)

# ============================================================================
# PASSO 8: TRATAR VALORES NULOS EM 'DATE'
# ============================================================================

print("\n📋 PASSO 8: TRATAMENTO INICIAL DE VALORES NULOS EM 'DATE'")

print("8a. Substituindo valores nulos da coluna 'Date' por '1900/01/01':")
df_limpo['Date'] = df_limpo['Date'].fillna('1900/01/01')

print("8b. Verificando se a mudança foi aplicada:")
print(df_limpo)

print("8c. Tentativa de transformar coluna 'Date' em datetime:")
try:
    df_limpo['Date'] = pd.to_datetime(df_limpo['Date'], format='%Y/%m/%d')
    print("✅ Conversão realizada com sucesso!")
except Exception as e:
    print(f"❌ ERRO ENCONTRADO: {e}")

# ============================================================================
# PASSO 9: RESOLVER PRIMEIRO ERRO
# ============================================================================

print("\n📋 PASSO 9: RESOLVENDO PRIMEIRO ERRO")

print("9a. Substituindo '1900/01/01' por NaN:")
df_limpo['Date'] = df_limpo['Date'].replace('1900/01/01', pd.NaT)

print("9b. Nova tentativa de conversão para datetime:")
try:
    df_limpo['Date'] = pd.to_datetime(df_limpo['Date'], format='%Y/%m/%d')
    print("✅ Conversão realizada com sucesso!")
except Exception as e:
    print(f"❌ AINDA COM ERRO: {e}")

print("9c. Verificando mudanças:")
print(df_limpo)

# ============================================================================
# PASSO 10: RESOLVER SEGUNDO ERRO (FORMATO "20201226")
# ============================================================================

print("\n📋 PASSO 10: RESOLVENDO SEGUNDO ERRO - FORMATO INCONSISTENTE")

print("Corrigindo valor '20201226' para formato correto:")
df_limpo['Date'] = df_limpo['Date'].replace('20201226', '2020/12/26')
print("✅ Formato inconsistente corrigido!")

# ============================================================================
# PASSO 11: CONVERSÃO FINAL PARA DATETIME
# ============================================================================

print("\n📋 PASSO 11: CONVERSÃO FINAL PARA DATETIME")

print("Executando transformação final para datetime:")
df_limpo['Date'] = pd.to_datetime(df_limpo['Date'], format='%Y/%m/%d', errors='coerce')

print("✅ Transformação final executada com sucesso!")
print("Verificando resultado:")
print(df_limpo)
print(f"\nTipo da coluna Date: {df_limpo['Date'].dtype}")

# ============================================================================
# PASSO 12: REMOÇÃO DE REGISTROS COM VALORES NULOS
# ============================================================================

print("\n📋 PASSO 12: REMOVENDO REGISTROS COM VALORES NULOS")

print("Valores nulos antes da remoção:")
print(df_limpo.isnull().sum())

linhas_antes = len(df_limpo)
df_limpo = df_limpo.dropna()
linhas_depois = len(df_limpo)

print(f"\n✅ Remoção executada:")
print(f"   Linhas antes: {linhas_antes}")
print(f"   Linhas depois: {linhas_depois}")
print(f"   Linhas removidas: {linhas_antes - linhas_depois}")

# ============================================================================
# PASSO 13: VERIFICAÇÃO FINAL
# ============================================================================

print("\n📋 PASSO 13: VERIFICAÇÃO FINAL E RESULTADO")
print("="*80)
print("🎯 DATASET FINAL APÓS LIMPEZA:")
print("="*80)
print(df_limpo)

print(f"\n📊 RESUMO FINAL:")
print(f"   ✅ Total de registros finais: {len(df_limpo)}")
print(f"   ✅ Total de colunas: {len(df_limpo.columns)}")
print(f"   ✅ Valores nulos restantes: {df_limpo.isnull().sum().sum()}")

print(f"\n📋 TIPOS DE DADOS FINAIS:")
print(df_limpo.dtypes)

print(f"\n📈 ESTATÍSTICAS DESCRITIVAS:")
print(df_limpo.describe())

# ============================================================================
# VALIDAÇÃO FINAL
# ============================================================================

print("\n" + "="*80)
print("🔍 VALIDAÇÃO DOS RESULTADOS")
print("="*80)

# Verificações de qualidade
print("✅ Verificações de qualidade dos dados:")

# 1. Verificar valores nulos
nulos = df_limpo.isnull().sum().sum()
print(f"   1. Valores nulos no dataset final: {nulos} {'✅' if nulos == 0 else '❌'}")

# 2. Verificar tipo da coluna Date
eh_datetime = df_limpo['Date'].dtype == 'datetime64[ns]'
print(f"   2. Coluna Date é datetime: {'✅' if eh_datetime else '❌'}")

# 3. Verificar registros com Calories = 0
calories_zero = (df_limpo['Calories'] == 0).sum()
print(f"   3. Registros com Calories = 0: {calories_zero}")

# 4. Verificar total de registros
print(f"   4. Total de registros finais: {len(df_limpo)}")

print(f"\n🎉 TRABALHO PRÁTICO CONCLUÍDO!")
print("="*80)

# Salvar resultado final
df_limpo.to_csv('dataset_limpo_final.csv', index=False, sep=';')
print("💾 Dataset limpo salvo como 'dataset_limpo_final.csv'")

