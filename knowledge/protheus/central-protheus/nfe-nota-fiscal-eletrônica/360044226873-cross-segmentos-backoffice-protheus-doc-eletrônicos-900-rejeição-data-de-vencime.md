---
article_id: 360044226873
category: NFe - Nota Fiscal Eletrônica
content_hash: 8416c815feea17d56f63429b9600098ac4cd3390b0cd90d8e8882ad4e5625c6e
fetched_at: '2026-06-28T22:40:03.324729+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  900 Rejeição:
  Data de vencimento da parcela não informada ou menor que Data de Emissão'
type: support-article
updated_at: '2025-07-18T18:45:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044226873-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-900-Rejei%C3%A7%C3%A3o-Data-de-vencimento-da-parcela-n%C3%A3o-informada-ou-menor-que-Data-de-Emiss%C3%A3o
---

**Dúvida**

Como corrigir a rejeição 900 : Data de vencimento da parcela não informada ou menor que Data de Emissão ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**

A Data de vencimento da parcela **não pode ser menor** que a data de emissão da nota, ou estar em branco.

1. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /** **Cadastros / Parâmetros** clicar em editar **MV\_DATDUPL = .T. Observação:**o parâmetro  indica se deverá considerar a **data da emissão** quando a **data de vencimento** da parcela for menor que  a data de autorização. 

![20220420_094520.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5568701953687)

2. Para não gerar duplicata no XML.Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /** **Cadastros / Parâmetros** clicar em editar **MV\_GRUPCOB = .F.**  
![20220420_094743.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5568733136535)

3. Após isso, ***gere a nota novamente.***

* ***Exemplo do grupo de Cobrança:***

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33567326839447)
