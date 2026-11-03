---
article_id: 360026231571
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 9eea5d345536bdc35881597f558d743fdefd8fefd81aebc6617d9ebd6daee936
fetched_at: '2026-06-28T22:42:44.626499+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Número do pedido de venda não é preenchido
  na Ordem de Produção
type: support-article
updated_at: '2021-07-30T13:18:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026231571-Manufatura-Linha-Protheus-SIGAPCP-N%C3%BAmero-do-pedido-de-venda-n%C3%A3o-%C3%A9-preenchido-na-Ordem-de-Produ%C3%A7%C3%A3o
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:00:40 min****Dúvida**Por que o número do **Pedido de venda** não é preenchido na **OP - Ordem de Produção**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Na lista de parâmetros da rotina de **OP** **por Venda**, no **MATA650** **- Ordens de Produção,** verifique o conteúdo do parâmetro **Avalia Pedido de Venda**. Se o conteúdo deste parâmetro for:

* **Agrupadamente**: o Sistema avalia todos os itens marcados e depois gera uma única **OP**.
* **Individualmente**: será gerada uma **OP** para cada item marcado e assim é preenchida a informação do número da **OP** no campo **C2\_PEDIDO - Pedido de Venda** e **C2\_ITEMPV - Item PV**.
