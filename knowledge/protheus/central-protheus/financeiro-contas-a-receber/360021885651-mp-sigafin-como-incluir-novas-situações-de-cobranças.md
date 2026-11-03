---
article_id: 360021885651
category: Financeiro - Contas a Receber
content_hash: 1a55953e021dc9ada43d9dc4908fa7872900d1fd2db85835807223f15975d638
fetched_at: '2026-06-28T22:38:14.261675+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: MP - SIGAFIN - Como incluir novas situações de cobranças
type: support-article
updated_at: '2021-04-28T15:17:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021885651-MP-SIGAFIN-Como-incluir-novas-situa%C3%A7%C3%B5es-de-cobran%C3%A7as
---

**Dúvida**No módulo **Financeiro** em **Contas a receber**, **transferências**, já temos algumas situações de cobrança configuradas. É possível incluir novas?  
   
 **Ambiente**Microsiga Protheus – Financeiro – A partir da versão 12.1.06

**Solução**Sim, para incluir novas situações de cobranças, realize os seguintes passos:  
 1. Acesse a rotina Situação de Cobrança (FINA022);2. Clique em incluir, preencha os campos solicitados e confirme;  
3. A nova situação de cobrança será gravada na tabela FRV e será exibida na rotina de transferências(FINA060) para utilização.

**Importante**Ao preencher o campo **Bloqueio Mov.** (FRV\_BLQMOV) com a opção 1-Sim, será habilitada a opção processos de bloqueio para que determine qual processo o usuário não poderá mais realizar caso o título esteja nessa situação de cobrança.  
**Exemplo:** Processo 003 - Baixa Manual. Neste caso, enquanto o título estiver nessa situação de cobrança, não será possível realizar uma baixa manual, sendo exibido o help **F023BLQMOV.**
