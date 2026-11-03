---
article_id: 8664015704471
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 0be32578583ed2016cfaf2bd80aa7e6e2b5a4f3d2c2fcbb0df9914d05634c6c4
fetched_at: '2026-06-28T22:38:32.740220+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - EXECAUTO FATA300
type: support-article
updated_at: '2022-09-05T17:37:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8664015704471-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-EXECAUTO-FATA300
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do **Execauto FATA300 - Oportunidade de Vendas.**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**Função utilizada para geração de Oportunidade de Venda via rotina automática (ExecAuto).  
  
**Exemplo**

```
#Include "Protheus.ch"  
  
User Function MyFATA300()  
  
    Local aCabec        := {}  
    Local lRet          := .T.  
    Local lTodosSim     := .F.  
    Private lMsErroAuto := .F.  
  
    dbSelectArea("AD1")  
    dbSetOrder(1)  
  
    ConOut("Teste de Inclusao de Oportunidade")  
    ConOut("Inicio: " + Time())  
    ConOut("Montando o array do cabecalho")  
  
    If !dbSeek(xFilial("AD1")+"000001"+"02")  
    // Monta o array com as informacoes para a gravacao  
        aCabec := {{ "AD1_FILIAL"  ,""                    ,NIL },;  
                   { "AD1_NROPOR"  ,"000001"              ,NIL },;  //Numero da Oportunidade  
                   { "AD1_REVISA"  ,"01"                  ,NIL },;  
                   { "AD1_DESCRI"  ,"TESTE DE ROT AUTOM"  ,NIL },;  
                   { "AD1_DATA  "  ,DATE()                ,NIL },;  
                   { "AD1_HORA  "  ,SUBSTR(TIME(),1,5)    ,NIL },;  
                   { "AD1_USER  "  ,"000000"              ,NIL },;  
                   { "AD1_VEND  "  ,"000001"              ,NIL },;  
                   { "AD1_DTINI "  ,DATE()                ,NIL },;  
                   { "AD1_PROSPE"  ,""                    ,NIL },;  
                   { "AD1_LOJPRO"  ,""                    ,NIL },;  
                   { "AD1_CODCLI"  ,"000001"              ,NIL },;  
                   { "AD1_LOJCLI"  ,"01"                  ,NIL },;  
                   { "AD1_PROVEN"  ,"000001"              ,NIL },;  
                   { "AD1_STAGE "  ,"000001"              ,NIL },;  
                   { "AD1_MOEDA "  ,1                     ,NIL },;  
                   { "AD1_PRIOR "  ,"1"                   ,NIL }}         
    EndIf      
  
    lTodosSim := ApMsgNoYes('Confirma a acao [Sim p/Todos]?')  
  
    //ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿//³Gravacao da oportunidade³//ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ  
  
    If lTodosSim  
        ConOut("Iniciando a gravacao")  
        MSExecAuto({|x,y|FATA300(x,y)},3,aCabec)  
  
        If lMsErroAuto  
            Conout('Erro ao cadastrar Oportunidade!')  
            DisarmTransaction()  
            MostraErro()  
            lRet := .F.  
        Else  
            Conout('Oportunidade cadastrada com Sucesso!')  
            lRet := .T.  
        EndIf  
  
        ConOut("Fim: " + Time())  
    EndIf  
  
Return lRet
```

 **Saiba Mais: [Execauto FATA300 - Oportunidade de Vendas](https://tdn.totvs.com/x/DYRn)**
