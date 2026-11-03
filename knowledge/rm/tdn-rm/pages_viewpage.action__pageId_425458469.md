---
content_hash: 0199460ac7d1949cab01ea0b5e864a55eaa38bebf8c6df0e1f63b963616a6220
fetched_at: '2026-06-29T00:09:30.696104+00:00'
page_id: '425458469'
product: rm
source: tdn-rm
title: Informações Estratégicas - Mensal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458469
version: 1
---

**Informações Estratégicas - Mensal**   
Apresenta informações sobre itens de contrato que têm vencimentos mensais juntamente com seus valores. É utilizada a data atual para obter o período de mês exatamente anterior ao mês corrente para buscar a faixa de registros. Exibe os campos código, produto, tipo e valor.   
                SELECT DISTINCT TTIP.CODTIP CODTIP, TTIP.DESCRICAO DESCRICAO, FCFO.CODCFO, FCFO.NOMEFANTASIA NOMECLIENTE,                        ROUND(SUM(FLAN.VALORORIGINAL \* TITMMOV.PRECOUNITARIO / TMOV.VALORLIQUIDO), 2) VALOR                 FROM TMOV (NOLOCK), FCFO (NOLOCK), FLAN (NOLOCK), TITMMOV (NOLOCK), TTIP (NOLOCK)                 WHERE     FCFO.CODCOLIGADA = FLAN.CODCOLCFO                       AND FCFO.CODCFO      = FLAN.CODCFO                       AND FCFO.CODCOLIGADA = TMOV.CODCOLCFO                       AND FCFO.CODCFO      = TMOV.CODCFO                       AND FLAN.CODCOLIGADA = TMOV.CODCOLIGADA                       AND FLAN.IDMOV       = TMOV.IDMOV                       AND TMOV.CODCOLIGADA = TITMMOV.CODCOLIGADA                       AND TMOV.IDMOV       = TITMMOV.IDMOV                       AND TMOV.STATUS      <> 'C'                       AND TMOV.CODCOLCFO   = :CODCOLCFO                       AND TMOV.CODCFO      IN (:CODCFO\_S) " +                       AND (DATEPART(MONTH, TMOV.DATAEMISSAO) = :NUMERO\_MES AND DATEPART(YEAR, TMOV.DATAEMISSAO)  = :NUMERO\_ANO)                       AND FLAN.CODCOLIGADA = :CODCOLIGADA                       AND TTIP.CODCOLIGADA = TITMMOV.CODCOLIGADA                       AND TTIP.CODTIP      = TITMMOV.CODTIP                       /**and**/                GROUP BY TTIP.CODTIP, TTIP.DESCRICAO, FCFO.CODCFO, FCFO.NOMEFANTASIA  
**Observação.:**  
A consulta SQL que retorna as informações pode ser personalizada e setada nos Parâmetros Gerais do Sistema. Clique no aqui para maiores informações.
