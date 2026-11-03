---
content_hash: 34c3a7d2c8e07167237d5beac6b49621bd90d3760542fb1f826ee88bc7e35610
fetched_at: '2026-06-29T00:10:35.451480+00:00'
page_id: '528915228'
product: rm
source: tdn-rm
title: 6660462 FISCAL01-10507 DT SPED Fiscal - COD_CTA não está sendo gerada no registro
  D500
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=528915228
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | SPED Fiscal |
| Ticket: | 6660462 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-10507 |

## **02. SITUAÇÃO/REQUISITO**

A questão levantada pelo cliente é que nas operações de entrada não é gerado o Registro D510. Logo, ele precisa que essa informação saia no D500. Vamos seguir com a sugestão dada pelo Rafael de pegar o Código da Conta disponível na Natureza, entretanto, gerando apenas quando o lançamento for de entrada. pegando a conta de Débito.

## **03. SOLUÇÃO**

Alteração na geração do SPED registro D500, para os Lançamentos de Entrada, onde passará a gerar o Código da Conta Contábil existente na Natureza, pegando a Conta de Débito.
