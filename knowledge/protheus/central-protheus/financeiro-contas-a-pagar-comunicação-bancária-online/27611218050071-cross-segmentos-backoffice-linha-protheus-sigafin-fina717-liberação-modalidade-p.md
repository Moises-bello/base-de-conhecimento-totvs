---
article_id: 27611218050071
category: Financeiro - Contas a Pagar - Comunicação Bancária Online
content_hash: 9565999ba344117cefc8feb38364e69690438d7011aa54d935b887e2fca1aa20
fetched_at: '2026-06-28T22:37:49.978267+00:00'
product: protheus
section_id: 26656222001687
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA717 - Liberação
  Modalidade PIX via API
type: support-article
updated_at: '2024-11-06T23:43:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27611218050071-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA717-Libera%C3%A7%C3%A3o-Modalidade-PIX-via-API
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27611191385239) Tempo aproximado para leitura: **00:10:00 min****Ocorrência**No módulo Financeiro, ao transmitir títulos usando o modelo **45 - Transferências PIX** e usando a opção de Liberação Automática **EE\_LIBEAUT** = N **(FINA130 - Parâmetros de Bancos)** ocorre a mensagem de erro no Internet Banking

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27611218008087)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.2310  
  
**Causa**Este incidente ocorre, pois para a regra de negócio do Banco do Brasil, onde as requisições usando a modalidade PIX, não podem ser solicitadas com pendência de aprovação

**Solução**Como a modalidade **PIX** não pode ser usada com a opção **"liberationConfig\":false",** conforme instrução do Banco do Brasil. Neste caso a sugestão é não usar o **PIX** nas transações de **Transmissão de Pagamentos**, ou criar uma **Sub-Conta** de **Parâmetros de Bancos** exclusiva para somente o envio do **PIX** com a opção de **Liberação Automática = SIM (EE\_LIBEAUT=S) nos parâmetros de bancos (FINA130)**  
  
**Saiba mais**  
[Contas a pagar (Comunicação bancária online)](https://tdn.totvs.com/pages/releaseview.action?pageId=734394071)
