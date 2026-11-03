---
article_id: 4404193483159
category: Financeiro - Contas a Receber
content_hash: 70f9f29ae807502a6e8710fcaa79deda5523e8fa13c2783e4bcdbe584d214745
fetched_at: '2026-06-28T22:38:12.734699+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - CTBAFIN - A contabilização
  na carteira a Receber é feita pelo campo E1_EMISSAO ou E1_EMIS1?
type: support-article
updated_at: '2021-07-16T14:46:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404193483159-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-CTBAFIN-A-contabiliza%C3%A7%C3%A3o-na-carteira-a-Receber-%C3%A9-feita-pelo-campo-E1-EMISSAO-ou-E1-EMIS1
---

**Ocorrência**A contabilização na carteira a Receber é feita pelo campo E1\_EMISSAO ou E1\_EMIS1?**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - CTBAFIN - A partir da 12.1.17  
  
**Causa**A Contabilização está sendo executada pelo campo E1\_EMISSAO ao invés do campo E1\_EMIS1  
  
**Solução**Na pergunta **Contabiliza Emissões ?** Indica por meio da seleção entre as opções**Pela dt.****emissão****( DT Contab. = E2\_EMIS1 / E1\_EMISSAO)** e **Pela Database (dDataBase)**.

A contabilização de **Contas a Pagar** é feita baseada na data de inclusão do título no sistema. Isto ocorre para que não sejam efetuados lançamentos contábeis em períodos já encerrados.  
Para o **Contas a Receber** é considerada a data de geração do título.  

**Exemplo**24/06/2019

**Saiba Mais**  
<https://tdn.totvs.com/pages/releaseview.action?pageId=497932563>
