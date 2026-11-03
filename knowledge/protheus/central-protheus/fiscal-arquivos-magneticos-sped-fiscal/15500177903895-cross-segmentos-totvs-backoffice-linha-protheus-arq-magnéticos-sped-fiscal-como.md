---
article_id: 15500177903895
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: ee65220449c5eaef74346d3bc61ff57e1530e31a6875471c215bfa7cb174b517
fetched_at: '2026-06-28T22:42:03.682451+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - TOTVS BackOffice Linha Protheus - Arq. Magnéticos - SPED
  FISCAL - Como não apresentar os valores de base de ICMS ST nos registros C100, C170
  e C190 do Sped Fiscal?
type: support-article
updated_at: '2023-06-27T11:46:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15500177903895-Cross-Segmentos-TOTVS-BackOffice-Linha-Protheus-Arq-Magn%C3%A9ticos-SPED-FISCAL-Como-n%C3%A3o-apresentar-os-valores-de-base-de-ICMS-ST-nos-registros-C100-C170-e-C190-do-Sped-Fiscal
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15500193373847) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Como **não** apresentar o valor de base de **ICMS ST** nos registros **C100, C170** e **C190** do Sped Fiscal?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) -  A partir da versão **12.1.25**  
  
**Solução**

Para que os valores de base de cálculo do **ICMS ST** não sejam apresentados no Sped Fiscal, pelo campo **23** do **C100**, **16** do **C170** e campo **08** do **C190** é necessário que o conteúdo do campo **F4\_CREDST** na **TES** (**MATA080**) possua o conteúdo **= 4.**

Imposto calculado na Nota Fiscal:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15588907693847)

Ao gerar o **Sped Fiscal**, os campos sem valores:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15589017113111)
