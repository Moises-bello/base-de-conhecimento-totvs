---
article_id: 360007451231
category: Gestão de Transportes (TMS)
content_hash: 2157d96818a9475b4ba6a35369d52d9da05b81e188007e3b42179ba3116b9ada
fetched_at: '2026-06-28T22:45:29.651134+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada TM040COL Alterações antes
  da Solicitação de Coleta
type: support-article
updated_at: '2022-01-18T14:05:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007451231-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-TM040COL-Altera%C3%A7%C3%B5es-antes-da-Solicita%C3%A7%C3%A3o-de-Coleta
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png)*** Tempo aproximado para leitura: **00:00:42 min****Dúvida**Como implementar o ponto de entrada **TM040COL** **Alterações antes da Solicitação de Coleta**?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O ponto de entrada **TM040COL** está localizado no **TMSA040** **Cotação de Frete** e permite ao usuário realizar alterações antes da geração da solicitação de coleta. Lembrando que neste Ponto de Entrada podemos utilizar algumas variáveis de memória que estão posicionadas como por exemplo **M->DT5\_DDD**, **M->DT5\_TEL**.  
  
**Programa Fonte**: TMSA040.PRW  
  
**Sintaxe**: TM040COL - Alterações antes da Solicitação de Coleta ( [ Nulo ] ) --> Nil  
  
**Parâmetros**:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Nome | Tipo | Descrição | Default | Obrigatório | Referência |
| Nulo | Nulo |  |  |  |  |

**Retorno:**Nil         (nulo)  
  
**Exemplos**:  
#Include "Protheus.ch"  
User Function TM040COL()  
M->DT5\_NOME := Posicione('DUE',1,xFilial('DUE')+M->DT5\_DDD+M->DT5\_TEL,'DUE\_NOME')  
Return NIL  
 **Variáveis:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Nome | Tipo | Escopo | Pode Alterar | Descrição |
|  | Array of Record | Global | Não |  |
