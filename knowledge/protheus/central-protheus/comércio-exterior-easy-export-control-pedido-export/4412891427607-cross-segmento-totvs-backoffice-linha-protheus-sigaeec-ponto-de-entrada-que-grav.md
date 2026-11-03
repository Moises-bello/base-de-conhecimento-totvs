---
article_id: 4412891427607
category: Comércio Exterior - Easy Export Control - Pedido - Export
content_hash: d29e64d7a680efe747a194df1df8c774641b842109f408a70c115ba7cbdda52f
fetched_at: '2026-06-28T22:36:59.058864+00:00'
product: protheus
section_id: 1500001538181
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Ponto de entrada
  que grava as informações da tabela SC5
type: support-article
updated_at: '2024-07-04T13:21:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412891427607-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Ponto-de-entrada-que-grava-as-informa%C3%A7%C3%B5es-da-tabela-SC5
---

**Dúvida**Foi criado um campo novo na tabela **SC5** da rotina Pedido de Venda **(MATA410)** e preciso que leve a informação da tabela **EE7** da rotina de Pedido de Exportação **(EECAP100)** para ele.  Temos um ponto de entrada que grava as informações do Pedido de Venda (MATA410) na tabela SC5. (faturamento)?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – Todas versões  
  
**Solução**O ponto de entrada que grava informações na tabela **SC5** e leva a tabela **EE7** seria a função  **EECFAT3** e o parâmetro é o **PE\_GRVCAPA**. Será necessário fazer a alteração da variável **aCab**.

**Saiba mais**[PE EECFAT2 Integração com Faturamento (SIGAFAT)](https://tdn.totvs.com/pages/releaseview.action?pageId=309408592)
