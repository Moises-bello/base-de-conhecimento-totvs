---
article_id: 15481494166295
category: NFe - Nota Fiscal Eletrônica
content_hash: ba237e820ca82514c89284d55fe1f15ebe7539ab4f5519a87662edce5d30e450
fetched_at: '2026-06-28T22:40:07.120076+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Qual situação tributária
  (CST) de PIS e COFINS
type: support-article
updated_at: '2025-06-17T12:01:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15481494166295-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Qual-situa%C3%A7%C3%A3o-tribut%C3%A1ria-CST-de-PIS-e-COFINS
---

**Dúvida**Qual situação tributária (CST) de PIS e COFINS que destaca o valor do imposto no XML e DANFE ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Para a correção preencher o CST do PIS e do Cofins, campo do PIS Sit. Trib. Pis **"F4\_CSTPIS"** o campo do cofins Sit. Trib. Cof. **"F4\_CSTCOF" .**

Situações tributadas do PIS e do Cofins no XML:

04=Operação Tributável (tributação monofásica (alíquota zero)); 05=Operação Tributável (Substituição Tributária); 06=Operação Tributável (alíquota zero);

Situações não tributadas  do PIS e do Cofins no XML:

07=Operação Isenta da Contribuição; 08=Operação Sem Incidência da Contribuição; 09=Operação com Suspensão da Contribuição;
