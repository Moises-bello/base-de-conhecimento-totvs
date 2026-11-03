---
content_hash: 8ca01561712eb39a5e519d0ab58fbbfe963719090825cadef87de6fac0ee8cb4
fetched_at: '2026-06-29T00:09:30.688267+00:00'
page_id: '425458465'
product: rm
source: tdn-rm
title: Informações Estratégicas - Projetos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458465
version: 1
---

**Informações Estratégicas - Projetos**   
Utilizando tabelas do módulo de Projetos, apresenta os projetos existentes para um determinado cliente, o código do projeto e seu status (posição) mais recente.  
                SELECT MPRJ.CODPRJ, MPRJ.DESCRICAO,   
                       (CASE MPRJ.POSICAO  
                           WHEN 1 THEN 'Em andamento'  
                           WHEN 2 THEN 'Paralisado'  
                           WHEN 3 THEN 'Concluído'          
                           WHEN 4 THEN 'A executar'          
                           WHEN 5 THEN 'Em negociação'  
                           WHEN 6 THEN 'Revisao'          
                           WHEN 7 THEN 'Cancelado'                   
                           ELSE 'Não informado'  
                        END) AS STATUS  
                FROM MPRJ (NOLOCK)  
                WHERE     MPRJ.CODCOLIGADA = :CODCOLCFO   
                      AND MPRJ.CODCLIENTE  = :CODCFO  
                      AND MPRJ.TIPOPRJ     <> 1   
                      AND MPRJ.REVISAO = (SELECT MAX(REVISAO) FROM MPRJ P (NOLOCK) WHERE P.CODCOLIGADA = MPRJ.CODCOLIGADA AND P.CODPRJ = MPRJ.CODPRJ)  
                      /**and**/  
**Observação.:**  
A consulta SQL que retorna as informações pode ser personalizada e setada nos Parâmetros Gerais do Sistema. Clique no aqui para maiores informações.
