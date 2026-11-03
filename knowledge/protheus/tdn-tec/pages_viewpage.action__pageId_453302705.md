---
content_hash: 62f5bbaca798a00836b71b4749af20c449851145a5816f8c7304495765056d88
fetched_at: '2026-07-02T19:24:23.970640+00:00'
page_id: '453302705'
product: protheus
source: tdn-tec
title: Correção - TPaintPanel causando fechamento do SmartClient
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=453302705
version: 1
---

Correção - TPaintPanel causando fechamento do SmartClient

|  |  |
| --- | --- |
| Situação | Ao utilizar o componente TPaintPanel para adicionar um shape do tipo imagem e em seguida invocar o método TPaintPanel:SetImageSize(), o SmartClient travava e fechava repentinamente com a mensagem "SmartClient parou de funcionar" |
| Ocorrência | Ocorria uma falha no tratamento da imagem do shape. |
| Correção | Foi aplicada uma correção no tratamento do shape de imagem. |
| Informações adicionais | * Referente ao chamado: PP-603 * Referente à ocorrência: ITEC-399 * Disponível em builds iguais ou superiores a 7.00.170117A - 17.3.0.5\_RC5 |
