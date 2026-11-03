---
article_id: 20881403131927
category: Gestão de Transportes (TMS)
content_hash: dbae1c4fcd030231b1700b8f68c4b87c180848dfd4220bc596cb7ac890b5420f
fetched_at: '2026-06-28T22:45:27.260226+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Arredondar ou truncar os valores calculados
  e de impostos
type: support-article
updated_at: '2024-08-27T13:36:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20881403131927-Log%C3%ADstica-Linha-Protheus-TMS-Arredondar-ou-truncar-os-valores-calculados-e-de-impostos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20881403125399) Tempo aproximado para leitura: **00:00:50 min** **Dúvida**Como arredondar ou truncar os valores de impostos no **Protheus**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Para **arredondar** os valores de impostos calculados para documentos de saídas pelo **Protheus**, devemos utilizar o parâmetro **MV\_ARREFAT** **= N** em conjunto com os parâmetros **MV\_RND**\*\* **= F**, onde **\*\*** estão descritos no artigo em **Saiba mais.**E, em **Atualizações/Comercial/ Componentes Frete - TMSA030,** os componentes de fretes devem estar configurados com o campo **Fração - DT3\_FRACAO** da seguinte forma:  
  
**1 - Percentual,** irá manter o valor calculado (exemplo: 120,22); **2 - Inteiro,** irá realizar o arredondamento (exemplo: 120,00).  
  
Para **truncar** os valores de impostos calculados para documentos de saídas pelo **Protheus**, devemos utilizar o parâmetro **MV\_ARREFAT** = **S** em conjunto com os parâmetros **MV\_RND**\*\* = **T**, onde **\*\*** estão descritos no artigo em **Saiba mais**.  
  
**Saiba mais**Para mais informações acesse: [CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Arredondamento de Impostos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023920652-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Arredondamento-de-Impostos)
