---
article_id: 4411593398551
category: RH - Provisão
content_hash: 401ddfab75cceb6dba9e412ba947e2fd3e0e862a6c96291401c0f417ab4ea94f
fetched_at: '2026-06-28T22:43:56.953205+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Ponto de Entrada GP090DIF - INSS e FGTS de Provisão
  de 13º Salário
type: support-article
updated_at: '2024-08-22T14:37:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411593398551-RH-Linha-Protheus-GPE-Ponto-de-Entrada-GP090DIF-INSS-e-FGTS-de-Provis%C3%A3o-de-13%C2%BA-Sal%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17990019800087) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Utilização do ponto de entrada GP090DIF.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Solução**

**Ponto de Entrada:** GP090DIF - INSS e FGTS de Provisão de 13º Salário.

**Descrição:** Ponto de entrada para alterar INSS e FGTS de Provisão de 13º Salário.  
  
**Programa Fonte:** GPEM080.PRX  
  
**Sintaxe:**

GP090DEC ()

Parâmetros: Nenhum

Retorno: NIL

Variáveis Disponpiveis:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Nome | Tipo | Escopo | Pode Alterar | Descrição |
| nV\_INSS | Numérico | Privado | Sim | Valor do INSS de 13º calculado |
| nV\_FGTS | Numérico | Privado | Sim | Valor do FGTS de 13º calculado |

**Exemplo**:  
#Include '[Protheus.ch](http://protheus.ch/)'  
User Function GP090DIF ()  
nV\_INSS :=u\_VaIINSS() //Valor do INSS  
nV\_FGTS :=u\_ValFGTS() // Valor do FGTS

**Saiba Mais:**

[Ponto de Entrada GP090DIF](https://tdn.totvs.com/pages/viewpage.action?pageId=863913997)   
[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
