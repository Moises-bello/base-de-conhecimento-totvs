---
content_hash: 89dd55ad0872b588f026a61e7643ae99699ad3f955ba2b02276d4260d181ed43
fetched_at: '2026-06-29T00:11:17.338348+00:00'
page_id: '679161145'
product: rm
source: tdn-rm
title: 13640631 FISCAL01-17729 - DT - Agrupamento R-2010
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=679161145
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Lançamento Fiscal |
| País: | Brasil |
| Ticket: | [13640631](https://totvssuporte.zendesk.com/agent/tickets/13640631 "View ticket on the Zendesk portal") |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-17749, FISCAL01-17728 |

## **02. SITUAÇÃO/REQUISITO**

Ao integrar este evento a DCTF Web via site da Receita o cliente observou que o valor do INSS está aparecendo somente para um Cliente\Fornecedor. O correto é aparecer o valor do INSS para vários cliente\fornecedor, por conta disto será necessário alterar a forma de agrupar o evento.

## **03. SOLUÇÃO**

**O Evento R-2010 passa a ser agrupado da seguintes formas:**

> Por CNO e CNPJ do Cliente Fornecedor quando o Projeto for Total\Parcial e de Terceiro, ou

> Por CNO e CNPJ da Filial e ou CNPJ do Projeto quando o Projeto for Total\Parcial Próprio, ou

> Por CNPJ do Cliente Fornecedor quando não estiver Projeto associado ao Lançamento Fiscal ou quando Campo Indicador de Prestação de Serviço do Projeto for igual a “Não se Aplica” ou “em branco” ou "Não é obra de construção civil ou não está sujeita a matrícula de obra" ou o CNO estiver vazio.

Informações

Disponível partir da versão 12.1.32
