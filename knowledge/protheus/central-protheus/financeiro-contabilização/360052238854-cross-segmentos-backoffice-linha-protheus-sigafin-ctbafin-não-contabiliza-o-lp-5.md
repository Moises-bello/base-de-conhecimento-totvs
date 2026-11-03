---
article_id: 360052238854
category: Financeiro - Contabilização
content_hash: 564281ceb86f803d086cea254face7c60e3aed8bef03c794895e7d79715526ec
fetched_at: '2026-06-28T22:38:05.346537+00:00'
product: protheus
section_id: 1500001550502
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBAFIN - Não contabiliza
  o LP 532
type: support-article
updated_at: '2022-08-17T23:22:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052238854-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBAFIN-N%C3%A3o-contabiliza-o-LP-532
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**Na rotina **CTBAFIN** não contabiliza o **LP 532** para os títulos que foram baixados de forma automática no Contas a Pagar?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**Esse incidente ocorre, quando a baixa do título está com motivo **NORMAL** e não foi digitado e gerado um **cheque** para que ocorra a contabilização  
  
 **Solução**Para solucionar essa ocorrência, configure o parâmetro **MV\_CTBAIXA = A,**para a contabilizar o motivo **NORMAL** sem cheque

**Saiba mais sobre o parâmetro:**[Baixas Pagar Manual - FINA080 - Financeiro - P12](https://tdn.totvs.com/display/public/PROT/Baixas+Pagar+Manual+-+FINA080+-+Financeiro+-+P12)
