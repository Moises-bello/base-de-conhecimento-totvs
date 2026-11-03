---
article_id: 23619903146135
category: Financeiro - Contabilização
content_hash: 9e8f8f1f0ef348bc1a055f55033eb672d89c791d9404ce0bf77462589ed7a4ca
fetched_at: '2026-06-28T22:38:05.343678+00:00'
product: protheus
section_id: 1500001550502
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBAFIN - Flag de contabilização
  comportamento
type: support-article
updated_at: '2025-09-04T18:49:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23619903146135-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBAFIN-Flag-de-contabiliza%C3%A7%C3%A3o-comportamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23619903109271) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Mesmo deletando a linha de contabilização do registro, os campos E2\_LA, E1\_LA e ou E5\_LA fica = S com isso o registro não é contabilizado novamente  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da release 12.1.33  
  
**Solução**

**FLAG de Contabilização : Comportamento**

Os **FLAGS** de contabilização são gravados a partir do momento em que o registro passa pela avaliação da regra definida no **lançamento padrão** (**CT5\_VLR01**), seja ela atendida (**retorno .T.**) ou não (**retorno .F.**).

Portanto, uma vez presentes e ativos os **LPs**, o sistema irá efetuar a respectiva marcação do **FLAG** nos registros atrelados independente do valor retornado e da manipulação dos registros na tela de contabilização **(inclusive se as linhas forem deletadas)  
  
Saiba mais:**[Contabilização Offline - CTBAFIN - Financeiro - P12](https://tdn.totvs.com/pages/viewpage.action?pageId=497932563)
