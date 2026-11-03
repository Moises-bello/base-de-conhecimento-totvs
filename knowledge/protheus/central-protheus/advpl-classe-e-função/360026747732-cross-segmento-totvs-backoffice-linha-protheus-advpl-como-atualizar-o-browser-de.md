---
article_id: 360026747732
category: ADVPL - Classe e Função
content_hash: 352d5cb22f762225bd0db67187f0ea6bb8683d026bde4e24a8ae5300b8efabfa
fetched_at: '2026-06-28T22:40:15.498618+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Como atualizar o
  Browser de um MarkBrow
type: support-article
updated_at: '2022-01-04T20:14:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026747732-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-atualizar-o-Browser-de-um-MarkBrow
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como atualizar o objeto da Função MarkBrow após posicionar em um registro?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Deve se utilizar a função refresh().  
Exemplo:

```
#include 'protheus.ch'  
#include 'parmtype.ch'  
#Include 'FWMVCDef.ch'  
  
user function MarkBrow()  
Private aRotina := MenuDef()  
//ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿  
 //³ Endereca a funcao de BROWSE ³  
 //ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ  
 MarkBrow("SC9","C9_OK",,,.t.,GetMark())  
return  
  
Static Function MenuDef()  
Local aRotina := {}  
ADD OPTION aRotina TITLE "Pesquisar" ACTION 'PesqBrw' OPERATION 1 ACCESS 0   
ADD OPTION aRotina Title 'Visualizar' Action 'AxVisual' OPERATION 2 ACCESS 0  
ADD OPTION aRotina Title 'Incluir' Action 'AxInclui' OPERATION 3 ACCESS 0  
ADD OPTION aRotina Title 'Alterar' Action 'AxAltera' OPERATION 4 ACCESS 0  
ADD OPTION aRotina Title 'Excluir' Action 'AxDeleta' OPERATION 5 ACCESS 0  
ADD OPTION aRotina Title 'Rotina Browser' Action 'U_Posic()' OPERATION 2 ACCESS 0  
Return aRotina  
  
User Function Posic()  
oObjMBrw := GetMarkBrow()  
oObjMBrw:oBrowse:GoTop()  
oObjMBrw:oBrowse:Refresh()  
  
return
```
