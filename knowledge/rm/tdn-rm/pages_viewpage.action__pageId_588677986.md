---
content_hash: 550b447ad0e4a5dbefffd768710b6be5d36b5ef06eb5a6387b9da818b57f9ea3
fetched_at: '2026-06-29T00:10:53.832332+00:00'
page_id: '588677986'
product: rm
source: tdn-rm
title: 10385001 FISCAL01-14448 DT SPED Fiscal - G125 não é gerado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=588677986
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Sped Fiscal |
| Ticket: | 10385001 e 9926129 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-14448 e FISCAL01-14315 |

## **02. SITUAÇÃO/REQUISITO**

Ao gerar a rotina SPED Fiscal com notas de entrada de ativo imobilizado não é apresentado os itens com inicio de  
apropriação de crédito no mês em que os bens tiveram a entrada.

## **03. SOLUÇÃO**

Ajuste na Geração do Sped Fiscal - CIAP, Registro G125.  
Ao selecionar os Itens:  
Serão Selecionados registros onde a Data de Aquisição seja Menor que a Data Final do Período de Geração e não mais  
com data Menor que a Data Inicial do Período de Aquisição.  
Concluindo itens com data de Aquisição dentro ou menor do Período de Geração serão incluídos no Arquivo.   
Registro G125.
