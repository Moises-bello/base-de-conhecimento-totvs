---
content_hash: 46163fb2b877223f19b382a923daa3ec3c4de9ecf73a2c4d45772974bc468110
fetched_at: '2026-06-29T00:11:21.241633+00:00'
page_id: '689867717'
product: rm
source: tdn-rm
title: Descontinuar uma Action Anexa (Interno para Desenvolvedores)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=689867717
version: 1
---

**01. VISÃO GERAL**

Se tivermos necessidade de descontinuar uma action anexa devemos ter a ciência que também é preciso realizar a remoção na tabela **GBKDETAILACTION** através de script.

## **02. EXEMPLO**

* Neste exemplo estamos alterando a Action anexa **MovMovimentoAction** já existente pela nova Action **PrjMovimentoAction**, ou seja,estamos descontinuando a primeira e incluindo a segunda.

* Como o anexo **MovMovimentoAction** está sendo descontinuado devemos excluir o seu registro na tabela **GBKDETAILACTION** através de script conforme exemplo abaixo. Para a Action **PrjMovimentoAction** que está sendo incluída nada precisa ser feito.

sqlExemplo de script a ser criado

## **03. INTERVENSÃO VIA SISTEMA**

Caso não seja criado o script para atualização da base pode ser necessário que o cliente faça isso manualmente via sistema. Neste caso o cliente deverá ser instruído para excluir estes dados através do cadastro **Actions Anexas**.
