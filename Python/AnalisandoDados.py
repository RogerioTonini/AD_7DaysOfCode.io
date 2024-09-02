""" 
# ALURA - Desafio: 7DaysOfCode - Junho/2024
# Dia 3: Analise dos dados 
"""
import pandas as pd
import os
#
pd.options.display.max_rows = 10000
pd.options.display.max_columns = 30
#
def fxCorrigeDataHora(_df, _strNomeColuna):
    _intContReg   = 1
    _lstDataHora = []
    for conteudo in _df[_strNomeColuna]:
        if str(conteudo) == 'nan':
            conteudo = ''
        elif len(conteudo) > 16:
            conteudo = conteudo[:16]
        #
        _lstDataHora.append(conteudo)
        print(f'Coluna: {_strNomeColuna}, Registro: {str(_intContReg)}, Data: {conteudo}')
        _intContReg += 1 
    #
    _df[_strNomeColuna]= _lstDataHora
    return None
#
_strExtArquivo    = '.csv'
_strDB_Emprestimo = 'DB_Emprestimo' + _strExtArquivo
_strPathData      = r'D:\Users\rtoni\OneDrive\Git-Dados\Projetos\7DaysOfCode.io'       # Pasta que armazena o arquivo
"""
# Carrega o arquivo DB_Emprestimo.csv
"""
try:
    _strPathFile  = os.path.join(_strPathData, _strDB_Emprestimo)
    df_Emprestimo = pd.read_csv(_strPathFile, sep=';', engine='c')
    #
    fxCorrigeDataHora(df_Emprestimo, 'data_emprestimo')
    fxCorrigeDataHora(df_Emprestimo, 'data_devolucao')
    fxCorrigeDataHora(df_Emprestimo, 'data_renovacao')
    print(df_Emprestimo.head())
    df_Emprestimo.to_csv(_strPathFile, header=True, index=False, sep=';')
    print("Processo finalizado")
except OSError as e:
    print(e)
