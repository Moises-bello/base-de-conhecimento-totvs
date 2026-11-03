---
article_id: 41423837183639
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 46a049feeab9f1fae1745416dc29c84ceca28446a87ec4861c8532603f005d1f
fetched_at: '2026-06-28T22:42:45.800015+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Quantidade da OP por venda diferente
  da quantidade do pedido de venda
type: support-article
updated_at: '2026-06-24T11:01:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41423837183639-Manufatura-Linha-Protheus-SIGAPCP-Quantidade-da-OP-por-venda-diferente-da-quantidade-do-pedido-de-venda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41423837168279) Tempo aproximado para leitura: **00:01:10 min**  
  
**Dúvida**  
Por que a quantidade da **OP - Ordem de Produção** gerada através da opção **venda** é diferente da quantidade do **pedido de venda**?  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**  
Quando o parâmetro **MV\_CONSEST - Considera Estoque na Geração da Ordem de Produção**está igual a **S** o Sistema pode gerar a **OP** com uma quantidade maior ou menor que o **pedido de venda**, por conta de uma demanda do estoque.  
Ou ainda o produto no qual foi gerado a **OP** possui lote econômico e/ou lote mínimo configurado no cadastro de produto e essa informação está sendo considerada.  
  
**Saiba mais**  
Para mais informações sobre não considerar o estoque na geração da OP por venda, acesse a documentação: [Manufatura - Linha Protheus - SIGAPCP - Não considerar saldo quando OP é aberta através do pedido de venda](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051263073-Manufatura-Linha-Protheus-SIGAPCP-N%C3%A3o-considerar-saldo-quando-OP-%C3%A9-aberta-atrav%C3%A9s-do-pedido-de-venda)
