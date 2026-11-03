---
content_hash: da33a13a84acb4a3984ea41866ec4e80a77a9012cfdcba2ee558dfbf2a285b5e
fetched_at: '2026-06-29T00:11:05.320212+00:00'
page_id: '628980023'
product: rm
source: tdn-rm
title: FISCAL01-16088 NT 2020.006 - Meio de Pagamento 99-Outros
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-16088+NT+2020.006+-+Meio+de+Pagamento+99-Outros
version: 7
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | NT 2020.006 - Meio de Pagamento 99-Outros |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-16088 |

## **02. SITUAÇÃO/REQUISITO**

Hoje enviamos o meio de pagamento "99 - Outros" quando o sistema estiver parametrizado para utilizar meio de pagamento e a forma de pagamento informada estiver entre:

* Outros
* Duplicata Mercantil
* Parcelado

## **03. SOLUÇÃO**

De acordo com NF-e NT 2020.006 v1.20

Para meios de pagamento que não possuem referência na tabela da SEFAZ, vamos continuar enviando o código 99 - Outros, e na nova tag de descrição (xPag), enviar a descrição do Meio de Pagamento definido no próprio cadastro.

Disponível a partir da versão 12.1.29
