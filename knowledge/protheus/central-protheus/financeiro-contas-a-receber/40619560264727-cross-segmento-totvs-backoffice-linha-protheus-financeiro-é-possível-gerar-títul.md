---
article_id: 40619560264727
category: Financeiro - Contas a Receber
content_hash: 87c0a256010a8a596ed23dd60b6492ecfb40a05a2402f01205ca911dd6e6cc4f
fetched_at: '2026-06-28T22:38:12.543913+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - É possível
  gerar título RA sem movimento bancário?
type: support-article
updated_at: '2026-05-20T19:28:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40619560264727-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Financeiro-%C3%89-poss%C3%ADvel-gerar-t%C3%ADtulo-RA-sem-movimento-banc%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40619588215575) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
É possível gerar um título do tipo RA (Recebimento Antecipado) sem que ocorra a geração de um movimento bancário no momento da sua inclusão?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**  
Não, não é possível gerar um título do tipo RA (Recebimento Antecipado) sem que ocorra a geração de um movimento bancário no momento de sua inclusão.

Por padrão, o RA representa obrigatoriamente um adiantamento financeiro, ou seja, um valor que efetivamente já ingressou na conta da empresa antes da emissão do faturamento.

Por causa desta premissa sistêmica:

* Na Inclusão: quando um RA é criado, o sistema gera automaticamente um movimento bancário correspondente de entrada.
* Na exclusão: Caso um RA seja excluído pela rotina FINA040, o sistema gerará automaticamente um movimento bancário de saída para realizar o estorno do valor recebido, garantindo a consistência do extrato e dos saldos da tabela SE5.
