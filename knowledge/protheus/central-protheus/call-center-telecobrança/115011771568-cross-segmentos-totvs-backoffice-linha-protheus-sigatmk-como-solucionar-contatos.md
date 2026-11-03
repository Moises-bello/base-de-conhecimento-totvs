---
article_id: 115011771568
category: Call Center - Telecobrança
content_hash: 0dfe95ed0aa345ea027d93554b938b57c6cdc7cd7164cba4f386e322ddb0342b
fetched_at: '2026-06-28T22:41:28.643390+00:00'
product: protheus
section_id: 1500001548222
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGATMK- Como solucionar
  contatos com atendimentos pendentes no log da lista de cobrança
type: support-article
updated_at: '2022-06-22T17:18:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115011771568-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Como-solucionar-contatos-com-atendimentos-pendentes-no-log-da-lista-de-cobran%C3%A7a
---

**Ocorrência**

No módulo de Call Center (SIGATMK), ao gerar uma Lista de Cobrança (**TMKA062**), alguns contatos aparecem no log como: Contato com atendimentos pendentes.  
  
**Causa**

Isso ocorre pelo fato de existir atendimentos com o campo Status como Pendente no Telemarketing (Tabelas **SUC**) ou como em cobrança no Telecobrança (Tabelas **ACF**).  
  
**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGATMK-A partir da versão 11.8  
  
**Solução**

Para solucionar a ocorrência da mensagem de contatos com atendimentos pendentes, realize os passos a seguir:

1. Acessar o módulo 13 - SIGATMK - Call Center;

2. Acessar a rotina Call Center - **TMKA271**;

3. Nela verifique a existência de atendimentos de Telemarketing ou Telecobranças para os contatos informados no log da Lista de Cobrança.

4. No caso dos atendimentos de Telemarketing, verificar a existência dos atendimentos com o campo Status (UC\_STATUS) igual a 2 - Pendente e mudá-los para outra opção de acordo com a sua necessidade.

5. Já no caso dos atendimentos de Telecobrança, se o campo Status (**ACF\_STATUS**) estiver como 2 - Cobrança, será necessário finalizar esse atendimento ou incluir os novos títulos disponíveis na seleção de títulos (SK1) nesse atendimento já existente.

6. Após efetuar esses procedimentos, ao gerar uma nova lista, a ocorrência dos atendimentos pendentes irá ser solucionada para esses contatos.

**SAIBA MAIS:**

Para demais assuntos e duvidas sobre Call Center, acessar o link abaixo: **[FAQs - Call Center](http://tdn.totvs.com/display/PROT/FAQs+-+Call+Center)**
