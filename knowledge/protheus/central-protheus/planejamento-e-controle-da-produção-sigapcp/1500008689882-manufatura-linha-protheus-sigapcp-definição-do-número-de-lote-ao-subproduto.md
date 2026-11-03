---
article_id: 1500008689882
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: d3600f1179cbb5662774deed6db61b9de43f9ffd9f3f4b1e3013acaf75cfb9a4
fetched_at: '2026-06-28T22:42:42.184759+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Definição do número de lote ao subproduto
type: support-article
updated_at: '2024-06-19T12:14:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008689882-Manufatura-Linha-Protheus-SIGAPCP-Defini%C3%A7%C3%A3o-do-n%C3%BAmero-de-lote-ao-subproduto
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17215175624343)***Tempo aproximado para leitura: **00:00:55 min**  
**Dúvida**Ao fazer o apontamento de uma **OP - Ordem de produção**, que possui subprodutos, como são definidos os números de lote dos subprodutos?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Para os subprodutos não há um campo de preenchimento do lote em tela, seu número é definido através da fórmula especificada no campo **B1\_FORMLOT - Código da fórmula para preenchimento do lote** ou no parâmetro **MV\_FORMLOT - Código da fórmula default utilizada para preenchimento dos lotes**, se não for determinada uma fórmula através do campo ou do parâmetro o Sistema irá atribuir o lote **AUTO** seguido de um sequencial.
