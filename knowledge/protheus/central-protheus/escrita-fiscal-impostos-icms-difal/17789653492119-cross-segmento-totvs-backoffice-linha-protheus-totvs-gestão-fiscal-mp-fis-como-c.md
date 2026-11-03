---
article_id: 17789653492119
category: Escrita Fiscal - Impostos - ICMS - Difal
content_hash: 83fdfb37217947586a80d27dff4203f9f56df55aa3ab2714d9a1b2ca7c510239
fetched_at: '2026-06-28T22:39:19.230873+00:00'
product: protheus
section_id: 1500001549902
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal -
  MP FIS Como calcular o Diferencial de alíquota base dupla sem descontar o ICMS no
  documento de entrada ?
type: support-article
updated_at: '2023-09-25T12:34:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17789653492119-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-TOTVS-Gest%C3%A3o-Fiscal-MP-FIS-Como-calcular-o-Diferencial-de-al%C3%ADquota-base-dupla-sem-descontar-o-ICMS-no-documento-de-entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17789668263191) Tempo aproximado para leitura: **HH:05:00 min** **Dúvida**MP FIS Como calcular o Diferencial de aliquotas base dupla sem descontar o ICMS no documento de entrada ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**Exemplo de calculo:

Valor da mercadoria = 1000,00  
Base de calculo do ICMS = 1000,00 \*12% = 120,00  
Diferencial de aliquotas = 1000,00 /0,82 = 1219,51   
1219,51 \*18% = 219,51-120,000 = 99,51

MV\_ESTADO  = GO

MV\_BASDENT = GO

MV\_BASDEGO = GO

Fornecedor = BA

TES

Calcula icms = sim

L fiscal icms = outros

CFOP = 2556/2551

Mat consumo = sim

Calc dif icm = sim

Documento de entradas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17789633632279)

O valor do ICMS diferencial de aliquotas será gravado no campo F3\_ICMSCOM

Boletim

<https://tdn.totvs.com/display/public/PROT/TUWAOG_DT_Decreto_RCTE_Art._65_III_do_estado_de_Goias>
