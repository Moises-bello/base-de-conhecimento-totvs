---
content_hash: 2c6e76d4ba28ba3a0e6de7edb81f5206a5e88bc21b1f1eaa0260427fde5c210a
fetched_at: '2026-06-29T00:08:15.678917+00:00'
page_id: '244920410'
product: rm
source: tdn-rm
title: RMPAT00003_Reabertura de Competência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244920410
version: 6
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS GESTÃO PATRIMONIAL |
| **Versões:** | 12.1.16 ou superior |
| **Ocorrência:** | Reabertura de Competência |
| **Ambiente:** |  |
| **Passo a passo:** | O processo de [Liberação de Competência](https://tdn.totvs.com/pages/viewpage.action?pageId=423938326) realiza a transposição de um mês/ano de cálculo para o próximo mês/ano. Após sua execução não é possível realizar aquisições, transferências de controle e operações patrimoniais no período anterior ao vigente, pois estas ações afetariam o saldo anterior.  Para executar estas tarefas, em um período de cálculo anterior ao corrente, sem afetar o saldo anterior é necessário **Reabrir a Competência**. A Reabertura de Competência tem como objetivo realizar a transposição de um mês/ano de cálculo para o mês/ano anterior, ou seja, se o período atual for 04/2015, após a execução do processo ele retornará para 03/2015.  Para realizar esta tarefa não poderão haver contabilizações integradas ao lote zero, caso tenha o sistema irá apresenta a mensagem abaixo: “Existem contabilizações integradas ao lote zero. Solicite a exclusão delas através do recurso de tarefa. Em seguida requisite a exclusão destas contabilizações, no Saldus, pelo contador da empresa.”  O período de cálculo anterior também não poderá ter sido fechado. Ao tentar reabrir períodos fechados o sistema exibirá a mensagem: “Não é possível realizar a reabertura, pois o período anterior está fechado.”  Para sua segurança faça um backup da base de dados. Se por algum motivo a reabertura de competência não se completar verifique o log. Caso seja necessário restaure imediatamente o backup e inicie o processo novamente.  O período de cálculo será atualizado para o MÊS/ANO anterior ao período atual. Sugerimos que este processo seja feito em um horário fora do expediente normal de trabalho, pois caso seja necessário voltar o backup as outras áreas da empresa não serão afetadas.    Disponível através do **Menu | Utilitários | Liberações | Reabertura de Competência**.        Durante a execução do processo a primeira atividade a ser realizada será a exclusão das contabilizações das ocorrências de acréscimo, baixa, transferência monetária e impairment. Em seguida serão excluídas as contabilizações da depreciação/correção monetária e da transferência de controle, além disso todas ocorrências citados anteriormente também serão excluídas.  Vale ressaltar que as contabilizações integradas também serão excluídas, porém se elas estiverem integradas ao lote zero não será possível executar o processo. Neste caso, antes de realizar a reabertura de competência será necessário solicitar a exclusão, via tarefa, de todas as contabilizações integradas a este lote e depois excluí-las no Totvs Gestão Contábil. |
| **Observações:** |  |
