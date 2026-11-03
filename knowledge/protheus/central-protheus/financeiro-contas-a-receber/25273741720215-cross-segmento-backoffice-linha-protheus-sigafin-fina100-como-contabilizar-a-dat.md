---
article_id: 25273741720215
category: Financeiro - Contas a Receber
content_hash: 2ee9e002a7726602c364adaeae6373dd1872cdfca62c6333854c3879b28cce9d
fetched_at: '2026-06-28T22:38:12.804278+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA100 - Como contabilizar
  a data de disponibilidade na transferência bancária LP560/561.
type: support-article
updated_at: '2024-07-30T17:03:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25273741720215-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA100-Como-contabilizar-a-data-de-disponibilidade-na-transfer%C3%AAncia-banc%C3%A1ria-LP560-561
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25273741698327) Tempo aproximado para leitura: **00:0:50 min****Dúvida**Como faço para contabilizar a data de disponibilidade quando realizado a transferência bancária?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA713 - Todas as versões.  
  
**Solução**

Na tela de inclusão das transferências bancárias **(FINA100)**, caso seja alterado o campo Data Credito, apenas o lançamento de destino terá o campo Data Disponibilidade **(E5\_DTDISPO)** alterado.

Com isso, o movimento de origem fará a alteração do saldo bancário, e para que a contabilização possa garantir a integridade dos saldos no balanço contábil, as transferências bancárias serão contabilizadas sempre pelo campo **Data Baixa (E5\_DATA)** - independente da configuração do pergunte "Contabiliza baixa ? " **[Data Baixa (E5\_DATA), Data Digitação (E5\_DTDIGIT) ou Data Disponibilidade (E5\_DTDISPO)]**

**SAIBA MAIS:**

**[560/561 Contabilização da transferência bancária](https://tdn.totvs.com/pages/releaseview.action?pageId=569477911)**
