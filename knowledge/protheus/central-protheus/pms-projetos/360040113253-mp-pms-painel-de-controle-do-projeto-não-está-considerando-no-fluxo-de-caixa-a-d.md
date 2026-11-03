---
article_id: 360040113253
category: PMS - Projetos
content_hash: 05345e0215e76eaeab8bb0d0a8bcaf64de0d490a3a091799bf1cd7e9a0c80f8b
fetched_at: '2026-06-28T22:37:15.062728+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: MP-PMS-Painel de Controle do Projeto não está considerando no fluxo de Caixa
  a data de inclusão to titulo tipo RA
type: support-article
updated_at: '2021-04-29T21:13:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040113253-MP-PMS-Painel-de-Controle-do-Projeto-n%C3%A3o-est%C3%A1-considerando-no-fluxo-de-Caixa-a-data-de-inclus%C3%A3o-to-titulo-tipo-RA
---

**Dúvida**O Painel de Controle do Projeto (**PMSA100**) não está considerando no fluxo de Caixa a data de inclusão to titulo tipo "RA".  
   
 **Ambiente**Microsiga Protheus -  a partir da release 12.1.17.  
  
**Solução**

Ao possuir títulos do tipo **RA** (**Recebimento Antecipado**) ou **PA** (**Pagamento Antecipado**), seus valores não apareciam nos campos **Despesas/Receitas** do dia em que foram incluídos, mas eram apresentados no **Saldo Final** do fluxo de caixa do projeto.

Para solucionar:

1. Efetue o download do pacote de correção, conforme a release de sistema:

12.1.25:<https://suporte.totvs.com/portal/p/10098/download?e=859850> ; 12.1.23:<https://suporte.totvs.com/portal/p/10098/download?e=859849> ; 12.1.17:<https://suporte.totvs.com/portal/p/10098/download?e=859848> ;

2. Aplique o pacote via TDS ou o antigo IDE, aceitando os fontes mais atualizados;

3. Posteriormente, inicialize o Smartclient e refaça o processo.

**OBS: O processo informado acima para ser realizado requer um analista com conhecimentos em estrutura de Protheus. Qualquer dúvida no processo, acione a equipe de Framework.**
