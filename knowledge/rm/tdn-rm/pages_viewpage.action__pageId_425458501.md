---
content_hash: fd61116f5f0e61d9f978ac6f461c809165224b1d9eb73bc91b819ec4f835a7ce
fetched_at: '2026-06-29T00:09:30.745418+00:00'
page_id: '425458501'
product: rm
source: tdn-rm
title: Informações Estratégicas - Em Aberto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458501
version: 1
---

**Informações Estratégicas - Em Aberto**   
Envolve as tabelas de Movimento, Itens de movimento, Lançamentos e Produtos. Filtrando os movimentos pelo cliente e através do movimento filtra os itens de movimento, retorna os lançamentos, referente ao movimento/itens de movimento, cuja data de vencimento é maior ou igual a data atual e o status do lançamento está setado como "Em Aberto".   
Retorna principalmente, entre outros, o valor em aberto (valor faturado - valor pago). Exibe os campos código, produto, tipo e valor:  
SELECT TPRD.CODIGOPRD, TPRD.NOMEFANTASIA NOMEPRODUTO, TITMMOV.CODTIP, FLAN.DATAVENCIMENTO,   
                       ROUND(SUM(FLAN.VALORORIGINAL \* TITMMOV.PRECOUNITARIO / TMOV.VALORLIQUIDO), 2) VALOR   
                FROM TMOV (NOLOCK), TITMMOV (NOLOCK), FLAN (NOLOCK), TPRD (NOLOCK)  
                WHERE     TMOV.CODCOLIGADA    = TITMMOV.CODCOLIGADA   
                      AND TMOV.IDMOV          = TITMMOV.IDMOV   
                      AND FLAN.STATUSLAN      = '0'   
                      AND FLAN.PAGREC         = 1   
                      AND FLAN.DATAVENCIMENTO >= :DATAVENCIMENTO  
                      AND TMOV.CODCOLIGADA    = FLAN.CODCOLIGADA   
                      AND TMOV.IDMOV          = FLAN.IDMOV   
                      AND TMOV.CODCOLIGADA    = :CODCOLIGADA  
                      AND TMOV.CODCOLCFO      = :CODCOLCFO  
                      AND TMOV.CODCFO         IN (:CODCFO\_S)   
                      AND TITMMOV.CODCOLIGADA = TPRD.CODCOLIGADA   
                      AND TITMMOV.IDPRD       = TPRD.IDPRD  
                      /**and**/  
                GROUP BY TPRD.CODIGOPRD, TPRD.NOMEFANTASIA, TITMMOV.CODTIP, FLAN.DATAVENCIMENTO  
**Observação.:**  
A consulta SQL que retorna as informações pode ser personalizada e setada nos Parâmetros Gerais do Sistema. Clique no aqui para maiores informações.
