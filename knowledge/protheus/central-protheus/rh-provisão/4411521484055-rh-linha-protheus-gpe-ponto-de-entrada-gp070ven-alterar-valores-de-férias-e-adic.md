---
article_id: 4411521484055
category: RH - Provisão
content_hash: 4ad1fa228de317033c964097c080fc15a06b1cb47f5f6c88e8c7393af3b2dc8f
fetched_at: '2026-06-28T22:43:56.942062+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Ponto de Entrada GP070VEN - Alterar valores de
  férias e adicionais de férias vencidas na provisão
type: support-article
updated_at: '2025-10-24T13:05:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411521484055-RH-Linha-Protheus-GPE-Ponto-de-Entrada-GP070VEN-Alterar-valores-de-f%C3%A9rias-e-adicionais-de-f%C3%A9rias-vencidas-na-provis%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32997908271383) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Utilização do ponto de entrada GP070VEN.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Solução****01. VISÃO GERAL**

Ponto de entrada para alterar os valores de férias e adicionais de férias vencidas na provisão.

**Programa Fonte**

GPEM070.PRW

**Sintaxe**

GP070VEN - Adicional de Férias Vencidas ( ) --> Nill

Retorno

**Nill**

(qualquer)

**02. EXEMPLO DE UTILIZAÇÃO**

User Function GP070VEN()

nV\_Valor := 1000.00

nV\_Adic := 300.00

Return()

**03. VARIÁVEIS**

**Outras Ações / Ações relacionadas**

| Nome | Tipo | Escopo | Pode Alterar |
| --- | --- | --- | --- |
| nV\_Valor | Numérico | Privado | Sim |
| nV\_Adic | Numérico | Privado | Sim |

**Saiba Mais:**

<https://tdn.totvs.com/pages/viewpage.action?pageId=642644879>
