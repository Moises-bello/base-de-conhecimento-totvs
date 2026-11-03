---
article_id: 34192204101527
category: Financeiro - Conciliador Backoffice
content_hash: 5b6e4074ba20f537b2e067523e30ec4de8960fe4c93f3bedcdd6e5adcc1bf610
fetched_at: '2026-06-28T22:37:47.198686+00:00'
product: protheus
section_id: 30769054561431
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - Exclusão
  de baixa / movimentação bancária aparecendo no conciliador
type: support-article
updated_at: '2025-08-15T10:25:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34192204101527-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-Exclus%C3%A3o-de-baixa-movimenta%C3%A7%C3%A3o-banc%C3%A1ria-aparecendo-no-conciliador
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34192216079127) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Exclusão de baixa ou movimento bancário continua aparecendo no conciliador.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.33  
  
**Solução**  
Neste caso seria um comportamento conceitual, os movimentos excluídos irão aparecer, isso sendo um conceito das tabelas **FKs**, e como a **FK5** que é a tabela principal do processo manual de conciliação. Atualmente existe a opção de filtro de remover estornados na rotina.  
  
De acordo com as regras de negócio e modelagem das tabelas **FK's**, a tabela **FK5** não possui exclusão de movimento, apenas estorno. Por esse motivo os movimentos bancários, mesmo excluídos, serão apresentados.

Saiba mais: [Reestruturação Financeiro - Baixas e Movimento Bancário](https://tdn.totvs.com.br/pages/releaseview.action?pageId=181965434)
