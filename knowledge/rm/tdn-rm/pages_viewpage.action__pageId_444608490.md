---
content_hash: a00b3ed8691e5c013c3bd8dd9a5f9f41fc1c9040db41412127fd060bae524128
fetched_at: '2026-06-29T00:09:54.318396+00:00'
page_id: '444608490'
product: rm
source: tdn-rm
title: 4285745 FISCAL01-7379 DT - Nota Fiscal do Consumidor Eletrônica - Tag vPag
  não está sendo calculada considerando valor opcional do lançamento financeiro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=444608490
version: 3
---

# Nota Fiscal do Consumidor Eletrônica

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | NFC-e |
| **Situação/Requisito:** | Ao emitir NFC-e gerada através de movimento originado do educacional para aluno com desconto de bolsa, a nota está sendo rejeitada com a mensagem abaixo:  Código do Erro: 869. Descrição do Erro: Rejeição: Valor do troco incorreto.  A bolsa é cadastrada como desconto (campo opcional 8 do lançamento financeiro), porém a tag vPag está sendo incluída com o valor integral sem o desconto da bolsa. Dessa forma, a tag fica com valor superior a tag ocasionando a rejeição. |
| **Solução/Implementação:** | Foi corrigido o serviço do financeiro para que o mesmo possa considerar o desconto no campo opcional. |
