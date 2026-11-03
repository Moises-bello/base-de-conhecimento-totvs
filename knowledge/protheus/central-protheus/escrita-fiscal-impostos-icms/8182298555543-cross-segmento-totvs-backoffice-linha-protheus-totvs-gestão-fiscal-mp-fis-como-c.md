---
article_id: 8182298555543
category: Escrita Fiscal - Impostos - ICMS
content_hash: afc6caff8ec27460d78e3a0bf9d859e421095047ee7ddf4689b1647344021b4c
fetched_at: '2026-06-28T22:39:24.093867+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal- MP
  FIS Como calcular Diferencial de alíquotas com base dupla de CTE?
type: support-article
updated_at: '2022-08-15T16:50:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8182298555543-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-TOTVS-Gest%C3%A3o-Fiscal-MP-FIS-Como-calcular-Diferencial-de-al%C3%ADquotas-com-base-dupla-de-CTE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:02:00 min **Dúvida**MP FIS Como calcular Diferencial de aliquotas com base dupla de CTE?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**O parametro MV\_BASDENT somente para espécie 55  
 

Em alguns estados nas prestações de serviços de transporte tomadas por consumidor final contribuinte do ICMS, se aplica a forma de cálculo definido na orientação tributária DOLT/SUTRI nº 002/2016. Para estes casos foi criado o parâmetro MV\_BASDPUF que permitirá informar a UF que realiza o cálculo de base simples para documentos de conhecimento de frete (CTR/CTE/CTA/CA/CTF/NFST) ou para documentos de comunicações e telecomunicações (NTST/NTSC), referente à aquisição de serviços de transportes, comunicações ou telecomunicações.

| **Itens/Pastas** | **Descrição** |
| --- | --- |
| **Nome** | MV\_BASDPUF |
| **Tipo** | Caracter |
| **Descrição** | Define UFs que terão cálculo da base do destino em operações de Difal em aquisição de transporte, comunicação e telecomunicação. |
