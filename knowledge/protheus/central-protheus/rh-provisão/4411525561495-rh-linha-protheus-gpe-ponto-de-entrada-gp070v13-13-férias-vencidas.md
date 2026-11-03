---
article_id: 4411525561495
category: RH - Provisão
content_hash: 0c0785451178476cded258461e0e8d72f9bce9523352fbf35938d84cf2e80c78
fetched_at: '2026-06-28T22:43:55.981403+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Ponto de Entrada  GP070V13 - 1/3 Férias Vencidas
type: support-article
updated_at: '2025-06-17T19:55:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411525561495-RH-Linha-Protheus-GPE-Ponto-de-Entrada-GP070V13-1-3-F%C3%A9rias-Vencidas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18362473676439) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Utilização do ponto de entrada GP070V13.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Solução****01. VISÃO GERAL**

Ponto de entrada para alterar os valores de 1/3 das férias vencidas na provisão de férias.

**Programa Fonte**  
GPEM070.PRW

**Sintaxe**

GP070V13 - 1/3 Férias Vencidas ( ) --> URET

Retorno

**URET**

(qualquer)

**02. EXEMPLOS DE UTILIZAÇÃO**

**Exemplo 1:**  
User Function GP070V13()

nV\_UmTer := 25.00

Return()

**Exemplo 2:**

User Function GP070V13()

  

// ALTERA VALOR DE 1/3 DE FÉRIAS PROVISÃO EQUIVALENTE A 40%

nV\_UmTer := nV\_UmTer \* 1.2

Alert( "Passou pelo PE GP070v13" )

  

Return()

**03. Variáveis**

**Outras Ações / Ações relacionadas**

| Nome | Tipo | Escopo | Pode Alterar |
| --- | --- | --- | --- |
| nV\_UmTer | Numérico | Privado | Sim |

![GP070V13.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/18362679355799)

Base TDN: <https://tdn.totvs.com/pages/viewpage.action?pageId=642642826>

**Saiba Mais:**  
[RH - Linha Protheus - GPE - Pontos de Entrada disponíveis para a rotina de Provisão de Férias e 13º Salário GPEM070](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034848114-RH-Linha-Protheus-GPE-Pontos-de-Entrada-dispon%C3%ADveis-para-a-rotina-de-Provis%C3%A3o-de-F%C3%A9rias-e-13o-Sal%C3%A1rio-GPEM070)
