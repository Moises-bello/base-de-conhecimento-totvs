---
article_id: 14865980636951
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: dfeac8c113c2cf02fc474f5a85f454a66afd6b2b9a1c7e0d1b42b25aca133ed8
fetched_at: '2026-06-28T22:38:45.239253+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - EXECAUTO CTBANFS
type: support-article
updated_at: '2023-05-26T13:45:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14865980636951-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-EXECAUTO-CTBANFS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do **Execauto CTBANFS - Contabilização Offline dos Documentos Fiscais de Saída (ExecAuto).**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**Rotina de processamento da contabilização offline dos Documentos de Saída.  
  
**Exemplo**

```
#INCLUDE 'PROTHEUS.CH'  
#INCLUDE 'TOTVS.CH'  
#INCLUDE "TBICONN.CH"  
  
User Function CTBAXFUN()  
  
    Local aParam:= {}  
    Private lMsErroAuto := .F.  
  
    //ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿  
    //³ mv_par01 - Mostra Lancamentos Contabeis ? Sim Nao ³  
    //³ mv_par02 - Aglutina Lancamentos ? Sim Nao ³  
    //³ mv_par03 - Gerar Lancamentos Por ? NF Periodo Dia ³  
    //³ mv_par04 - Contabiliza C.M.V. ? Sim Nao ³  
    //³ mv_par05 - Data Inicial ³  
    //³ mv_par06 - Data Final ³  
    //³ mv_par07 - Da Filial ³  
    //³ mv_par08 - At‚ a Filial ³  
    //³ mv_par09 - Contabiliza Notas de Credito ? Sim Nao ³  
    //ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ  
  
    //ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿  
    //³Preparando o ambiente para execucao ³  
    //ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ  
  
    ConOut(Repl("-",80))  
    ConOut(PadC("Teste de Lancamento Contabil",80))  
  
    PREPARE ENVIRONMENT EMPRESA "99" FILIAL "01" //USER "ADMIN" PASSWORD "" TABLES "SF2" MODULO "FAT"  
  
        aAdd(aParam,(1))        //Mostra Lancamentos Contabeis? 1-Sim / 2-Nao  
        aAdd(aParam,(2))        //Aglutina Lancamentos? 1-Sim / 2-Nao  
        aAdd(aParam,(1))        //Gerar Lancamentos Por? 1-Documento / 2-Periodo / 3-Dia  
        aAdd(aParam,(2))        //Contabiliza Custo On-Line? 1-Sim / 2-Nao  
        aAdd(aParam,(DATE()))   //Data Inicial  
        aAdd(aParam,(DATE()))   //Data Final  
        aAdd(aParam,(" "))      //Da Filial  
        aAdd(aParam,("99"))     //Ate a Filial  
        aAdd(aParam,(2))        //Contabiliza Notas de Credito? 1-Sim / 2-Nao  
  
        CTBANFS(aParam)  
  
        If !lMsErroAuto  
            ConOut("Incluido com sucesso! ")  
        Else  
            ConOut("Erro na inclusao!")  
        EndIf  
  
        ConOut(Repl("-",80))  
  
    RESET ENVIRONMENT  
  
Return
```

**Saiba Mais**

**[CTBANFS - Contabilização Offline dos Documentos Fiscais de Saída (ExecAuto)](https://tdn.totvs.com/x/rITaAw)**
