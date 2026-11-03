---
article_id: 360020540691
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: a1b284f131b7b191236c0a990d39578f657783de56ebcaab97a9163d948ab172
fetched_at: '2026-06-28T22:40:32.545207+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB CTBA102 - O intervalo
  de datas informadas não poderá ser processado.
type: support-article
updated_at: '2021-11-16T12:19:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020540691-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA102-O-intervalo-de-datas-informadas-n%C3%A3o-poder%C3%A1-ser-processado
---

**Ocorrência**

 Ao Incluir o lançamento o sistema apresenta mensagem abaixo

Verifique o Intervalo de datas ou os calendários no Intervalo

O intervalo de datas informadas não poderá ser processado

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360016381812/mceclip0.png)

**Ambiente**

Protheus  – Contabilidade gerencial  – A partir da versão 11.80  
  
**Causa**

Situação é apresentada pois o campo CT2\_CONVER está preenchido para realizar a conversão para mais de uma moeda , porem o calendário não está amarrada a todas as moedas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360016381832/mceclip1.png)  
  
**Solução**

**1º** É possível editar o campo Crit Conv informando conversão somente para as moeda amarradas  e informar " 5" para não converter

**Ex.:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018764952/mceclip0.png)

**2º** Alteração

* Através do cadastro do lançamento Padrão (CTBA080) campo CT5\_MOEDA informar para quais moedas deverão ser efetuados lançamentos contábeis. Poderá ser preenchido com:

1 - Efetua o lançamento na Moeda  
2 - Não efetua o lançamento.  
Cada “1” ou “2” representa uma moeda em uso pelo sistema.

Ex: Se o campo for preenchido com  
“11211”, somente na moeda 3 não será  
efetuado o lançamento contábil

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360016382312/mceclip4.png)

3º Alteração

* Através do cadastro do plano de contas (CTBA020) verifique o critério de conversão informado na conta

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360016434251/mceclip5.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360016382132/mceclip3.png)

Veja também :

[MP - SIGACTB - Calendário Contábil vs Moeda](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007251451-MP-SIGACTB-Calend%C3%A1rio-Cont%C3%A1bil-vs-Moeda-?source=search&auth_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X2lkIjo4ODgxMTAsInVzZXJfaWQiOjI0NTk2NDIwNDg3LCJ0aWNrZXRfaWQiOjQxNDY2NTAsImNoYW5uZWxfaWQiOjYzLCJ0eXBlIjoiU0VBUkNIIiwiZXhwIjoxNTQyMjA4MDI1fQ.Nw7JOue4TqmlMKhOccvM4qUCG6YZs_RC_uohXgtxVhM)  
[MP - SIGACTB - Lançamentos em outras moedas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007149771-MP-SIGACTB-Lan%C3%A7amentos-em-outras-moedas?source=search)

[MP - SIGACTB - CTBA010 Como abrir período contábil bloqueado/fechado para movimentação?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006722952-MP-SIGACTB-CTBA010-Como-abrir-per%C3%ADodo-cont%C3%A1bil-bloqueado-fechado-para-movimenta%C3%A7%C3%A3o-?source=search)

[MV\_CRITPLN](https://tdn.totvs.com/display/PROT/SIGACTB+-+Diversos+--+24238)

* [CTBA105 - Contabilização Off-Line não valida a linha do lançamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059273293-MP-SIGACTB-CTBA105-Contabiliza%C3%A7%C3%A3o-Off-Line-n%C3%A3o-valida-a-linha-do-lan%C3%A7amento?source=search)
