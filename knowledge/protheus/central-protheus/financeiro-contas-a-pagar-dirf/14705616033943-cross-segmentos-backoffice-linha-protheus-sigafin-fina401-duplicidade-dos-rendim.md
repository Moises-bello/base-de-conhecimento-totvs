---
article_id: 14705616033943
category: Financeiro - Contas a Pagar - Dirf
content_hash: b945ec8dc31b7e1c07a0a8d34e6a303bf0ed726cdb0a27554503ee1b8904a526
fetched_at: '2026-06-28T22:38:10.719085+00:00'
product: protheus
section_id: 1500001550482
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA401 - Duplicidade
  dos rendimentos tributários no relatório
type: support-article
updated_at: '2024-01-22T14:57:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14705616033943-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA401-Duplicidade-dos-rendimentos-tribut%C3%A1rios-no-relat%C3%B3rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min****Ocorrência**Ao acessar a rotina FINA401 e gerar as informações para a Dirf, o relatório apresenta duplicidade nos rendimentos tributários, conforme imagem abaixo:  
  
Títulos incluídos para geração da Dirf no valor de 5.000,00 reais cada;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14705370227479)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**Esse incidente ocorre, ao utilizar uma natureza que calcule IR e PCC, e colocando o código de retenção  5952, referente ao PCC no título Pai.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14705424731415)  
  
**Solução**Para o funcionamento correto, como a natureza tem retenção de IR e PCC, deve-se utilizar o código de retenção 1708 - IR no título Pai, pois o sistema colocará automaticamente nos títulos do PCC o código 5952, evitando assim, duplicidade no relatório.

**Saiba Mais**[Informações sobre a DIRF?](https://tdn.totvs.com/pages/releaseview.action?pageId=43549271)
