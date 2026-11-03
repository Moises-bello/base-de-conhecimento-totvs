---
content_hash: 3318ec14d9128c2420da8fb9cf19929aa6a1e24664ab17fbce263de6e619b71e
fetched_at: '2026-06-29T00:11:12.468587+00:00'
page_id: '653567182'
product: rm
source: tdn-rm
title: FISCAL01-17089 - Desconto no Lançamento Fiscal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=653567182
version: 2
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Escrituração |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-17080 |

**02. SITUAÇÃO/REQUISITO**

Ao realizar a Escrituração de um movimento que possui Desconto , o Lançamento Fiscal está somando o valor do Desconto no campo \*Valor Mercadoria.

## **03. SOLUÇÃO**

Ajuste no Calculo do Valor da Mercadoria do Item quando o Parâmetro "Preço Total Editado"  
esta marcado, Neste caso o processo de Escrituração vai atribuir o valor do campo "Preço Total" para o mesmo.

Este valor e considerado no Calculo da Base do Diferencial de Alíquota.

obs.: Para que o Valor do Frete componha a Base do Diferencial de Alíquota o Parâmetro Afeta Base ICMS na Natureza  
deve estar marcado (Frete).
