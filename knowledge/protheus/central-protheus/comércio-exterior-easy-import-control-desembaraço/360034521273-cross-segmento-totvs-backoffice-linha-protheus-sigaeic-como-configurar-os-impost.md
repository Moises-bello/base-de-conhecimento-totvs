---
article_id: 360034521273
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: d8ab9921ce83c2cc704c035074a4024832b192c75c9f70a92a585b46d97816fa
fetched_at: '2026-06-28T22:39:50.004144+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Como configurar
  os impostos que serão gerados na nota Filha?
type: support-article
updated_at: '2022-11-22T15:10:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034521273-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Como-configurar-os-impostos-que-ser%C3%A3o-gerados-na-nota-Filha
---

**Dúvida**Como configurar os impostos que serão gerados na nota Filha?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução**Somente poderá incluir uma Nota Filha, se já existir uma nota mãe gerada para o processo.  
Para indicar quais valores serão considerados na nota Filha, é necessário que o parâmetro **MV\_NFFILHA** esteja com o tipo 0, 1, 2 e 3 sendo:  
  
**Tipo "0"** = Os valores considerados será o valor da mercadoria + (FOB + FRETE + SEGURO + CIF + II):

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10405285952663)  
  
**Tipo "1" =** O Tipo “0” + todas as despesas:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10405250706199)  
  
**Tipo "2" =** Irá considerar apenas o valor FOB:

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10405381064471)  
  
**Tipo "3" =** Onde considera o parâmetro MV\_NFFILHA = 0 + despesas base ICMS.

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10405321995031)
