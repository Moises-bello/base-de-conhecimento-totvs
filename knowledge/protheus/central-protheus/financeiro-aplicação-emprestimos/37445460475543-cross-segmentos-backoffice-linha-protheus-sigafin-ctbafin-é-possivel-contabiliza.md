---
article_id: 37445460475543
category: Financeiro - Aplicação / Emprestimos
content_hash: 473076ef24e9a83f8d8736fb590d3b1d0e8c53bccd6a426e7854519d12ebc205
fetched_at: '2026-06-28T22:37:59.461340+00:00'
product: protheus
section_id: 1500001550542
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBAFIN - É possivel
  contabilizar o LP 582 offline?
type: support-article
updated_at: '2026-01-05T19:56:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37445460475543-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBAFIN-%C3%89-possivel-contabilizar-o-LP-582-offline
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37445463330327) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
É possivel contabilizar as apropriação do LP 582 offline ?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da release 12.1.33  
  
**Solução**  
A rotina CTBAFIN só contabiliza o LP 582 de movimentos que geraram movimento na SE5.  
   
As apropriações mensais efetuadas através das rotinas **FINA716** serão contabilizada na respectiva rotina, ou seja, indisponível na contabilização offline (**CTBAFIN)**, pois estes processos não geram movimentação bancária;

* As operações que geram movimentações bancárias (Resgate de Aplicações ou Pagamento de Empréstimos - serão contabilizadas pela rotina **CTBAFIN**;
  + É importante salientar que o '*flag*' de contabilização destes movimentos, na rotina **CTBAFIN**, é controlado através da tabela **SE5**.  
    Estas movimentações podem gerar valores ref. a diferença no cálculo de apropriação e neste caso serão contabilizados, *LP 582* - Apropriação, também pela rotina **CTBAFIN**, pois estão relacionados à movimentação bancária.

**Importante:**

As apropriações financeiras podem ser realizadas **com ou sem movimentação bancária**.

Quando a apropriação ocorre **sem movimentação bancária**, como nas apropriações mensais realizadas pelas rotinas **FINA716 sem resgate**, não ficando disponível para contabilização offline pela **CTBAFIN**, uma vez que esses processos **não geram registros na tabela SE5**.

Por outro lado, quando há **movimentação bancária**, como nos casos de **resgate de aplicações** ou **pagamento de empréstimos**, ocorre automaticamente uma apropriação financeira vinculada a essa movimentação no momento do resgate. Nesses casos, a contabilização poderá ser realizada pela rotina **CTBAFIN - Contabilização offline**, incluindo o **LP 582 – Apropriação**, pois tais operações geram movimentação na **SE5**.

É importante destacar que:

* A rotina **CTBAFIN** somente contabiliza o **LP 582** para resgate de aplicações onde automaticamente geram apropriações;

**Saiba mais:** [Aplicações e Empréstimos - Financeiro P12](https://tdn.totvs.com/pages/releaseview.action?pageId=392500138)
