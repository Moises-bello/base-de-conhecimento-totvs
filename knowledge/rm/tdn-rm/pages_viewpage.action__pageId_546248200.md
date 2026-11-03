---
content_hash: d0ed0fdaf102d5bc6a0894bc8a688cc9c4d5d9660f88b1a49a1cdb625a958a01
fetched_at: '2026-06-29T00:10:39.214201+00:00'
page_id: '546248200'
product: rm
source: tdn-rm
title: 8279209 FISCAL01-12475 DT Serviço de tributação ICMS ST com ICMS Desonerado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=546248200
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Serviço de Tributação |
| Ticket: | 8279209 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-12475 |

## **02. SITUAÇÃO/REQUISITO**

Cliente relatou que em operações de vendas relacionadas a SUFRAMA o sistema deve levar a alíquota do ICMS para o movimento, mesmo que nas regras fiscais do ICMS este esteja marcado como ICMS Desonerado, para que seja calculado o ICMSST***.***

## **03. SOLUÇÃO**

Ajuste no serviço de Tributação do Movimento: Implementação para carregar a alíquota do tributo ICMS no Item do Movimento quando a Natureza for do Tipo Substituição Tributária com ICMS Desonerado.
