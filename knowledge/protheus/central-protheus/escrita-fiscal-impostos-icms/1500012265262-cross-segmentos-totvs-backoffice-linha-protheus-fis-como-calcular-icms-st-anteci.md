---
article_id: 1500012265262
category: Escrita Fiscal - Impostos - ICMS
content_hash: 4ff2381cfe51d64d214f4dce121b5cfd90b2db65d908cc77b2d794242a67a6d5
fetched_at: '2026-06-28T22:39:24.155050+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: 'CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como calcular ICMS
  ST antecipado com base dupla ? '
type: support-article
updated_at: '2021-08-17T12:56:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012265262-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-calcular-ICMS-ST-antecipado-com-base-dupla
---

**Dúvida**Como calcular ICMS ST antecipado com base dupla ?   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

Como calcular o ICMS antecipado com base dupla.

Exemplo para calculo estado de MG

MV\_estado = MG

MV\_basdant = .T.

MV\_basdent = MG/SP

MV\_UFBDST = MG

Fornecedor = MG

Cadastro de produtos

Solid entradas = 0,01

TES  
Calcula icms = sim  
Calcula ipi = sim  
IPI na base = não  
L fiscal icms = diferente de não  
L fiscal ipi = outros  
MKP icm comp = não  
marg solid = nunca  
F4\_anticms = sim  
Calc. Dif. ICMS (F4\_COMPL) = N - Não

Mat.consumo = SIM

Valor da mercadoria = 1000,00

Valor do icms = 120,00

Calculo do icms antecipado = 1000,00-120,00 = 880,00

880,00/0,82 = 1.073,17

1073,17 \* 18 % = 193,17

193,17-120,00 = 73,17

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019447462/mceclip0.png)
