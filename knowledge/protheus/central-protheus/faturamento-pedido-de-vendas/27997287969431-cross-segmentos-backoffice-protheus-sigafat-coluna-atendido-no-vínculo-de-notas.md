---
article_id: 27997287969431
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 34a07879210794bb07b060c35a049c820f58374d93ec2eb1b40907dff9c2caab
fetched_at: '2026-06-28T22:38:39.673200+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Coluna "Atendido" no vínculo
  de notas do pedido de venda
type: support-article
updated_at: '2024-11-22T17:58:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27997287969431-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Coluna-Atendido-no-v%C3%ADnculo-de-notas-do-pedido-de-venda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27997303975703) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Coluna "Atendido" no vínculo de notas do pedido de venda, o que ela indica?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**Exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27997303978007)

Seria que aquela movimentação é a entrada, e, pelo menos alguma parte dela, dessa entrada com poder de/em terceiros específica, já foi ATENDIDO e vinculado em uma saída (devolvida), exemplo a seguir (expanda a imagem para ver os registros da tabela SB6 - Poder De/Em Terceiros):

![](https://p23.zdusercontent.com/attachment/888110/kX2Jn60wEHSQd7R2rGBe6l0Ex?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..EbvewMzzjJcIJEseqMjpig.s2n3CRxtyGmvLLW__X7QYas-SqJmBp-nfOLbOcHx4FDehHOCZwpSrXMtEf8FXpCBTC8QIMm1tz3dpA4QMXFNxOIHQRhmIph98qlK2k2VejTyMAC7u-_9daMvTsos96kgoCwRyVTooMpLBFKS-DyIBLWAPFneFgFKDYXoM4L6XI66fd1EasUUFcBRIC5y7Vy5MQ-Pm8yIs_7q-J7mnQnIG5Rcbd6EV6PH34xjkTUjEaHC9FmCcCiD7oz8mCdN6O7abFUqo5yz5tCGx44EutufjwuBIbeb44N8ZhMIuBeifW8.Sqf9JubEbqVcK5GvGRRoyQ)

A linha superior é a entrada do item com poder terceiros

A linha inferior é a saída do item com poder terceiros (TES de saída = 521)
