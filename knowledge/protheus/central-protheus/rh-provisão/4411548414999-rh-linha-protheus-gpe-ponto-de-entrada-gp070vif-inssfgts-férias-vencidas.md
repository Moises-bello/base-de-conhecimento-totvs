---
article_id: 4411548414999
category: RH - Provisão
content_hash: 4489348379b9125f120440dfcd237cace1ab1533cd9067497345649dd88a3308
fetched_at: '2026-06-28T22:43:56.023624+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Ponto de entrada GP070VIF - INSS/FGTS - Férias
  Vencidas
type: support-article
updated_at: '2025-06-17T20:25:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411548414999-RH-Linha-Protheus-GPE-Ponto-de-entrada-GP070VIF-INSS-FGTS-F%C3%A9rias-Vencidas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17987950930455) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Utilização do ponto de entrada GP070VIF.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Solução****01. VISÃO GERAL**

Ponto de Entrada para alterar os valores de Inss e FGTS na provisão de férias vencidas.  
**Programa Fonte**

GPEM070.PRW

**Sintaxe**

GP070VIF - INSS/FGTS - Férias Vencidas ( ) --> NILL

Retorno

**NILL**

(qualquer)

**02. EXEMPLO DE UTILIZAÇÃO**

User Function GP070VIF()

nV\_Inss := 10.00

nv\_Fgts := 20.00

Return()

**03. VARIÁVEIS**

**Outras Ações / Ações relacionadas**

| Nome | Tipo | Escopo | Pode Alterar |
| --- | --- | --- | --- |
| nV\_Inss | Numérico | Privado | Não |
| nV\_Fgts | Numérico | Privado | Não |

![GP070VIF.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17987952902167)

**Saiba Mais:**

<https://tdn.totvs.com/pages/viewpage.action?pageId=642645497>
