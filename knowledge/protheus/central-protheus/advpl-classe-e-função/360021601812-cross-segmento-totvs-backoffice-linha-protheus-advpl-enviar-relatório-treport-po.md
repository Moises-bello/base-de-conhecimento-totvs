---
article_id: 360021601812
category: ADVPL - Classe e Função
content_hash: 76ab2685c8af8c539e166815351dcac9ac0c4dbdc3b2b87d14e66f6f255b2767
fetched_at: '2026-06-28T22:40:15.790106+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Enviar relatório
  TReport por e-mail
type: support-article
updated_at: '2021-08-02T17:21:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021601812-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Enviar-relat%C3%B3rio-TReport-por-e-mail
---

**Dúvida**É possível enviar um relatório um por e-mail utilizando a classe TReport()?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.8  
  
**Solução**Não, somente é possível realizar o envio do relatório por e-mail.  
  
**Fonte**

```
// BIBLIOTECAS NECESSÁRIAS  
#Include "TOTVS.ch"  
#Include "REPORT.ch"  
#Include "TBICONN.CH"  
  
// SIMULA A EXECUÇÃO VIA JOB  
User Function T153START()  
    StartJob("U_T153RPTMAIL", GetEnvServer(), .T.)  
Return (NIL)  
  
// FUNÇÃO PRINCIPAL  
User Function T153RPTMAIL()  
    Local oReport := NIL // OBJETO TREPORT  
    Local oBreak  := NIL // QUEBRA DE PÁGINA  
    Local oSA1    := NIL // SEÇÃO SA1  
  
    RPCSetEnv("99", "01", /*cUserId*/, /*cPasswd*/ , "FIN") // PREPARAÇÃO DE AMBIENTE (COMENTAR SE VIA GUI)  
        // INSTANCIAÇÃO DE VARIÁVEL OREPORT  
        DEFINE REPORT oReport NAME "REPORT1" TITLE "Relatorio de Clientes" PARAMETER "REPORT" ACTION {|oReport| PrintReport(oReport)}  
  
        // DEFINIÇÃO DA SEÇÃO OSA1  
        DEFINE SECTION oSA1 OF oReport TITLE "Cliente" TABLES "SA1"  
            DEFINE CELL NAME "A1_COD"  OF oSA1 ALIAS "SA1"  
            DEFINE CELL NAME "A1_NOME" OF oSA1 ALIAS "SA1"  
            DEFINE CELL NAME "A1_VEND" OF oSA1 ALIAS "SA1"  
        DEFINE BREAK oBreak OF oSA1 WHEN oSA1:Cell("A1_VEND")  
  
        DEFINE FUNCTION FROM oSA1:Cell("A1_COD") FUNCTION COUNT BREAK oBreak  
  
        oReport:nRemoteType := NO_REMOTE        // FORMA DE GERAÇÃO DO RELATÓRIO  
        oReport:nDevice     := 8                // ENVIO DE .PDF VIA E-MAIL  
        oReport:cEmail      := "SEU EMAIL AQUI" // DESTINATÁRIO  
  
        oReport:SetReportPortal("cRptPortal") // DEFINE O NOME DO RELATÓRIO  
        oReport:Print()  
    RPCClearEnv() // ENCERRRA AMBIENTE (COMENTAR SE VIA GUI)  
Return (NIL)  
  
// DADOS DE EXIBIÇÃO  
Static Function PrintReport(oReport)  
    Local cAlias := "" // ALIAS TEMPORÁRIO  
  
    // SE AMBIENTE IGUAL A TOPCONNECT  
    #IFDEF TOP  
        cAlias := GetNextAlias() // RECUPERA O PRÓXIMO ALIAS TEMPORÁRIO DO SISTEMA  
        MakeSQLExp("REPORT")  
  
        // INICIA QUERY PARA RETORNO DE DADOS  
        BEGIN REPORT QUERY oReport:Section(1)  
            BEGINSQL ALIAS cAlias  
                SELECT A1_COD, A1_NOME, A1_VEND  
                FROM %Table:SA1% SA1  
                WHERE A1_FILIAL = %XFilial:SA1% AND SA1.%NotDel%  
                ORDER BY A1_FILIAL, A1_VEND  
            ENDSQL  
        END REPORT QUERY oReport:Section(1)  
  
        oReport:Section(1):Print(.F.)  
    #ENDIF  
Return (NIL)
```

**Saiba Mais**

[MP - ADVPL - Salvar relatório Treport .PDF em diretório](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049503954-MP-ADVPL-Salvar-relat%C3%B3rio-Treport-PDF-em-diret%C3%B3rio?source=search)[TReport](https://tdn.totvs.com/display/public/PROT/TReport)
