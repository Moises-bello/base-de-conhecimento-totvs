---
article_id: 7887883451799
category: ADVPL - Classe e Função
content_hash: 33de098271fd16ea79141454d719e5ea858101896435d67b8652158f2a10493e
fetched_at: '2026-06-28T22:40:16.813007+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Função para criar
  régua de progressão
type: support-article
updated_at: '2025-08-13T19:36:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7887883451799-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Fun%C3%A7%C3%A3o-para-criar-r%C3%A9gua-de-progress%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34161537477783) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Função para criar régua de progressão.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – Todas as versões  
  
**Solução**Processa - Cria diálogo com uma régua de progressão.  
  
**Sintaxe**Processa( *bAcao,* [ *cTitulo* ] *,* [ *cMsg* ]*,* [ *lAborta*]  ) -> nil

|  |  |  |  |
| --- | --- | --- | --- |
| Argumento | Obrigat. | Tipo | Descrição |
| bAcao | Sim | C | Função a ser executada. |
| *cMsg* | Não | C | Mensagem a ser exibida a baixo da régua de progressão |
| *cTitulo* | Não | C | Título de janela |
| *lAborta* | Não | L | Habilita botão cancelar. |

**Descrição**A função Processa() cria um diálogo onde a execução de um determinada função pode ser acompanhada através de uma régua de progressão. Para atribuir o valor total da régua utilizamos a função ProcRegua() e para incrementar a régua utilizamos a função IncProc().  
  
Exemplo

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
  
Next  
Return
```

**Saiba mais  
[Processa](https://tdn.totvs.com/display/public/framework/Processa)****[IncProc](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7888204707863)****[ProcRegua](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7888046989591)**
