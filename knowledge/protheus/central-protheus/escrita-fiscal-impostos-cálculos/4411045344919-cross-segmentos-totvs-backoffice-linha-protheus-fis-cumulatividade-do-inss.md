---
article_id: 4411045344919
category: Escrita Fiscal - Impostos - Cálculos
content_hash: 71e06615e5b5c5118e6245888a7f46efa6dffbbf8c05ee9c85028b973c9cff09
fetched_at: '2026-06-28T22:39:30.571639+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Cumulatividade do
  INSS
type: support-article
updated_at: '2021-10-19T18:19:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411045344919-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Cumulatividade-do-INSS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como ocorre a cumulatividade do INSS?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**

Com a configuração:

**MV\_INSACPJ** = 1  (Com acúmulo)  
**MV\_VLRETIN** = 29.00

O sistema irá se comportar da seguinte maneira:

![](https://tdn.totvs.com/download/attachments/51253274/image2013-6-10%2012%3A26%3A3.png?version=1&modificationDate=1370878047000&api=v2)

\*Após a geração do título de retenção do INSS o Sistema reinicia o Processo de Cumulatividade, porém o INSS só será gerado se o total das notas incluídas ultrapassa o valor do parâmetro MV\_VLRETIN.

O acúmulo é feito MENSALMENTE, respeitando a configuração do parâmetro **MV\_ACMINSS** (vencimento/emissão).
