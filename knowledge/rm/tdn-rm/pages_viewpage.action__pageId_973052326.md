---
content_hash: 9e63536b45a31c212bafe71b3c4eb0126aa10cb355dbb1ff3f2cc6d614f623ff
fetched_at: '2026-06-29T00:12:15.228998+00:00'
page_id: '973052326'
product: rm
source: tdn-rm
title: FISCAL01-26305 - NT_2025.001- Dados Cobrança
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=973052326
version: 1
---

## **01. DADOS GERAIS**

| Produto: | TOTVS |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | BackOffice |
| Módulo: | Gestão de Estoque, Compras e Faturamento |
| Função: | Envio NF-e / NFC-e |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-26305 |

## **02. SITUAÇÃO/REQUISITO**

A nota técnica 2025.001 inclui uma nova regra para os dados de cobrança que pede que o grupo de parcelas (tag:”dup”) não seja gerado para casos de pagamentos à vista (indPag=0).

## **03. SOLUÇÃO**

O grupo de parcelas (tag:”dup”) não é mais gerado quando o movimento usar uma forma de pagamento à vista.

Disponível a partir da biblioteca 12.1.2410
