---
article_id: 360036648814
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 20d01cb73beeb3bcbcf5365dae03d082741221a01dd8f3bc68ea0f02212b938f
fetched_at: '2026-06-28T22:38:31.294864+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: 'MP-FAT-MV_FTRESBL '
type: support-article
updated_at: '2021-04-28T15:54:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036648814-MP-FAT-MV-FTRESBL
---

**Dúvida**

Qual a utilização do parâmetro **MV\_FTRESBL**?  
   
 **Ambiente**

Microsiga Protheus -  a partir da versão 12.

**Solução**

O parâmetro **MV\_FTRESBL** é utilizado na função de nova liberação da rotina de Liberação de Estoques (**MATA455**), sua finalidade é determinar se haverá avaliação crédito  sobre  a quantidade restante do itens na execução da Nova Liberação. 

Abaixo os dados técnicos do parâmetro:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047962554/mceclip0.png)

**Obs**: O parâmetro trabalhará em conjunto com os parâmetros de avaliação de crédito e estoque: **MV\_BLOQUEI, MV\_BLQCRED, MV\_GRVBLQ2, MV\_SELLOTE, MV\_SELPLOTE** e **MV\_RISCOB**.

**SAIBA MAIS: [TSNZAE\_DT\_Parâmetro\_MV\_FTRESBL\_(nova\_liberação)](https://tdn.totvs.com/pages/viewpage.action?pageId=189314043)**
