---
article_id: 360007174512
category: NFe - Nota Fiscal Eletrônica
content_hash: 903431ad9d5c63ed0fc434a30f91b15e255ce8d28f923c6ca5524234fc5b02a7
fetched_at: '2026-06-28T22:39:59.916897+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 898 Rejeição :
  Data de vencimento da parcela não informada ou menor que Data de Autorização'
type: support-article
updated_at: '2021-07-20T20:11:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007174512--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-898-Rejei%C3%A7%C3%A3o-Data-de-vencimento-da-parcela-n%C3%A3o-informada-ou-menor-que-Data-de-Autoriza%C3%A7%C3%A3o
---

**Dúvida**Como corrigir a rejeição abaixo:

Rejeição: 898 Data de vencimento da parcela não informada ou menor que Data de Autorização ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

* **Se gerado grupo de duplicata no XML:**

**Y07 - dup Grupo Parcelas**

O grupo **<dup>** deve ser gerado e a TAG **<dVenc>** deve ter data igual ou maior que a data de autorização da nota.

1 - Altere o parâmetro **MV\_DATDUPL  = .T.**

![20201117_154623.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360099753093/20201117_154623.gif)

2- Após isso, **exclua a nota** e gere novamente.

* **IMPORTANTE:**

Se a Sefaz estiver gerando rejeição com a data de **vencimento igual a data da autorização**, deverá entrar em contato junto a mesma para saber o motivo da rejeição, pois na NT informa que a data não pode ser menor.
