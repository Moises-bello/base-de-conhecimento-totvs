---
content_hash: 19c5bba5986a2e97ec512a35ab285a8d6417b153b8852ae68f573cfb740d272b
fetched_at: '2026-06-29T00:09:03.541123+00:00'
page_id: '381048434'
product: rm
source: tdn-rm
title: 3551573 FOPCALCULO01-4154 SEFIP - Base de FGTS de Afastados
type: documentation
url: https://tdn.totvs.com/display/LRM/3551573+FOPCALCULO01-4154+SEFIP+-+Base+de+FGTS+de+Afastados
version: 1
---

# SEFIP

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | SEFIP |
| **Situação/Requisito:** | Quando o funcionário está afastado por Acidente de Trabalho e está vinculado ao Tomador Administrativo, ao realizar a Distribuição da SEFIP, o evento de código de cálculo 315 - Base de FGTS de Afastados não é apresentado na Distribuição. Esta situação só ocorre quando é informado no histórico de afastamento do funcionário o tomador administrativo no campo "Código do Tomador". |
| **Solução/Implementação:** | No TOTVS Folha de Pagamento foi identificado que o evento de código de cálculo 315 não é apresentado na Distribuição da SEFIP. Foi identificado que a situação só ocorre quando o "Código do Tomador" está preenchido no histórico de afastamento do funcionário. Foi feito o ajuste na Distribuição da SEFIP para que considere corretamente o código de cálculo 315. |
| **Tickets relacionados:** | 3551573. |
