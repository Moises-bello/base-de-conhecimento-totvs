---
article_id: 22981374423063
category: Contabilidade Gerencial - Balancetes
content_hash: 990d218feac0296e7f01dbf88be3c5abf3370194ee48bc2b5b10ff3708c498c6
fetched_at: '2026-06-28T22:41:04.125950+00:00'
product: protheus
section_id: 1500001537281
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - (CTBR040 x CTBR400)
  - Balancete Modelo 1  com saldo diferente do Razão Contábil
type: support-article
updated_at: '2025-01-24T18:05:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22981374423063-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBR040-x-CTBR400-Balancete-Modelo-1-com-saldo-diferente-do-Raz%C3%A3o-Cont%C3%A1bil
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22981361416471) Tempo aproximado para leitura: **00:03 min****Ocorrência**Saldo do balancete mod1 esta diferente do saldo do razão contábil  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões]  
  
**Causa**Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.  
  
**Solução**

* Primeiro verificar se a diferença ocorre somente em um mês
* Se for mais de um mês emitir o relatório de meses anteriores até localizar um mês que o saldo esteja igual ao do razão.
* Após localizar o mês que tenha o saldo de acordo com o razão, seja apenas de um mês ou mais meses, execute a rotina de reprocessamento de saldos.
* Na rotina de reprocessamento na pergunta data inicial informar o ultimo dia do mês que esta com o saldo correto.

**Exemplo: agosto com saldo incorreto, porem identificou que julho esta com saldo igual ao do razão**

**Informar a data inicial com 31/07/2024 e data final informar  30 ou 31 do ultimo mês no período que esta com movimentação, para refletir o saldo correto em  todos os meses posteriores ao mês de julho.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22981374366231)

* - Tipo de saldo igual a 1
* - Moedas igual a todas
* - Qual moeda igual a 01
* - Executar o reprocessamento

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22981361430679)

Informações relacionadas

[Diferenças no Balancete ou Razão contábil](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010085772-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBR040-CTBR400-Balancete-Modelo-1-ou-Raz%C3%A3o-Cont%C3%A1bil-com-saldo-incorreto?source=search)
