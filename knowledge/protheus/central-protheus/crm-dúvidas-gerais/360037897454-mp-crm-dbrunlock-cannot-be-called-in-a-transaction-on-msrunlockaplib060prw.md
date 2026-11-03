---
article_id: 360037897454
category: CRM - Dúvidas Gerais
content_hash: 706a68ef72a7f6a2229fe30dc3140e4c22efa6cb7bcaa44bdb46ff7a56d8ac05
fetched_at: '2026-06-28T22:40:27.558296+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: MP-CRM-DBRUnlock cannot be called in a transaction on MSRUNLOCK(APLIB060.PRW)
type: support-article
updated_at: '2021-04-28T14:49:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037897454-MP-CRM-DBRUnlock-cannot-be-called-in-a-transaction-on-MSRUNLOCK-APLIB060-PRW
---

**[Remover as instruções entre colchetes]**  
 **Ocorrência**

Ao criar uma anotação, após dar uma Oportunidade (**CRMA110**) como ganha no CRM, é gerado o erro:

**DBRUnlock cannot be called in a transaction on MSRUNLOCK(APLIB060.PRW) 16/09/2019 15:22:28 line : 1133**

**Ambiente**

 Microsiga Protheus: a partir da release 12.1.17.  
   
 **Causa**

O erro ocorria em razão da chamada da tela de Anotações no meio do Begin Transaction na finalização da proposta.

**Solução**

Para solucionar essa ocorrência, realize os seguintes passos:

1. Efetue o download do **FATN300**, conforme a release de sistema: 12.1.25:<https://suporte.totvs.com/portal/p/10098/download?e=829582> ; 12.1.23:<https://suporte.totvs.com/portal/p/10098/download?e=829581> ; 12.1.17:<https://suporte.totvs.com/portal/p/10098/download?e=829580> ;  
2. Aplique o pacote via TDS ou o antigo IDE, aceitando os fontes mais atualizados;  
3. Posteriormente, inicialize o Smartclient e refaça o processo.

**OBS: O processo informado acima para ser realizado requer um analista com conhecimentos em estrutura de Protheus. Qualquer dúvida no processo, acione a equipe de Framework.**
