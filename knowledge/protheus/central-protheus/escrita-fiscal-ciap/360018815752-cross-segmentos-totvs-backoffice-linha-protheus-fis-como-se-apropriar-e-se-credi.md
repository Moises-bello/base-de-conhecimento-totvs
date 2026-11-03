---
article_id: 360018815752
category: Escrita Fiscal - CIAP
content_hash: 308faa94358b2adc44cef7a0d48a61f28cdc1f4a12f035b7836554b2b049c5ba
fetched_at: '2026-06-28T22:39:33.834012+00:00'
product: protheus
section_id: 1500001538561
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como se apropriar
  e se creditar no CIAP somente do ICMS Complementar?
type: support-article
updated_at: '2021-07-29T12:41:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018815752-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-se-apropriar-e-se-creditar-no-CIAP-somente-do-ICMS-Complementar
---

**Dúvida** **Como se apropriar e se creditar no CIAP somente do ICMS Complementar**  
   
 **Ambiente**Protheus - Livros Fiscais - Todas as versões  
   
**Solução:**

Configurar a TES:

Credita ICMS = Sim  
Calcula ICMS = Não  
L. Fiscal ICMS = Outros  
Calc Dif ICM = Sim  
Material de Consumo = Sim  
L. Ciap = Sim

Parâmetros:  
MV\_BICMCMP = F  
MV\_DACIAP = S
