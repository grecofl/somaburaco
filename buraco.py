# -*- coding: UTF-8 -*-

"""

Esse programa tem o objetivo de criar uma aplicação que seja útil para jogadores de buraco.
As variáveis serão declaradas abaixo, de acordo com o tipo de dado que a mesma receberá

"""

# Variáveis to tipo STRING
""" 
    jogador01           ->  Nome do Primeiro Jogador
    jogador02           ->  Nome do Segundo Jogador
    jogador03           ->  Nome do Terceiro Jogador
    jogador04           ->  Nome do Quarto Jogador
    dupla01             ->  Será constituída do Jogador 01 e do Jogador 02
    dupla02             ->  Será constituída do Jogador 03 e do Jogador 04
"""

# Variáveis do tipo INT
"""
    cartas_dupla01      ->  Total de pontos da rodada que a dupla01 realizou em pontos de cartas (somatória de pontos das cartas disponíveis na mesa)
    cartas_dupla02      ->  Total de pontos da rodada que a dupla02 realizou em pontos de cartas (somatória de pontos das cartas disponíveis na mesa)
    mesa_dupla01        ->  Total de pontos da rodada que a dupla01 realizou em pontos de mesa (canastras limpas, canastras sujas, canastra real, batida, etc)
    mesa_dupla02        ->  Total de pontos da rodada que a dupla01 realizou em pontos de mesa (canastras limpas, canastras sujas, canastra real, batida, etc)
    rodada_dupla01      ->  Total de pontos da rodada que a dupla01 obteve no somatório dos pontos de cartas e de mesa
    rodada_dupla02      ->  Total de pontos da rodada que a dupla01 obteve no somatório dos pontos de cartas e de mesa
    total_dupla01       ->  Total de pontos da rodada que a dupla01 obteve no somatório das rodadas
    total_dupla02       ->  Total de pontos da rodada que a dupla01 obteve no somatório das rodadas
    total_partida       ->  Total de pontos para fechar uma partida
    total_vulneravel    ->  Total de pontos para ficar vulnerável
"""

# Variáveis do tipo LISTA
"""
    tipo_contagem       ->  Declara o tipo de contagem de pontos que será realizada, podendo ser do tipo CONTÍNUA (pontos de cartas e mesa somados num único insert de dados) ou PARCIAL (pontos de mesa separados dos pontos de cartas)
    valor_partida       ->  Declara o valor da partida, podendo ser de 3.000, 5.000 ou 10.000 pontos
"""

# Define o Nome dos Jogadores

jogador01 input ('Digite o Nome do Jogador 1: ')
jogador02 input ('Digite o Nome do Jogador 2: ')
jogador03 input ('Digite o Nome do Jogador 3: ')
jogador04 input ('Digite o Nome do Jogador 4: ')


print ('O jogo será entre a Dupla 01 ', jogador01, ' e ', jogador02, ' versus a Dupla 02 ', jogador03, ' e ', jogador04)

dupla01 = jogador01,jogador02
dupla02 = jogador03,jogador04


# Seleciona o Valor da Partida e Tipo de Contagem de Pontos

print ('Defina o Valor da Partida')
valor_partida [3.000, 5.000, 10.000]
total_partida = valor_partida

print ('Defina o Tipo de Contagem que será utilizada')
print ('A contagem CONTÍNUA coloca os valores num único campo, sendo a soma dos pontos da mesa e de cartas da rodada. \n\ A contagem PARCIAL coloca os valores em dois campos diferentes, sendo um para os pontos de mesa e outro para os pontos de cartas da rodada')
tipo_contagem ["CONTÍNUA", "PARCIAL"]

# Define o Valor de Pontos para as Duplas para o Início da Partida

total_dupla01 = 0
total_dupla02 = 0

# Define o Valor para ficar Vulnerável

total_vulneravel == valor_partida/2

# Realiza o Somatório da Rodada Através do Tipo de Contagem Selecionada

if tipo_contagem == CONTÍNUA:

    then
    
        rodada_dupla01 = input ('Informe o Valor de Pontos obtidos na Rodada pela Dupla 01: ')
        rodada_dupla02 = input ('Informe o Valor de Pontos obtidos na Rodada pela Dupla 02: ')

elif tipo_contagem == PARCIAL:

    then
        # Informa os Valores de Pontos da Rodada Obtidos pela Dupla 01
        mesa_dupla01 = int (input ('Informe o Valor de Pontos de Mesa obtidos na Rodada pela Dupla 01: '))
        cartas_dupla01 = int (input (input ('Informe o Valor de Pontos de Cartas obtidos na Rodada pela Dupla 01: '))
        # Realiza a soma de pontos de mesa e cartas da Dupla 01 na rodada atual
        rodada_dupla01 = mesa_dupla01 + cartas_dupla01

        # Informa os Valores de Pontos da Rodada Obtidos pela Dupla 01
        mesa_dupla02 = int (input ('Informe o Valor de Pontos de Mesa obtidos na Rodada pela Dupla 02: '))
        cartas_dupla02 = int (input (input ('Informe o Valor de Pontos de Cartas obtidos na Rodada pela Dupla 02: '))
        # Realiza a soma de pontos de mesa e cartas da Dupla 01 na rodada atual
        rodada_dupla02 = mesa_dupla02 + cartas_dupla02

# Realiza o Somatório das Rodadas e coloca o Valor no Total da Dupla
                          
total_dupla01 = total_dupla01 + rodada_dupla01
total_dupla02 = total_dupla02 + rodada_dupla02

# Verifica condição de Vulnerabilidade e Informa condição ao Usuário

if total_dupla01 > total_vulneravel:
                          
   elif total_dupla02 > total_vulneravel:
                          
        print ('As Duplas estão vulneráveis!!!')
   
    else print ('A Dupla 01 está vulnerável!!!'):
    
    else if total_dupla02 > total_vulneravel:

    print ('A Dupla 02 está Vulnerável!!!')

# Verifica o fim da partida

if total_dupla01 > total_partida:

    elif total_dupla01 > total_dupla02:
        
        print ('A Dupla 01 venceu a partida!!!')
    
    else if total_dupla02 > total_partida:
                              
        print ('A Dupla 02 venceu a partida!!!')
