---
content_hash: 22470bc725f815065785d9fb01610163a62cc31370ea4ce432bb2331c48b0bf3
fetched_at: '2026-06-29T00:09:30.694192+00:00'
page_id: '425458468'
product: rm
source: tdn-rm
title: Informações Estratégicas - Em Atraso
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458468
version: 1
---

**Informações Estratégicas - Em Atraso**   
Similar ao anexo de registros "Em Aberto" mas com a condição da data de vencimento diferente. Envolve as tabelas de Movimento, Itens de movimento, Lançamentos e Produtos. Filtrando os movimentos pelo cliente e através do movimento filtra os itens de movimento, retorna os lançamentos, referente ao movimento/itens de movimento, cuja data de vencimento é menor ou igual a data atual menos um dia (dia anterior) e o status do lançamento está setado como "Em Aberto". Retorna principalmente, entre outros, o valor em atraso. Exibe os campos código, produto, tipo e valor:   
                SELECT TMOV.NUMEROMOV, TPRD.NOMEFANTASIA NOMEPRODUTO, FLAN.DATAVENCIMENTO, TITMMOV.CODTIP,                        ROUND(SUM(FLAN.VALORORIGINAL \* TITMMOV.PRECOUNITARIO / TMOV.VALORLIQUIDO), 2) VALOR                 FROM TMOV (NOLOCK), TITMMOV (NOLOCK), FLAN (NOLOCK), TPRD (NOLOCK)                 WHERE     TMOV.CODCOLIGADA    = TITMMOV.CODCOLIGADA                       AND TMOV.IDMOV          = TITMMOV.IDMOV                       AND FLAN.STATUSLAN      = '0'                       AND FLAN.PAGREC         = 1                       AND FLAN.DATAVENCIMENTO <= (:DATAVENCIMENTO) - 1                       AND TMOV.CODCOLIGADA    = FLAN.CODCOLIGADA                       AND TMOV.IDMOV          = FLAN.IDMOV                       AND TMOV.CODCOLIGADA    = :CODCOLIGADA                       AND TMOV.CODCOLCFO      = :CODCOLCFO                       AND TMOV.CODCFO         IN (:CODCFO\_S)                       AND TITMMOV.CODCOLIGADA = TPRD.CODCOLIGADA                       AND TITMMOV.IDPRD       = TPRD.IDPRD                       /**and**/                 GROUP BY TMOV.NUMEROMOV, TPRD.NOMEFANTASIA, FLAN.DATAVENCIMENTO, TITMMOV.CODTIP  
Observação.:  
A consulta SQL que retorna as informações pode ser personalizada e setada nos Parâmetros Gerais do Sistema. Clique no aqui para maiores informações.
