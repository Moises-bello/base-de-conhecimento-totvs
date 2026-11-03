---
content_hash: ef82d03469c344aedf6e148e0f5a8833bbeb6420ffeebcec753d113cd04126c7
fetched_at: '2026-06-29T00:10:31.120457+00:00'
page_id: '520670129'
product: rm
source: tdn-rm
title: FISCAL01-11410 - DT REGISTRO C191
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-11410+-+DT+REGISTRO+C191
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | SPED Fiscal |
| Ticket: | FISCAL01-11410 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11410 |

## **02. SITUAÇÃO/REQUISITO**

Incluir na geração do Registro C191 o Modelo 65, com a consistência para gerar a partir de 2020.

## **03. SOLUÇÃO**

Foi implementado uma validação na geração do Sped Fiscal para que na criação do registro C190 seja possível  
também criar o registro C191 em casos que o Código do modelo de documento fosse igual a 65 e que o ano de  
sua geração fosse maior ou igual a 2020
