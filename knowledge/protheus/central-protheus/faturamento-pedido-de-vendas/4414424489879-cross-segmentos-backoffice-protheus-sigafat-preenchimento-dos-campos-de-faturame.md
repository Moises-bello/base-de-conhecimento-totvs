---
article_id: 4414424489879
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: e84be085b018061ca2d65ba15d07cfbf43368ea6f118fc6943f987ba66c5f842
fetched_at: '2026-06-28T22:38:39.997511+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Preenchimento dos campos
  de faturamento da tabela SB2
type: support-article
updated_at: '2026-06-12T14:11:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414424489879-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Preenchimento-dos-campos-de-faturamento-da-tabela-SB2
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22661059523863) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Como os campos de faturamento a SB2 são preenchidos?  
  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT (Faturamento) - A partir da release 11.80.  
  
  
**Solução**

Tabela “SB2” - Saldos Físico e Financeiro

Na **Análise de Saldo do Produto em Estoque**, o sistema considera os dados da tabela “**SB2**” (**Saldos Físico e Financeiro**) validando, principalmente, os **campos**:

* “**Saldo Atual**” (**B2\_QATU**): Saldo Atual do Produto no Estoque, porém **não significa** que esta quantidade está **disponível para venda**, pois nela estão somadas as **quantidades empenhadas** e de **terceiros**;

* “**Quantidade Empenhada**” (**B2\_QEMP**): Quantidade do produto **destinada** ao atendimento de **Ordens de Produção**;

* “**Qtd. Reservada**” (**B2\_RESERVA**): Quantidade **Reservada** por um **Pedido de Vendas**, este campo é alimentado pelas **Quantidades** deste produto em **Pedidos de Venda Liberados sem bloqueio de estoque (apto a faturar)**;

* “**Qtd. Pedido de Vendas**” (**B2\_QPEDVEN**): Quantidade em **Pedido de Vendas**, campo é alimentado pelas **Quantidades** deste produto em **Pedidos de Venda em aberto ou liberado com estoque bloqueado (ainda não apto para faturar)**;

* “**Qt. Ter. Ns. Pd.**” (**B2\_QTNP**):  Quantidade de **Terceiros em Nosso Poder**, indica a **Quantidade** de produtos, em estoque, que **Pertence à Terceiros**. São materiais que deram entrada com um **TES** (Tipo de Entrada e Saída) que controla Poder de Terceiros (**F4\_PODER3**) como “**R-Remessa**”.

* “**Qt. Ns. Pd. Ter**” (**B2\_QNPT**): Quantidade **Nossa em Poder de Terceiros**, indica a **Quantidade** de seu estoque que **Está em Terceiros**. São Materiais que saíram com um **TES** (Tipo de Entrada e Saída) que controla Poder de Terceiros (**F4\_PODER3**) como “**R-Remessa**”.

**Saiba mais:**

[FAT0009 Configurações para Análise / Bloqueio de Estoque](https://tdn.totvs.com/pages/releaseview.action?pageId=555270781)
