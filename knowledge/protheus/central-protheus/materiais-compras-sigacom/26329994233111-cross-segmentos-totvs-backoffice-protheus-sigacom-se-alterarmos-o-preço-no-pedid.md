---
article_id: 26329994233111
category: Materiais - Compras (SIGACOM)
content_hash: 74189e102f5dd7c3bb0f3e87fd3ee740e1ff7398c7f633b3c99ce8aa6fdbc48f
fetched_at: '2026-06-28T22:41:25.317017+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Se alterarmos o preço
  no Pedido de Compra, a tabela de preços vinculada ao pedido também será atualizada?
type: support-article
updated_at: '2024-09-12T17:52:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26329994233111-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Se-alterarmos-o-pre%C3%A7o-no-Pedido-de-Compra-a-tabela-de-pre%C3%A7os-vinculada-ao-pedido-tamb%C3%A9m-ser%C3%A1-atualizada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26329994211991) Tempo aproximado para leitura: **HH:02:00 min** **Dúvida**Se alterarmos o preço no Pedido de Compra, a tabela de preços vinculada ao pedido também será atualizada?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus Compras - Todas as versões  
  
**Solução**

Alterar o preço no Pedido de Compra não atualizará automaticamente o preço na tabela vinculada. Para atualizar o valor corretamente, siga estas etapas:

1. **Atualize a Tabela de Preço:**

   * Modifique o campo AIB\_PRCCOM com o novo valor unitário.
2. **Atualize o Pedido de Compra:**

   * Na rotina do Pedido de Compra, pressione Enter e selecione a opção para atualizar a informação do campo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26329977816343)  
3-) Na rotina do Pedido de Compra, no campo C7\_CODTAB, selecionar o código e apertar o Enter para atualizar o campo.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26329977819799)  
  
***Saiba Mais:***

[Tabela de Preços no Pedido de Compras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5745230677783-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-carregar-a-Tabela-de-Pre%C3%A7os-no-Pedido-de-Compras?source=search)

[Pagina Centralizadora](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
