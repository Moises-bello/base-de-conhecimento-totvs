---
content_hash: cd25055f45ae5df643881c29e8e9e4ef72144feeb3e92ae8880aecdee9339a67
fetched_at: '2026-06-29T00:09:30.685962+00:00'
page_id: '425458464'
product: rm
source: tdn-rm
title: Informações Estratégicas - Produtos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458464
version: 1
---

**Informações Estratégicas - Produtos**   
Exibe todos os produtos adquiridos pelo cliente (ou grupo de clientes) e a situação dos mesmos.   
A consulta SQL interna ao sistema faz uso das tabelas de Cliente, Item de contrato, Status do contrato e Produto e então realiza um filtro dos produtos do cliente através da tabela de Itens do contrato. Utiliza as demais tabelas para buscar descrições de alguns campos apresentados. O SQL fixo dentro do código que retorna a lista de produtos do cliente/grupo de cliente é:  
SELECT TPRD.CODIGOPRD, TPRD.NOMEFANTASIA NOMEPRODUTO, TITMCNT.QUANTIDADE, TITMCNT.NSEQITMCNT,  
                  TITMCNT.NUMEROSERIE, TITMCNT.DATAINICIO, TSTACNT.DESCRICAO POSICAO,   
                       TITMCNT.DATACANCEL, TITMCNT.CODCFO, FCFO.NOMEFANTASIA NOMECLIENTE  
                FROM TITMCNT (NOLOCK), FCFO (NOLOCK), TPRD (NOLOCK), TSTACNT (NOLOCK)  
                WHERE     TITMCNT.CODCOLCFO   = FCFO.CODCOLIGADA  
                      AND TITMCNT.CODCFO      = FCFO.CODCFO  
                      AND TITMCNT.CODCOLIGADA = TPRD.CODCOLIGADA  
                      AND TITMCNT.IDPRD       = TPRD.IDPRD  
                      AND TITMCNT.CODCOLIGADA = TSTACNT.CODCOLIGADA  
                      AND TITMCNT.CODSTACNT   = TSTACNT.CODSTACNT  
                      AND TITMCNT.CODCOLIGADA = :CODCOLIGADA  
                      AND TITMCNT.CODCFO      IN (:CODCFO\_S)  
Observação.:  
A consulta SQL que retorna as informações pode ser personalizada e setada nos Parâmetros Gerais do Sistema. Clique no aqui para maiores informações.
