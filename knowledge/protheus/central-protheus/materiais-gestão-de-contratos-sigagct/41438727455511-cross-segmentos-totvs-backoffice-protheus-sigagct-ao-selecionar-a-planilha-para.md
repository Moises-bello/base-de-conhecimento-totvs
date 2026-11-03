---
article_id: 41438727455511
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 739065b0346760ed0d2f425992d04e07dbe735e4ee344aedef14668cd92e6a61
fetched_at: '2026-06-28T22:37:21.375164+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Ao selecionar a planilha
  para Medição ocorre Help CTA_BLOQ informando que "esta entidade está bloqueada"
type: support-article
updated_at: '2026-06-23T20:33:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41438727455511-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Ao-selecionar-a-planilha-para-Medi%C3%A7%C3%A3o-ocorre-Help-CTA-BLOQ-informando-que-esta-entidade-est%C3%A1-bloqueada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41438719075863) Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**

Na rotina de Medição, ao selecionar a planilha ocorre o Help CTA\_BLOQ informando que "Existe Inconsistência no Item" e que "esta entidade está bloqueada"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41438727433623)

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões

**Solução**

A mensagem está relacionada a no ambiente em questão, no cadastro do contrato que se está tentando medir, haver uma Entidade Contábil (Centro de Custo, Conta Contábil, Classe de Valor ou Item Contábil) que está bloqueado em seu cadastro no módulo SIGACTB.

Por padrão, ao selecionar a planilha para a medição, são "gatilhadas" as informações dos itens da planilha do contrato (tabela CNB) para o item da planilha da medição (tabela CNE), sendo que caso haja entidade bloqueada no seu cadastro no módulo de Contabilizada, a rotina não permite a inclusão dessa entidade no campo da medição, ocorrendo assim o help.

A rotina não possui a funcionalidade de trazer as informações bloqueadas do contrato para a planilha para que posteriormente estas sejam alteradas na rotina de medição.

Para a solução, a alternativa é a realização de uma revisão do contrato para se alterar a(s) entidade(s) contábil(eis) bloqueada(s) para outras que não estejam bloqueadas conforme as orientações do artigo abaixo

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como realizar uma Revisão Contábil em contratos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028517152-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-realizar-uma-Revis%C3%A3o-Cont%C3%A1bil-em-contratos)

e assim possam ser trazidas do contrato para a planilha sem a ocorrência do help impeditivo.

***Saiba Mais:***

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
