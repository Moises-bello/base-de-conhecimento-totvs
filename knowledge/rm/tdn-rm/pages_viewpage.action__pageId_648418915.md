---
content_hash: 85a644afc65eeb678a8156385ec77127e5a6f1590af0700ba0a658dd72824943
fetched_at: '2026-06-29T00:11:11.727905+00:00'
page_id: '648418915'
product: rm
source: tdn-rm
title: FISCAL01-15907 DT - Colocar campo na tela do Lançamento Fiscal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=648418915
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Lançamento Fiscal |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-15907 |

## **02. SITUAÇÃO/REQUISITO**

Colocar um campo para desconsiderar a RSN na Situação tributária do Lançamento Fiscal

## **03. SOLUÇÃO**

Na tela de Lançamento Fiscal foi incluído um checkbox para desconsiderar a RSN na Situação tributária.

Regras:

Parametrizar para que o campo seja habilitado na situação tributária dos lançamentos fiscais de entrada/saída.

Para isso acesse o parametrizador do Gestão Fiscal:

03.01 - Identificação de Regras de Apuração | Lançamento Fiscal 5/7

A natureza deve ser Avançada ou Completa, e o novo Check deve estar marcado.

Já nos Lançamentos Fiscais vá nas Situações Tributárias.

Ao marcar o campo "Desabilita regra de seleção de natureza" todas as CPFS serão liberadas no lookup
