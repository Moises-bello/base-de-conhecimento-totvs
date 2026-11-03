---
article_id: 4409190848535
category: Comércio Exterior - Easy Export Control - Pedido - Export
content_hash: e3535a1ccdfc414fad02c4bd7e75dd6dc1ff937cc6357811303957691f954e2e
fetched_at: '2026-06-28T22:36:59.063060+00:00'
product: protheus
section_id: 1500001538181
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Preenchimento
  do campo EE7_MARCAC no pedido de exportação.
type: support-article
updated_at: '2021-09-22T13:45:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409190848535-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Preenchimento-do-campo-EE7-MARCAC-no-pedido-de-exporta%C3%A7%C3%A3o
---

**Dúvida**De onde vem as informações para preenchimento do campo **EE7\_MARCAC** no pedido de exportação?  
  
**Ambiente** Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – Todas versões.  
  
**Solução**O conteúdo do campo **EE7\_MARCAC**, é inicializado do Importador se preenchido o campo **A1\_VM\_MARC** (Marcação).   
  
Caso contrario, quando não está preenchido o campo **A1\_VM\_MARC** (Marcação) do cadastro do importador/cliente, o sistema grava o conteúdo informado nos campos destacados na planilha a partir das tabelas SA1- SA2- SYA e SY9, de acordo com a via de transporte informada no pedido de exportação:

|  |  |  |
| --- | --- | --- |
| Tabelas | Campos | Descrição |
| SA1 | A1\_NREDUZ | N Fantasia |
| SA2 | A2\_NREDUZ | N Fantasia |
| SYA | YA\_NOIDIOM | No Idioma |
| SY9 | Y9\_DESCR | Descrição |
