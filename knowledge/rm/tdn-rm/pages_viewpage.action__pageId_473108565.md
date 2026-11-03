---
content_hash: ab32bfddef9262a13b6a44058a87ade15a99a612c985afea142f8e47f5bde0b1
fetched_at: '2026-06-29T00:10:16.603266+00:00'
page_id: '473108565'
product: rm
source: tdn-rm
title: DEDUANALYTICS-1238 DT - Extração dimensão Histórico Contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=473108565
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | TOTVS Educacional |
| Módulo: | Fast Analytics |
| Função: | Extração de dimensão |
| Ticket: | N/A |
| Requisito/Story/Issue (informe o requisito relacionado) : | DEDUANALYTICS-1238 |

## **02. SITUAÇÃO/REQUISITO**

Como é obrigatório a marcação de pelo menos um item na variável Histórico Contábil existente no Gooddata, com isso, a aplicação de forma restritiva dessa variável sob as métricas contábeis faz com que os relatórios contábeis não retorne nenhuma informação caso o cliente não precise de utilizar o histórico para definir os valores de fechamento contábil.

## **03. SOLUÇÃO**

Foi modificado a consulta de extração para retornar um valor que será o default na variável de histórico contábil. Como esse valor não estará relacionado aos valores da fato de contabilidade, não haverá efeito colateral para os clientes que não precisam configurar os históricos relacionados ao fechamento contábil.
