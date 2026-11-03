---
content_hash: a8a101bba9adb395b6bf786f2df44e3f0718a05da3c9b20c27dc344aa5d4e081
fetched_at: '2026-06-29T00:06:14.980627+00:00'
page_id: '210050874'
product: rm
source: tdn-rm
title: DT_Calculo_Hora_Extra_Noturna_Parte1
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Calculo_Hora_Extra_Noturna_Parte1
version: 3
---

# CÁLCULO DE HORA EXTRA NOTURNA - PARTE  I

## Características do Requisito

  

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **TOTVS Automação de Ponto** |
| **Rotina:** | | **Rotina** | **Nome Técnico** | | --- | --- | | *Cálculo de Ponto* | *Cálculo de Adicional Noturno* | |
| **Versões/Release:** | *12.1.5* |

## Descrição

Através das funcionalidades compensação do cálculo, limite do banco de horas, lançamento das horas para o banco de horas, lançamento das horas para o movimento e exibição dos totais no espelho o usuário pode considerar o percentual de adicional noturno para as horas noturnas

## Procedimento para Utilização

Os parâmetros a seguir consideram o percentual de banco de horas:

Ao exibir o saldo do banco de horas:

Irá considerar o percentual do evento do banco de horas para exibição e definição do saldo.

Na compensação do banco de horas:

Irá considerar o percentual do evento do banco de horas para o processo de compensação.

Considera percentual de incidência no Banco de Horas:

Irá aplicar o percentual no momento que as horas forem lançadas para o banco de horas

Caso esse parâmetro esteja marcado, o parâmetro “Considera percentual ao exibir o saldo do banco de horas” é desabilitado para que o percentual não seja considerado duas vezes. Ele será habilitado somente se o parâmetro “Considera percentual de incidência do evento do banco / Saldo do banco de horas” estiver marcado.

Os seguintes parâmetros  consideram o percentual no limite do banco de horas:

Limite executado por dia:

Aplica o limite em todo o executado do dia.

Limite executado por semana:

Aplica o limite em todo o executado da semana.

Limite executado por período:

Aplica o limite em todo o executado do período.

Considera percentual para o limite do banco de horas:

Irá considerar o percentual ao aplicar o limite do banco de horas.

Considerando limite de extra diário de 02:00  
Se o funcionário fez 1:45 de extra noturna, sem considerar o percentual não ultrapassa o limite de extra, porém, se considerar, iria de 1:45 para 2:01 ultrapassando o limite, fazendo com que a partir de 1:45 seja alterado a atitude ou a faixa.

Considerando limite de executado diário de 10:00  
Se o funcionário fez 08:00 de trabalho noturno e 0:48 de extra noturna, sem considerar o percentual não ultrapassa o limite de executado, porém, se considerar, iria de 08:00 para 09:06 de trabalho e de 0:48 para 0:55 de extra ultrapassando o limite, fazendo com que a partir de 0:48 seja alterado a atitude ou a faixa

Início def. limite: Início do dia/Fim do dia

Por padrão irá aplicar o limite a partir do início do dia, podendo alternar para aplicar a partir do fim do dia.

Início def. limite: Início da semana/Fim da semana

Por padrão irá aplicar o limite a partir do início da semana, podendo alternar para aplicar a partir do fim da semana.

Início def. limite: Início do período/Fim do período

Por padrão irá aplicar o limite a partir do início do período, podendo alternar para aplicar a partir do fim do período.

Parâmetros que consideram o percentual do movimento:

Considera percentual de incidência no Movimento:

Aplica o percentual no momento que as horas forem lançadas para o movimento

**Espelho .NET**

Na visão dos totais do dia tem um menu para configuração das colunas, assim como nas visões padrões do sistema, para que o usuário possa escolher as colunas a serem exibidas e para definir a ordem.

Os seguintes parâmetros consideram o percentual na configuração do espelho:

% de incidência:

Define qual o percentual será aplicado para o tipo de ocorrência do cadastro.

Intervalo a considerar:

Define para qual intervalo de horas o percentual será aplicado.

Ex: Tipo de Ocorrência: EA (Extra autorizada)  
       % incidência: 1,1429  
        Intervalo a considerar: 22:00 a 05:00

No caso acima, todas as ocorrências que fizerem interseção com esse intervalo terão suas horas multiplicadas pelo percentual. O que não fizer interseção não será aplicado:

Ocorrência 1: EA – 00:00 a 01:00  - O percentual será aplicado  
Ocorrência 2: EA – 09:00 a 09:30  - O percentual não será aplicado
