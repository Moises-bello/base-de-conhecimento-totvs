---
article_id: 360025602692
category: Inspeção de Entradas (SIGAQIE)
content_hash: 15487467452d9cfd86ab12102d2f228ea5e1a1aac2b22d0bf5c38afc25041198
fetched_at: '2026-06-28T22:42:26.855246+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - Aba Baixas do CQ não é exibida na rotina
  de Resultados
type: support-article
updated_at: '2021-12-23T17:44:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025602692-Manufatura-Linha-Protheus-SIGAQIE-Aba-Baixas-do-CQ-n%C3%A3o-%C3%A9-exibida-na-rotina-de-Resultados
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:01:05 min****Dúvida**Por que na rotina **QIEA215** - **Resultados**, ao visualizar o laudo, em alguns casos não é apresentada a aba **Baixas do CQ**?   
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Versão 12  
  
**Solução**A aba **Baixas do CQ** é exibida quando:

* A entrada teve origem na rotina **MATA103** - **Documento de Entrada** ou **MATA101N - Factura de Entrada**. A rotina **MATA101N** é utilizada apenas por clientes do **Mercado Internacional**. Caso a entrada for realizada pela rotina **QIEA200** **- Entradas** esta aba não é exibida, pois não houve movimentação de estoque;
* O campo **B1\_TIPOCQ - Tipo CQ** da aba **CQ** do **MATA010 - Cadastro de Produtos** seja igual à **SigaQuality**;
* E quando a **TES - Tipos de Entrada e Saída** utilizada no documento de entrada está parametrizada para atualizar estoque, ou seja, quando o campo **F4\_ESTOQUE - Atu. Estoque** está como **Sim** do **MATA080 - Atualização da TES.**
