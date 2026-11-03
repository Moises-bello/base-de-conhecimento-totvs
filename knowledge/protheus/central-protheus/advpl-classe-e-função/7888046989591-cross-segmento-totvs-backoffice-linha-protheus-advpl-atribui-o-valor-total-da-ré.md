---
article_id: 7888046989591
category: ADVPL - Classe e Função
content_hash: 3737ab7ecf63928197632a6c7631c7906fb9d812d61998fae6d68234ef548192
fetched_at: '2026-06-28T22:40:14.473013+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Atribui o valor
  total da régua de progressão
type: support-article
updated_at: '2025-08-13T19:38:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7888046989591-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Atribui-o-valor-total-da-r%C3%A9gua-de-progress%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34161581035287) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Atribui o valor total da régua de progressão?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – Todas as versões  
  
**Solução**ProcRegua - Atribui o valor total da régua de progressão cria pela pela função **Processa**().  
  
**Sintaxe**ProcRegua( *nTotal* ) -> nil

|  |  |  |  |
| --- | --- | --- | --- |
| Argumento | Obrigat. | Tipo | Descrição |
| nTotal | Sim | N | Valor total da régua. |

**Descrição**Após atribuir o valor total da régua, para incrementar utilizamos a função **IncProc**().  
  
**Exemplo**

```
User Function <nome-da-função>( )  
  
Local bAcao := {|lFim| Exemplo(@lFim) }  
  
Local cTitulo := ''  
Local cMsg := 'Processando'  
Local lAborta := .T.  
  
Processa( bAcao, cTitulo, cMsg, lAborta )  
  
Return  
  
Static Function Exemplo(lFim)  
  
Local nI  
  
ProcRegua(10000)  
  
For nI := 1 To 10000  
   If lFim  
      Exit  
   EndIf  
   IncProc()  
Next nI  
  
Return
```

**Saiba mais  
[ProcRegua](https://tdn.totvs.com/display/public/framework/Processa)****[IncProc](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7888204707863)****[Processa](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7887883451799)**
