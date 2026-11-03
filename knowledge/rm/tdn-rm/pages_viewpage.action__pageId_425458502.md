---
content_hash: ba38b63952ae27c5c528e62b2523d9c7beafb718d664761c17e4446408c3549b
fetched_at: '2026-06-29T00:09:30.747635+00:00'
page_id: '425458502'
product: rm
source: tdn-rm
title: Informações Estratégicas - Faturado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458502
version: 1
---

**Informações Estratégicas - Faturado**   
Exibe as informações de todos os itens de todos os contratos faturados para aquele cliente. Mostra o código e a descrição dos produtos para os quais existe um contrato. Possui o campo tipo no qual exibe o tipo do produto. O campo valor exibe o valor do contrato.   
   
   
                SELECT TPRD.CODIGOPRD, TPRD.NOMEFANTASIA NOMEPRODUTO, FLAN.STATUSLAN, FLAN.DATAVENCIMENTO, TITMMOV.CODTIP,   
                       ROUND(SUM(FLAN.VALORORIGINAL \* TITMMOV.PRECOUNITARIO / TMOV.VALORLIQUIDO), 2) VALOR  
                FROM TMOV (NOLOCK), TITMMOV (NOLOCK), FLAN (NOLOCK), TPRD (NOLOCK)  
                WHERE     TMOV.CODCOLIGADA    = TITMMOV.CODCOLIGADA  
                      AND TMOV.IDMOV          = TITMMOV.IDMOV  
                      AND FLAN.STATUSLAN      IN ('0', '1')  
                      AND TMOV.CODCOLIGADA    = FLAN.CODCOLIGADA  
                      AND TMOV.STATUS         <> 'C'  
                      AND TMOV.IDMOV          = FLAN.IDMOV  
                      AND TMOV.CODCOLIGADA    = :CODCOLIGADA  
                      AND TMOV.CODCOLCFO      = :CODCOLCFO  
                      AND TMOV.CODCFO         IN (:CODCFO\_S)  
                      AND TITMMOV.CODCOLIGADA = TPRD.CODCOLIGADA  
                      AND TITMMOV.IDPRD       = TPRD.IDPRD  
                      /**and**/  
                GROUP BY TPRD.CODIGOPRD, TPRD.NOMEFANTASIA, FLAN.STATUSLAN, FLAN.DATAVENCIMENTO, TITMMOV.CODTIP   
Observação.:  
   
A consulta SQL que retorna as informações pode ser personalizada e setada nos Parâmetros Gerais do Sistema. Clique no aqui para maiores informações.
