---
content_hash: 517fc6f71fcebeb464e000199e787dcf2996958dffeb0a614467316a84616973
fetched_at: '2026-06-29T00:09:30.683840+00:00'
page_id: '425458463'
product: rm
source: tdn-rm
title: Informações Estratégicas - Pago
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458463
version: 1
---

**Informações Estratégicas - Pago**   
Esta subpasta traz as informações sobre os valores quitados para cada item do contrato. Este valor é a última cobrança que foi feita do cliente. Exibe os campos código, produto,tipo e valor.   
                SELECT TPRD.CODIGOPRD, TPRD.NOMEFANTASIA NOMEPRODUTO, TITMMOV.CODTIP,                             ROUND(SUM(FLAN.VALORBAIXADO \* TITMMOV.PRECOUNITARIO / TMOV.VALORLIQUIDO), 2) VALOR                 FROM    TMOV (NOLOCK), TITMMOV (NOLOCK), FLAN (NOLOCK), TPRD (NOLOCK)                 WHERE  TMOV.CODCOLIGADA    = TITMMOV.CODCOLIGADA                         AND TMOV.IDMOV          = TITMMOV.IDMOV                        AND FLAN.STATUSLAN    = '1'                       AND FLAN.PAGREC         = 1                       AND TMOV.CODCOLIGADA    = FLAN.CODCOLIGADA                       AND TMOV.IDMOV          = FLAN.IDMOV                       AND TMOV.CODCOLIGADA    = :CODCOLIGADA                       AND TMOV.CODCOLCFO      = :CODCOLCFO                       AND TMOV.CODCFO         IN (:CODCFO\_S)                       AND TITMMOV.CODCOLIGADA = TPRD.CODCOLIGADA                       AND TITMMOV.IDPRD       = TPRD.IDPRD                       /**and**/                 GROUP BY TPRD.CODIGOPRD, TPRD.NOMEFANTASIA, TITMMOV.CODTIP  
Observação.:  
A consulta SQL que retorna as informações pode ser personalizada e setada nos Parâmetros Gerais do Sistema. Clique no aqui para maiores informações.
