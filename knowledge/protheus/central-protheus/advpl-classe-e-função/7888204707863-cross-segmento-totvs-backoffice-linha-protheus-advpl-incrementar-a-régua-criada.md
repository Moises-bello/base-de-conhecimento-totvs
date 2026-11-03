---
article_id: 7888204707863
category: ADVPL - Classe e Função
content_hash: 9a938f91932c1fa56e105bcbbcdf44a9d45d41e341498e59d187af3f8320b84e
fetched_at: '2026-06-28T22:40:16.957308+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Incrementar a régua
  criada pela função Processa
type: support-article
updated_at: '2025-08-13T19:37:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7888204707863-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Incrementar-a-r%C3%A9gua-criada-pela-fun%C3%A7%C3%A3o-Processa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34161609602327) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Incrementar a régua criada pela função Processa?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – Todas as versões  
  
**Solução**IncProc- Incrementa régua de progressão.  
  
**Sintaxe**IncProc() -> nil  
  
**Descrição**Para incrementar a régua criada pela função Processa(), utilizamos a função IncProc()  
  
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

**Saiba mais**

**[IncProc](https://tdn.totvs.com/display/public/framework/Processa)****[Processa](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7887883451799)****[ProcRegua](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7888046989591)**
