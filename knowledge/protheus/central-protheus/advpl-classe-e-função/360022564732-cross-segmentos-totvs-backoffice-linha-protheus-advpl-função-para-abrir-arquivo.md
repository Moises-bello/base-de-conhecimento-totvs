---
article_id: 360022564732
category: ADVPL - Classe e Função
content_hash: 283bebde330ea6a9bc96f9f18c5ad643fb6b08b607aa2a9276cd6a7cda5c011b
fetched_at: '2026-06-28T22:40:19.424913+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Função para abrir
  arquivo do word
type: support-article
updated_at: '2022-01-10T21:30:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022564732-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Fun%C3%A7%C3%A3o-para-abrir-arquivo-do-word
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min****Dúvida**Existe uma função do Advpl que possa selecionar documentos do tipo word nas pastas abaixo do server, ou seja, subpastas de Protheus\_data   
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Temos função **[CGETFILE](http://tdn.totvs.com/display/tec/cGetFile)** para obter o caminho do arquivo e utilizar as funções:(**[CpyS2T](http://tdn.totvs.com/display/tec/CpyS2T)**, **[MemoWrite](http://tdn.totvs.com/display/tec/MemoWrite), [OLE\_OPENFILE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022751891-MP-ADVPL-GENERIC-INTEGRACAO-COM-O-WORD-E-COPIAS-DE-ARQUIVO?source=search)**)

```
#Include 'Protheus.ch'  
#INCLUDE "PROTHEUS.CH"  
#INCLUDE "TBICONN.CH"  
  
User Function fPegaArq()  
 Local cArqAux := ""  
 Private oWord  
  
cArqAux := cGetFile( "Arquivo Texto | *.*",; //Máscara  
                              "Arquivo...",; //Título  
                                          ,; //Número da máscara  
                                          ,; //Diretório Inicial  
                                       .T.,; //.F. == Abrir; .T. == Salvar  
                            GETF_LOCALHARD,; //Diretório full. Ex.: 'C:\TOTVS\arquivo.docx'  
                                        .F.) //Não exibe diretório do servidor  
   
 //Caso o arquivo não exista ou estiver em branco ou não for a extensão docx  
 If Empty(cArqAux) .Or. !File(cArqAux) .Or. (SubStr(cArqAux, RAt('.', cArqAux)+1, 3) != "dot" .And. SubStr(cArqAux, RAt('.', cArqAux)+1, 3) != "docx")  
 Alert("Arquivo inválido!" - "Atenção")  
   
 //Senão, define abra arquivo  
 Else  
  OpenWord(@oWord,cArqAux)  
 EndIf  
Return  
  
  
Static Function OpenWord(oWord,cFile)  
Local nVarWord := 0  
  
OLE_CloseFile(oWord)  
OLE_CloseLink(oWord)  
  
// Inicializa o Ole com o MS-Word 97 ( 8.0 )  
oWord := OLE_CreateLink('TMsOleWord97')  
  
OLE_OpenFile(oWord, cFile)  
  
Return(.T.)
```

**Saiba mais****[Manipulação de arquivos, discos e IO](http://tdn.totvs.com/pages/viewpage.action?pageId=6063692)****[GENERIC - Integração com o Word e copias de arquivo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022751891-MP-ADVPL-GENERIC-INTEGRACAO-COM-O-WORD-E-COPIAS-DE-ARQUIVO?source=search)**
