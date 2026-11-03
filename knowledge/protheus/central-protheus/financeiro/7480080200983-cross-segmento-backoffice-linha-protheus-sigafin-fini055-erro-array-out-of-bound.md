---
article_id: 7480080200983
category: Financeiro
content_hash: b26c90828264ee69d183a7466fd1d83463c6e02726e5626aee94f87be6160faa
fetched_at: '2026-06-28T22:38:01.109279+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINI055 - Erro array
  out of bounds [1] of [0]  on INCLUISEV(FINI055.PRW) '
type: support-article
updated_at: '2022-07-18T17:13:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7480080200983-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINI055-Erro-array-out-of-bounds-1-of-0-on-INCLUISEV-FINI055-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**No processo de integração entre os produtos RM x Protheus(Financeiro) ao integrar a mensagem única FINANCING ocorre o Erro array out of bounds [1] of [0] on INCLUISEV(FINI055.PRW) 12/05/2021 16:50:49 line : 1668  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINI055 - A partir da release 12.1.17  
  
**Causa**Esse incidente ocorre, pois a parametrização do sistema está incorreta no parâmetro **MV\_CTBCGER  
  
Solução**Preencha o parâmetro **MV\_CTBCGER** indique uma entidade adicional desejada. O conteúdo do parâmetro pode ser de 05 até 09, mas ao preencher por exemplo com o conteúdo 05, os campos da entidade adicional 05 devem estar criados e o cadastro da entidade adicional deverá estar na CT0.

![](https://totvssuporte.zendesk.com/attachments/token/uLBA27WlTJRrxlc5mLdPfovqR/?name=inline-538510608.png)  
  
**Importante**  
Primeiramente o cliente precisará verificar se possui entidade adicional em seu ambiente, conforme o processo informado na documentação: [Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA020 - Erro ManagerialAccountingEntityPolicy](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7221979681303-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA020-Erro-ManagerialAccountingEntityPolicy)
