---
article_id: 4412136004887
category: TAF - REINF
content_hash: 2fff1be7e5fb2f5c8a9ae9b74947b42420c0d0b4eb570debe3e74b2b926a9388
fetched_at: '2026-06-28T22:41:33.430943+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: CROSS Segmentos - Backoffice Linha Protheus - TAF - REINF - Qual a origem do
  campo C1H_PAA no ERP PROTHEUS?
type: support-article
updated_at: '2023-03-30T16:51:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412136004887-CROSS-Segmentos-Backoffice-Linha-Protheus-TAF-REINF-Qual-a-origem-do-campo-C1H-PAA-no-ERP-PROTHEUS
---

**Dúvida**

Qual a origem do campo PAA (C1H\_PAA) no Cadastro de Participante (TAFA053) no ERP PROTHEUS?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TAF - Todas as versões  
  
**Solução**

A origem do campo PAA **(CH1\_PAA)**  é a partir do Complemento Cadastral do Cliente (tabela AI0) campo (AI0\_INDPAA), essa informação é utilizada para o evento R-2050.

O Complemento Cadastral do Cliente está disponível no Cadastro de Clientes (MATA030) em Outras Ações:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412143742743/mceclip0.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412151142807/mceclip1.png)

**Assuntos relacionados:**

[MP - FIS - Preenchimento do Campo Ind Isenção - C30\_INDISE = 1](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025548013-MP-FIS-Preenchimento-do-Campo-Ind-Isen%C3%A7%C3%A3o-C30-INDISE-1?source=search)

**R-2050 - Comercialização da Produção por Produtor Rural PJ/Agroindústria**

<https://tdn.totvs.com/display/public/TAF/EFD-Reinf#EFD-Reinf-R-2055-Aquisi%C3%A7%C3%A3oProdutorRural>
