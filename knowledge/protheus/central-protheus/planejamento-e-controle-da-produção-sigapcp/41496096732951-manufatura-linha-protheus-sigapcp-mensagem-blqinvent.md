---
article_id: 41496096732951
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: b0e3e855804b7acb1216a86a3ab1f733b50e2dc7eeea96fbe351c0abda8448d4
fetched_at: '2026-06-28T22:42:44.439240+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Mensagem BLQINVENT
type: support-article
updated_at: '2026-06-26T17:46:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41496096732951-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-BLQINVENT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41496113200535) Tempo aproximado para leitura: **00:01:10 min**  
  
**Ocorrência**  
Ao tentar realizar um apontamento de produção, apontamento de perda, estorno de apontamento ou estorno de perda é apresentada a mensagem **BLQINVENT**.  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Causa**  
Essa mensagem é apresentada quando um dos produtos que terão seu estoque movimentado com o apontamento que se deseja realizar ou estorno tem o a movimentação de estoque bloqueada para ser inventariado.  
  
**Solução**  
Na mensagem apresentada é indicado o produto e armazém que estão bloqueados para inventário, reavalie esse bloqueio e faça a liberação , se possível, através da rotina **MATA271.**  
  
**Saiba mais**  
Para mais informações sobre o bloqueio , **acesse** [**MATA271 - Bloqueio de produtos para inventário por data informada**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021554891-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA271-Bloqueio-de-produtos-para-invent%C3%A1rio-por-data-informada)**.**  
  
**Glossário**  
**OP** - Ordem de produção  
**BLQINVENT** - O produto está bloqueado para inventário nesta data portanto não pode ser movimentado  
**MATA271** - Bloqueio de inventário
