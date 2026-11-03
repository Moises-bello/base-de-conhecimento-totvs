---
article_id: 360016417992
category: ADVPL - Classe e Função
content_hash: 8ae317abdd54736ab700eab9e916e1c34cfb89072e3572568521c0949f570ef2
fetched_at: '2026-06-28T22:40:14.465897+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Associar uma tecla
  de atalho para definir o foco em um objeto na aplicação
type: support-article
updated_at: '2022-04-06T16:48:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016417992-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Associar-uma-tecla-de-atalho-para-definir-o-foco-em-um-objeto-na-aplica%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:03:00 min****Dúvida**Associar uma tecla de atalho para definir o foco em um objeto na aplicação.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80.  
  
**Solução**É possível associar uma tecla de atalho para definir o foco em um determinado objeto utilizando em conjunto a função **SetKey** e o método **SetFocus**.   
A seguir um exemplo utilizando dois objetos **MsGet**, onde a tecla de atalho F12 realiza o foco no segundo objeto.

```
#Include 'Protheus.ch'  
  
User Function tstge()  
  
Local oButton1  
Local oGet1  
Local oGet2  
Local cGet1 := ' '  
Local cGet2 := ' '  
Local oSay1  
Local oSay2  
Static oDlg  
  
DEFINE MSDIALOG oDlg TITLE "Teste Foco" FROM 000, 000 TO 300, 500 COLORS 0, 16777215 PIXEL  
  
 @ 038, 065 SAY oSay1 PROMPT "Código 1" SIZE 049, 007 OF oDlg COLORS 0, 16777215 PIXEL  
 @ 048, 065 MSGET oGet1 VAR cGet1 SIZE 060, 010 OF oDlg COLORS 0, 16777215 PIXEL  
   
 @ 075, 065 SAY oSay2 PROMPT "Código 2" SIZE 049, 007 OF oDlg COLORS 0, 16777215 PIXEL  
 @ 085, 065 MSGET oGet2 VAR cGet2 SIZE 060, 010 OF oDlg COLORS 0, 16777215 PIXEL   
   
 SetKey(VK_F12, {|| oGet2:SetFocus() }) //Foco no código 2  
  
ACTIVATE MSDIALOG oDlg CENTERED  
  
Return
```
