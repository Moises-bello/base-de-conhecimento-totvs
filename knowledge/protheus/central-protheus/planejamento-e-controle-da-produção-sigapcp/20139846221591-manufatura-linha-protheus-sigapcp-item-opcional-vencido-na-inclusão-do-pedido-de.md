---
article_id: 20139846221591
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 31f7b07cbd7e271c59c3a6fc4bbcda385fbe515ad6eaa213c01927717b0b76cf
fetched_at: '2026-06-28T22:42:43.499517+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Item opcional vencido na inclusão do
  pedido de venda
type: support-article
updated_at: '2023-12-27T16:49:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20139846221591-Manufatura-Linha-Protheus-SIGAPCP-Item-opcional-vencido-na-inclus%C3%A3o-do-pedido-de-venda
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20139818801303)*Tempo aproximado para leitura:**00:01:25 min  
  
Dúvida**Por que o item opcional está como vencido na inclusão do **pedido de venda**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Essa situação ocorre quando o **componente** vinculado ao item opcional não está válido para atender a **produção**.  
Para que o item opcional não apareça como vencido na inclusão do **pedido de venda** através da rotina **MATA410 - Pedido de Venda**, a data de entrega do **pedido de venda** informada no campo **C6\_ENTREG - Data de Entrega** menos o **prazo de produção** deve ser maior do que a data inicial do componente na estrutura e menor que a data final do componente na estrutura.  
  
**Saiba mais**Para saber como o Sistema calcula o **prazo de produção**, acesse: [Manufatura - Linha Protheus - SIGAPCP - Cálculo da previsão de entrega ou previsão inicial de um produto na geração da OP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029130031-Manufatura-Linha-Protheus-SIGAPCP-C%C3%A1lculo-da-previs%C3%A3o-de-entrega-ou-previs%C3%A3o-inicial-de-um-produto-na-gera%C3%A7%C3%A3o-da-OP?source=search)Para mais informações sobre item opcional vencido na abertura da **OP - Ordem de Produção**, acesse: [Manufatura - Linha Protheus - SIGAPCP - Item opcional vencido está aparecendo ao abrir uma OP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027616251-Manufatura-Linha-Protheus-SIGAPCP-Item-opcional-vencido-est%C3%A1-aparecendo-ao-abrir-uma-OP)
