---
article_id: 4411583141399
category: RH - Provisão
content_hash: 8160e975702a3176c09260ab28747d1e4a7d72ac87c357d37c0502ca0e7b7ca4
fetched_at: '2026-06-28T22:43:56.010767+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Ponto de entrada GP070PIF - INSS/FGTS - Férias
  Proporcional
type: support-article
updated_at: '2025-06-17T20:00:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411583141399-RH-Linha-Protheus-GPE-Ponto-de-entrada-GP070PIF-INSS-FGTS-F%C3%A9rias-Proporcional
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18016404332567) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Utilização do ponto de entrada  GP070PIF.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Solução****01. Visão Geral**Ponto de Entrada para alterar os valores de INSS e FGTS na provisão de Férias Proporcionais (a vencer).  
  
**Programa Fonte**GPEM070.PRW  
  
**Sintaxe**GP070PIF - INSS/FGTS - Férias Proporcional ( ) --> uRet  
Retorno  
**uRet**(qualquer)  
  
**02. Exemplos de Utilização**User Function GP070PIF()  
nP\_Inss := 100.00  
nP\_Fgts := 200.00  
Return()  
  
**03. Variáveis****Outras Ações / Ações relacionadas**

| Nome | Tipo | Escopo | Pode Alterar |
| --- | --- | --- | --- |
| nP\_Inss | Numérico | Privado | Sim |
| nP\_Fgts | Numérico | Privado | Sim |

![GP070PIF.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/18019025901079)

**Saiba Mais:**

<https://tdn.totvs.com/pages/viewpage.action?pageId=642641323>
