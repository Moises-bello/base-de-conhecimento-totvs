---
article_id: 1500010276541
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 92dacf0055ad967e25222f33496145cf19e848dd6c7c92d242f95e021b3b0521
fetched_at: '2026-06-28T22:42:45.803381+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Quantidade da SC ou OP intermediária
  diferente da necessidade
type: support-article
updated_at: '2023-12-19T17:59:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010276541-Manufatura-Linha-Protheus-SIGAPCP-Quantidade-da-SC-ou-OP-intermedi%C3%A1ria-diferente-da-necessidade
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:40 min**  
**Dúvida**Por que a quantidade da **SC - Solicitação de Compra** ou **OP - Ordem de produção** intermediária é diferente do empenho da **OP** pai ?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Essa situação pode ocorrer quando o item em questão possui lote mínimo, quantidade por embalagem ou lote econômico definidos ou quando o parâmetro **MV\_CONSEST - Considera Estoque na Geração da Ordem de Produção** possui o conteúdo **S** e o Sistema identifica estoque parcial para atender a demanda de acordo com os parâmetros **Considera Armazém Padrão**, **Armazém De** e **Armazém Até** do **MATA650 - Ordens de Produção**.
