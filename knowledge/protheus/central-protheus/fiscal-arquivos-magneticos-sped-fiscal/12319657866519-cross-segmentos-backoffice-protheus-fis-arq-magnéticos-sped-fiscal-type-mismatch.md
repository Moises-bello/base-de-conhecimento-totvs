---
article_id: 12319657866519
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: dffd46d668ce53dbede2ebaa63ffd73952f9cdf009e8af578c4fdfbb704b56df
fetched_at: '2026-06-28T22:42:02.465466+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - type mismatch in array subscriptor - expected N->C on REGC175(SPEDFISCAL.PRW)
type: support-article
updated_at: '2023-02-10T14:40:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12319657866519-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-type-mismatch-in-array-subscriptor-expected-N-C-on-REGC175-SPEDFISCAL-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao gerar o Sped Fiscal ocorre o error log type mismatch in array subscriptor - expected N->C on **REGC175(SPEDFISCAL.PRW)**.  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) -  A partir da versão **12.1.25**  
  
**Causa**O erro ocorre devido ao ambiente não possuir a aplicação do patch de correção abaixo quando houver nota de saída, modelo **55** e informações na tabela **CD9 - Complemento Veículo Automotor** alimentada nos **Complementos Fiscais da nota (MATA926)**

**Solução**

Para solução do erro aplique o pacote de correção abaixo:

12.1.2210:<https://suporte.totvs.com/portal/p/10098/download?e=1095603>; 12.1.27:<https://suporte.totvs.com/portal/p/10098/download?e=1095604>; 12.1.33:<https://suporte.totvs.com/portal/p/10098/download?e=1095605>;
