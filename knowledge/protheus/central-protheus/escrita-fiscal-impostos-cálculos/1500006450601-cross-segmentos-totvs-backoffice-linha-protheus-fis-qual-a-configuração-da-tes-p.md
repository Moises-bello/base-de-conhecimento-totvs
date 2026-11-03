---
article_id: 1500006450601
category: Escrita Fiscal - Impostos - Cálculos
content_hash: f3d6f3b2631d59f842650c452bcbbaabf5487bc37271f6a94ec53a5d31100448
fetched_at: '2026-06-28T22:39:30.626646+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Qual a configuração
  da TES para NF do EIC?
type: support-article
updated_at: '2021-07-29T13:22:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006450601-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Qual-a-configura%C3%A7%C3%A3o-da-TES-para-NF-do-EIC
---

**Dúvida**MP - FIS - QUAL A CONFIGURAÇÃO DA TES PARA NF DO EIC?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

Para as notas fiscais de origem do EIC não podemos calcular nenhum imposto, deve ser configurado da seguinte forma:

|  |  |
| --- | --- |
| Calcula ICMS (F4\_ICM) | não |
| Calcula IPI (F4\_IPI) | não |
| Cod.Fiscal (F4\_CF) | Algum Iniciado por “3” Ex: 3101 |
| L. Fisc. ICMS (F4\_LFICM) | de acordo com a necessidade |
| L.Fisc. IPI (F4\_LFIPI) | de acordo com a necessidade |
| IPI na base (F4\_INCIDE) | sim |
| Agrega Valor (F4\_AGREG) | B ou C |
| PIS/COFINS (F4\_PISCOF) | 4 = não considera |
| Cred. PIS/COF (F4\_PISCRED) | 1 – Credita |
| Agr. Cofins (F4\_AGRCOF) | C – COF+Merc |
| Agr. PIS (F4\_AGRPIS) | P – PIS+ Merc |
| PS/CF Import (F4\_INTBSIC) | 3 - Ambos |
| Calc.Ipi.Frete (F4\_IPIFRET) | N - Não |

ICMS  - Desp. Ac. ICMS (F4\_DESPICM) = sim

IPI - Desp. Ac. IPI (F4\_DESPIPI) = não

PIS - Desp. Ac. PIS (F4\_DESPPIS) = não

COFINS - Desp. Ac. COF (F4\_DESPCOF) = não

F4\_agreg = B -  O valor da mercadoria não contém o valor do ICMS, portanto, o valor do ICMS e da mercadoria será agregado ao total do documento. Este agregador de valor não calcula nenhum imposto,

mantendo-se o que for informado pelo usuário ou transmitido por outro sistema.

F4\_agreg = C - O valor da mercadoria não contém o valor do ICMS, mas somente o valor da mercadoria será agregado ao total do documento. Note que a base de cálculo do ICMS sofrerá a incorporação

do valor do ICMS. Este agregador de valor não calcula nenhum imposto, mantendo-se o que for informado pelo usuário ou transmitido por outro sistema.
