---
article_id: 360024864154
category: NFe - Nota Fiscal Eletrônica
content_hash: 5d8feec67dc70d7288ace52f325cb5290f870f45f2c397f38b150fd36d636562
fetched_at: '2026-06-28T22:40:05.247169+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 696 Rejeição :
  Operação com não contribuinte deve indicar operação com consumidor final'
type: support-article
updated_at: '2025-06-18T14:32:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024864154-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-696-Rejei%C3%A7%C3%A3o-Opera%C3%A7%C3%A3o-com-n%C3%A3o-contribuinte-deve-indicar-opera%C3%A7%C3%A3o-com-consumidor-final
---

**Dúvida**Como solucionar a rejeição 696 Rejeição : Operação com não contribuinte deve indicar operação com consumidor final  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**

* **Para nota de saída** (ou que utiliza cadastro de cliente)**:**

Se nota de saída <tpNF>**1**</tpNF> **( nota de saída)**ou <tpNF>**0**</tpNF>**(se nota de devolução com cliente ou utiliza cadastro de cliente)** informar no cadastro de cliente A1\_TIPO = F (consumidor final).

![](https://centraldeatendimento.totvs.com/hc/pt-br/article_attachments/13406912382487/287d7f00a65b25d8f15b28ef8757e7d2136ec7ddc29f1c8d7103d7f6c359f248.png)

* **Para nota de entrada** (ou que utiliza cadastro de fornecedor)**:**

Se nota <tpNF>**0**</tpNF> **(nota de entrada)** ou <tpNF>**1**</tpNF> **(se nota de devolução com fornecedor ou utiliza cadastro de fornecedor)**, indIEDest=9 **(não contribuinte)** e não for operação do exterior, ou seja idDest<>3 (diferente de 3) será tratado direto no fonte do NFESEFAZ para gerar de forma automático indFinal = 1, sendo assim não há necessidade de configurar no sistema. Para gerar indIEDest=9 (não contribuinte) deve ser preenchido no cadastro de fornecedor A2\_CONTRIB= Não.

* **Validação da Sefaz:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360039191793)
