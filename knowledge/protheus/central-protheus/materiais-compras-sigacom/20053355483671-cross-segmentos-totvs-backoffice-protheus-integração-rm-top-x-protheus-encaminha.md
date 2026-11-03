---
article_id: 20053355483671
category: Materiais - Compras (SIGACOM)
content_hash: bcf9332b5d0ecd90c2859a0241035bc6a4bb01ba62cde70c6aaff655477f05de
fetched_at: '2026-06-28T22:41:12.874801+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - Integração RM TOP x Protheus
  encaminha o pedido de compras com valores de faturamento direto, dedução e retenção
type: support-article
updated_at: '2023-12-26T11:07:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20053355483671-Cross-Segmentos-Totvs-Backoffice-Protheus-Integra%C3%A7%C3%A3o-RM-TOP-x-Protheus-encaminha-o-pedido-de-compras-com-valores-de-faturamento-direto-dedu%C3%A7%C3%A3o-e-reten%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20053355476503) Tempo aproximado para leitura: **00:02 min****Dúvida**Como é tratado os valores quando a Integração RM TOP x Protheus encaminha o pedido de compras com valores de faturamento direto, dedução e retenção?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - A partir da Versão 12  
  
**Solução**

Receber um pedido de compras gerado pelo RM TOP que contenha valores de Faturamento Direto, Dedução e Retenção.

1 - Inserir um documento de entrada e associá-lo ao pedido de compra originado pelo RM TOP. Ao vincular o pedido, os montantes de Faturamento Direto, Dedução e Retenção serão automaticamente transferidos para o documento.   
  
2 - Na seção "Duplicatas", o valor correspondente na duplicata será ajustado conforme os montantes informados nos campos de Faturamento Direto, Dedução e Retenção.

3 - Ao confirmar o documento de entrada, o pedido de compra será atualizado com o valor utilizado no documento de entrada.

**Atenção:** Para que o processo funcione corretamente é necessário ter o parâmetro **MV\_PMSITMU** habilitado.

***Saiba Mais:***

* [PCOM04030 - Pedido de Compras - Integração RM TOP - Faturamento Direto / Dedução / Retenção](https://tdn.totvs.com.br/pages/releaseview.action?pageId=815579595)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
