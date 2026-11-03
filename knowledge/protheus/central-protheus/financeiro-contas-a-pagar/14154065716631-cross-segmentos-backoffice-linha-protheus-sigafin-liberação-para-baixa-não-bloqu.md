---
article_id: 14154065716631
category: Financeiro - Contas a Pagar
content_hash: 1fd5ef89e1bb7e1048c2a4a0efe675e397a55885df2334ff366841efd86c07a1
fetched_at: '2026-06-28T22:38:08.449690+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN  - Liberação para baixa
  não bloqueia PA
type: support-article
updated_at: '2023-04-28T12:09:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14154065716631-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Libera%C3%A7%C3%A3o-para-baixa-n%C3%A3o-bloqueia-PA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Rotina de liberação de títulos não bloqueia a baixa do PA?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
 **Solução**Avaliação do parâmetro **MV\_CTLIPAG** é para o pagamento, a inclusão do título tipo: **PA**, é um pagamento no momento da inclusão (diferente de um tipo: **NF** que ainda será gerado um pagamento).  Ao incluir um **PA** (**Pagamento Antecipado**) é movimentado banco sem a liberação, dessa forma o **PA** não tem influência no parâmetro **MV\_CTLIPAG**.  
  
**Saiba mais**[Liberação para Baixa - FINA580 - Financeiro - P12](https://tdn.totvs.com/pages/releaseview.action?pageId=312165854)  
[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA580 - Como utilizar a rotina liberação para baixa](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016596851)
