---
article_id: 1500010811321
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 086d6559ad62a88d706f28a49e207851a815d3019557a42301f490739ca11e16
fetched_at: '2026-06-28T22:38:44.035036+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Emissão de nota fiscal de
  saída no módulo Faturamento
type: support-article
updated_at: '2025-10-28T18:58:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010811321-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Emiss%C3%A3o-de-nota-fiscal-de-sa%C3%ADda-no-m%C3%B3dulo-Faturamento
---

**Dúvida**

Com incluir uma NF de saída no módulo Faturamento?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da release 12  
  
**Solução**

No módulo **Faturamento**, não é possível incluir uma **nota fiscal de saída (MATA461)** diretamente, diferentemente do que ocorre com o **documento de entrada**.

Para **emitir** uma nota fiscal de saída, é necessário **primeiro gerar um pedido de venda** e **liberá-lo**, deixando-o **apto para faturamento**.

A **preparação da nota de saída** pode ser realizada de **duas formas**:

* **1 -** Através da rotina **"Pedidos de Venda (MATA410)**: opção **"Outras ações > Prep.Doc.saída"**

![prep_docs_mata410.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500017696681)

* **2 -** Através da rotina **"Documentos de Saída (MATA460A)":**

![prep_docs_mata461.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500017429802)

A  geração da nota fiscal de saída, quando for do tipo Normal, irá gerar títulos a receber (**SE1**) para pagamento do cliente.

Para faturar mais de um pedido ao mesmo tempo, basta selecionar os pedidos que deseja faturar através do browser do mata460a, e depois clique em prep. docs , conforme visto acima, e o processo seguirá da mesma forma, gerando as notas para cada pedido.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5526027525911)

Se o processo for incluir pagamento para fornecedor por meio de títulos a pagar (SE2), efetue o processo do artigo: **[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como incluir Documento de Entrada com Solicitação de Compras e Pedido de Compras?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037447974-MP-SIGACOM-Como-incluir-Documento-de-Entrada-com-Solicita%C3%A7%C3%A3o-de-Compras-e-Pedido-de-Compras-)**

Em caso de dúvidas relacionadas a documento de entrada, contate nossa equipe de Compras para melhor orientação.

**Saiba Mais:**

**[Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Tamanho da numeração de notas fiscais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019924212-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Tamanho-da-numera%C3%A7%C3%A3o-de-notas-fiscais)**

**Processos de Pedido de Vendas:  <https://tdn.totvs.com/display/PROT/Pedidos+de+Venda+-+MATA410+-+Faturamento+-+P12>**

**Documento de referência sobre Documento de saída: [Documentos de Saída - MATA461 - Faturamento - P12](https://tdn.totvs.com/pages/viewpage.action?pageId=256317539)**
