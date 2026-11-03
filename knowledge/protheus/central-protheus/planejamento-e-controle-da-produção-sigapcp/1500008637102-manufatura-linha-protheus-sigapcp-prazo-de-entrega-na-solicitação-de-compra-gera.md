---
article_id: 1500008637102
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 7f3e83764dcba67209aea47e61b9736f1eb0f92cf6eb5a86047013f62e182056
fetched_at: '2026-06-28T22:42:45.686494+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Prazo de entrega na solicitação de
  compra gerada
type: support-article
updated_at: '2024-10-15T14:07:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008637102-Manufatura-Linha-Protheus-SIGAPCP-Prazo-de-entrega-na-solicita%C3%A7%C3%A3o-de-compra-gerada
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24100851374103)***Tempo aproximado para leitura: **00:00:40 min**  
**Dúvida**Por que o prazo de entrega do item comprado não é considerado no momento da geração da **SC - Solicitação de Compra**  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Na **SC** temos o campo **C1\_DATPRF - Data prevista da necessidade** que é a data na qual o item deve estar em estoque para atender a demanda da produção, essa data sempre coincide com a data de início prevista da **OP - Ordem de Produção**, e não a data em que o produto deve ser enviado pelo fornecedor.Contudo, no relatório **MATR100 - Relatório de Solicitações de Compras** temos a informação de **Data Limite de Compra**, que vem a ser a **Data prevista da necessidade** menos o **prazo de entrega do item.**
