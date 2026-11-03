---
content_hash: c458cc58212ebcf6499dafe92579ee443ca022146b6225abd583158d3786ee15
fetched_at: '2026-06-29T00:10:53.127536+00:00'
page_id: '577406087'
product: rm
source: tdn-rm
title: FISCAL01-13666 DT Envio de NF-e tag cNF
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-13666+DT+Envio+de+NF-e+tag+cNF
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Envio de NF-e |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-13666 |

## **02. SITUAÇÃO/REQUISITO**

Para segurança da chave da NF-e o campo cNF deverá ser gerado de forma aleatória conforme arquitetura estabelecida pela TOTVS [https://arquitetura.totvs.io/rfcs/RFC000007/#r189-gere-tokens-unicos-usando-uma-fonte-segura-de-aleatoriedade](https://arquitetura.totvs.io/rfcs/RFC000007/#r189-gere-tokens-unicos-usando-uma-fonte-segura-de-aleatoriedade "Seguir link")

## **03. SOLUÇÃO**

No envio da NF-e a tag cNF será gerado com um número aleatório com 8 dígitos.
