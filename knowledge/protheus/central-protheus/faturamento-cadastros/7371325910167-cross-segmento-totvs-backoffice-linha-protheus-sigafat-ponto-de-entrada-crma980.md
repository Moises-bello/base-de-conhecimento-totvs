---
article_id: 7371325910167
category: Faturamento - Cadastros
content_hash: 8f1f98a8bd7817b0e4fbb17ba0c1c312d3f4d719840579d83454692f0313fc8d
fetched_at: '2026-06-28T22:38:36.602540+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ponto de Entrada
  CRMA980 - BUTTONBAR
type: support-article
updated_at: '2022-07-22T18:38:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7371325910167-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-CRMA980-BUTTONBAR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do Ponto de Entrada **CRMA980 - BUTTONBAR**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**O retorno do Ponto de Entrada **CRMA980** irá depender de qual **ID** estará sendo executado no momento, nesse exemplo iremos utilizar o **ID** **BUTTONBAR** que permite ao usuário adicionar botões à barra no topo da tela.  
  
**Obs.:** O nome do arquivo não poderá ser **CRMA980.PRW**, utilize por exemplo **MYCRMA980.PRW**.  
  
**Exemplo:**

```
#INCLUDE "PROTHEUS.CH"  
#INCLUDE "FWMVCDEF.CH"  
  
Static __LogTela    := NIL  
  
User Function CRMA980() ///cXXX1,cXXX2,cXXX3,cXXX4,cXXX5,cXXX6  
  
    Local aParam        := PARAMIXB  
    Local xRet          := .T.  
    Local lIsGrid       := .F.  
    Local cIDPonto      := ''  
    Local cIDModel      := ''  
    Local oObj          := NIL  
  
    If __LogTela == NIL  
        __LogTela   := ApMsgYesNo("A geracao do 'LOG de processamento' dos PE 'CRMA980' (MVC) sera exibido em TELA?" + CRLF + CRLF +;  
            'SIM = TELA' + CRLF +;  
            'NAO = CONSOLE do AppServer')  
    EndIf  
  
    If aParam <> NIL  
        oObj        := aParam[1]  
        cIDPonto    := aParam[2]  
        cIDModel    := aParam[3]  
        lIsGrid     := (Len(aParam) > 3)  
        nOperation := oObj:GetOperation()  
  
        If cIDPonto == 'BUTTONBAR'  
            ApMsgInfo("Adicionando um botao na barra de botoes da rotina (PE '" + cIDPonto + "')." + CRLF +;  
                    "ID '" + cIDModel + "'")   
  
            xRet    := {{'TITULO DO BOTAO',;                               //Titulo para o botao  
                        'SALVAR',;                                         //Nome do Bitmap para exibicao  
                        {|| Alert('Executou uma rotina especifica!')},;    //CodeBlock a ser executado  
                        'Este botao executa uma rotina especifica.'}}      //ToolTip (Opcional)  
        EndIf       
    
    EndIf  
  
Return xRet
```

**Saiba Mais: [PE CRMA980 - Pontos de Entrada do Cadastro de Clientes (MVC)](https://tdn.totvs.com/x/-rO6J)**
