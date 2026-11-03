---
article_id: 22567604376599
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 577e45b6be9f80cade95a0f321705790cfa4adc96ad74571bc809716569003c9
fetched_at: '2026-06-28T22:38:39.742764+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Composição dos campos da
  liberação manual da rotina de análise de crédito de cliente MATA450A
type: support-article
updated_at: '2024-04-05T11:49:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22567604376599-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Composi%C3%A7%C3%A3o-dos-campos-da-libera%C3%A7%C3%A3o-manual-da-rotina-de-an%C3%A1lise-de-cr%C3%A9dito-de-cliente-MATA450A
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22567604366615) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Qual a composição dos campos da liberação manual da rotina de análise de crédito de cliente MATA450A?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da release 12.

**Solução**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22567612109463)

* **Lim. Credito** = Limite de Crédito "A1\_LC";
* **Saldo Título** = [Títulos em aberto "E1\_STATUS = A"] - [RA];
* **Sl.Pd.Bl.Cre** = Saldo em Pedidos Liberados, bloqueados por crédito;
* **Sld Ped. Lib** = Saldo em Pedidos Liberados sem bloqueio de crédito;
* **Saldo Lim.Credito** = [**Lim. Credito**] - [**Saldo Título**] - [**Sld Ped. Lib**];
* **Adicional LC** = [**Sl.Pd.Bl.Cre**] + [**Sld Ped. Lib**] - [**Lim. Credito**] + [**Saldo Título**].

**Observação:** Os demais campos podem ser consultados no Cadastro do Cliente (tabela SA1).

**Saiba mais:**

[Dados Técnicos (MATA450A - SIGAFAT)](https://tdn.totvs.com/x/WaLaFQ)
