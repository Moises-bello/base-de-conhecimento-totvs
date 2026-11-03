---
article_id: 360007199672
category: Gestão de Transportes (TMS)
content_hash: 797af980e3de95a6a1680d895822e8bf57de979fb062f7a87274c237065393e2
fetched_at: '2026-06-28T22:45:29.610732+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada TM040APR Alteração de Status
  da Cotação de Frete
type: support-article
updated_at: '2022-01-18T17:25:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007199672-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-TM040APR-Altera%C3%A7%C3%A3o-de-Status-da-Cota%C3%A7%C3%A3o-de-Frete
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png)*** Tempo aproximado para leitura: **00:00:54 min  
  
Dúvida**Como implementar o ponto de entrada **TM040APR** **Alteração de Status da Cotação de Frete**?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O ponto de entrada **TM040APR** está localizado no **TMSA040** **Cotação de Frete** e permite ao usuário realizar validação e alterar o *Status* **DT4\_STATUS** da cotação de frete. Lembrando que neste Ponto de Entrada podemos utilizar algumas variáveis de memória que estão posicionadas como **M->DT4\_FILORI** , **M->DT4\_NUMCOT**.  
  
**Programa Fonte**: TMSA040.PRW  
  
**Sintaxe**: TM040APR - Alteração de Status da Cotação de Frete ( [ nOpcx ] ) --> lRet  
**Parâmetros**:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Nome | Tipo | Descrição | Default | Obrigatório | Referência |
| nOpcx | Array of Record |  |  |  |  |

**Retorno:**  
lRet  
       (logico)  
  
**Exemplos:**#Include "Protheus.ch"  
User Function TM040APR()      
Local nOpcx := ParamIXB[1]  
Local lRet := .T.  
If nOpcx == 3   
       lRet := .F.  
End If  
Return lRet  
  
**Variáveis:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Nome | Tipo | Escopo | Pode Alterar | Descrição |
|  | Array of Record | Global | Não |  |
