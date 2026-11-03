---
content_hash: 16e3f6e073d14eead408606704286c2d16bfea4303f055dce80b3b5ba120e3f3
fetched_at: '2026-07-02T19:24:22.381020+00:00'
page_id: '269439179'
product: protheus
source: tdn-tec
title: Correção-Comportamento de LastRec() com tabelas temporárias.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269439179
version: 1
---

Esta build contém uma correção de comportamento da função LastRec(), quando usada com tabelas temporárias do DBAccess.

|  |  |
| --- | --- |
| Situação | Utilização de tabelas temporárias com o DBAccess |
| Ocorrência | * Caso uma tabela temporária seja utilizada e apagada, e posteriormente uma tabela temporária de mesmo nome seja utilizada, a contagem de registros – retornada pela função LastRec() – mostrava a quantidade de registros da tabela anterior, mesmo que a tabela atual tenha sido criada vazia. * Caso fosse realizada uma inserção na tabela temporária diretamente pelo SGDB – por exemplo, TCSqlEXEC() ou por Procedure ou Insert direto no SGDB – a função TCRefresh() não atualizava o LastRec() da tabela. |
| Correção | Ambos os casos foram resolvidos. Quanto à inserção direta no SGDB em tabela temporária, a função TCRefresh() pode ser utilizada para atualizar o contador de registros da tabela temporária. |
| Informações adicionais | * Referente ao chamado: TWBRY1 * Referente à ocorrência: SSIM-1233 * Disponível a partir do DBAccess Build 2016913, com data de geração igual ou superior a |
