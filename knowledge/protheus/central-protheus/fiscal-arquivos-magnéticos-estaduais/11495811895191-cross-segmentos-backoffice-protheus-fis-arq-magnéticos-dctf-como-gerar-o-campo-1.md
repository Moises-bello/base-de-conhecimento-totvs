---
article_id: 11495811895191
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: dce4b9f6dceae53c0cb36013298fb8184bb268be9ec9568091c2c22c2a05dc78
fetched_at: '2026-06-28T22:42:09.165149+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - DCTF - Como
  gerar o campo 19 - SCP  do R10? '
type: support-article
updated_at: '2023-01-09T12:16:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11495811895191-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-DCTF-Como-gerar-o-campo-19-SCP-do-R10
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) empo aproximado para leitura: **00:02:00 min** **Dúvida**Como gerar o campo 19 - SCP = 1 para o registro  R10?   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**Para que o **campo 19 do registro R10** seja gerado como 1, é preciso informar o código de receita, variação e periodicidade no **parâmetro MV\_SCP000**, conforme exemplo abaixo:   
  
**MV\_SCP000 -> 810908M;**

![](https://totvssuporte.zendesk.com/attachments/token/R2QVTxDdlvy3TocnUCrvNReLM/?name=image.png)  
  
Preenchendo dessa forma, o campo é gerado corretamente como 1, conforme exemplo didático abaixo:  
  
![](https://totvssuporte.zendesk.com/attachments/token/TgqWL7AVeKLJRLkhfVJqxEywq/?name=image.png)
