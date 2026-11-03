---
content_hash: 165b0be41b3320b7c0f8dcf4e955aa10f2e185e3084cd6ccaf7b5fd29f440bec
fetched_at: '2026-06-29T00:09:24.552881+00:00'
page_id: '423937959'
product: rm
source: tdn-rm
title: Reabertura de Competência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423937959
version: 6
---

Dica

O processo é multicoligada a partir da versão 12.1.2310.

A reabertura de competência tem como objetivo retornar o período de cálculo do sistema para o último liberado, ou seja, se o período atual for 01/2024, após a execução do processo ele retornará para 12/2023.

Por ser um processo *multicoligadas* é possível realizar a reabertura de período de várias coligadas simultaneamente, respeitando suas respectivas diferenças.

Por que o processo de Reabertura de Competência é necessário?

Após executar o processo de liberação de competência não é possível realizar aquisições, transferências de controle e operações patrimoniais no período anterior ao vigente, pois estas ações afetariam o saldo anterior.

Para executar estas tarefas, em um período de cálculo anterior ao corrente, sem afetar o saldo anterior é necessário reabrir a competência.

Atenção as listas de informações que serão excluídas

Antes do processo ser executado são exibidas as contabilizações da depreciação, correção monetária, realização da avaliação, correção da avaliação, ocorrências de baixa, acréscimo, transferência monetária, *impairment* e transferências de controle existente no período de cálculo vigente.

Durante a execução do processo a primeira atividade a ser realizada será a exclusão das contabilizações das ocorrências de acréscimo, baixa, transferência monetária e *impairment*. Em seguida serão excluídas as contabilizações da depreciação/correção monetária e da transferência de controle. Vale ressaltar que as contabilizações integradas também serão excluídas, porém se elas estiverem integradas ao lote zero não será possível executar o processo. Neste caso, antes de realizar a reabertura de competência será necessário solicitar a exclusão, via tarefa, de todas as contabilizações integradas a este lote e depois excluí-las no Totvs Gestão Contábil.

Precauções e sugestões

Para sua segurança faça um backup da base de dados. Se por algum motivo a reabertura de competência não se completar verifique o log. Caso seja necessário restaure imediatamente o backup e inicie o processo novamente.  
  
O período de cálculo será atualizado para o MÊS/ANO anterior ao período atual. Sugerimos que este processo seja feito em um horário fora do expediente normal de trabalho, pois caso seja necessário voltar o backup as outras áreas da empresa não serão afetadas.

Em quais situações a reabertura não acontecerá?

Para realizar esta tarefa não poderão haver contabilizações integradas ao lote zero, caso tenha o sistema irá apresenta a mensagem abaixo no log:  
"Existem contabilizações integradas ao lote zero. Solicite a exclusão delas através do recurso de tarefa. Em seguida requisite a exclusão destas contabilizações, no Saldus, pelo contador da empresa."

O período de cálculo anterior também não poderá ter sido fechado. Ao tentar reabrir períodos fechados o sistema exibirá a mensagem:   
"Não é possível realizar a reabertura, pois o período anterior está fechado."
