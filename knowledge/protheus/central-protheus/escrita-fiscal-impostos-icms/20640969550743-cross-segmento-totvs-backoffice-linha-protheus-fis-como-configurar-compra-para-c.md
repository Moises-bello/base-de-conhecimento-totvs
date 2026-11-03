---
article_id: 20640969550743
category: Escrita Fiscal - Impostos - ICMS
content_hash: ebbd3f12426ab718de3c609b1bb06ef9a27eda308f774b221f73b5b06b8bd3be
fetched_at: '2026-06-28T22:39:24.038740+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Como configurar
  compra para consumo com redução de base?
type: support-article
updated_at: '2024-01-17T14:23:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20640969550743-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-compra-para-consumo-com-redu%C3%A7%C3%A3o-de-base
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20640941347863) Tempo aproximado para leitura: 03:00**min** **Dúvida**Como configurar compra para consumo com redução de base?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**

Compra de mercadoria para consumo com redução de base de calculo sem credito do ICMS.

valor da mercadoria = 1000,00

Redução de base = 66,67%

Alíquota do ICMS = 12%

Base de calculo do ICMS = 333,30 \* 12% = 40,00

Base de calculo do Diferencial de alíquota = 1000,00\*18% = 180,00 -40,00 = 140,00

Exemplo

MV\_ESTADO = PR

MV\_BICMCMP = .F.

Fornecedor = MG

TES

Calcula icms = sim

L fiscal icms = outros

Mat consumo = outros

% red icm = 33,33

Calc dif icms = sim

Sit trib icm = 20

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20640941350807)

Ao lançar o documento de entradas o imposto será demonstrado na aba impostos, porém no livro fiscal será demonstrado em outros do ICMS, se precisar fazer a devolução tem o calculo do ICMS.

Documento de entradas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20640969530135)

Livros

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20640941354775)
