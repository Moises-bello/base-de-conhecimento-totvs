---
article_id: 360040696874
category: ADVPL - Relatório
content_hash: 97f20cd2f5212c36e1323800d6adb3d11dfd373f94019b01e4e2e28eebaf7080
fetched_at: '2026-06-28T22:40:22.817375+00:00'
product: protheus
section_id: 1500001549062
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Envio de relatório
  TReport via e-mail em formato planilha
type: support-article
updated_at: '2023-01-06T20:00:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040696874-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Envio-de-relat%C3%B3rio-TReport-via-e-mail-em-formato-planilha
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Assim como por meio da interface gráfica é possível fazer o envio de um relatório via e-mail em formato planilha, é possível fazê-lo apenas utilizando a classe `TReport()`?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus – ADVPL – A partir da versão 12.1.17  
  
**Solução**

1. Atribua a propriedade `lExcelByEmail` com valor `.T.`
2. Defina um nome para o arquivo com a propriedade `cFile`
3. Utilize o método `Print()` com conteúdo `.F.`
4. Informe a constante `IMP_EXCEL` no método `SetDevice()`
5. Adicione um ou mais e-mails (separado por ponto e vírgula) na propriedade `cEmail`

**Exemplo**

```
// BIBLIOTECAS NECESSÁRIAS  
#Include "TOTVS.ch"  
#Include "REPORT.ch"  
  
// SIMULA A EXECUÇÃO VIA JOB  
User Function T248START()  
    StartJob("U_T248XMLRPT", GetEnvServer(), .T.)  
Return (NIL)  
  
// FUNÇÃO PRINCIPAL  
User Function T248XMLRPT()  
    Local oReport := NIL // OBJETO TREPORT  
    Local oSA1    := NIL // SEÇÃO SA1  
    Local oBreak  := NIL // QUEBRA DE PÁGINA  
  
    RPCSetEnv("99", "01", /*cUserId*/, /*cPasswd*/, "FIN") // PREPARAÇÃO DE AMBIENTE (COMENTAR SE VIA GUI)  
        // INSTANCIAÇÃO DE VARIÁVEL OREPORT  
        DEFINE REPORT oReport NAME "REPORT1" TITLE "Relatorio de Clientes" PARAMETER "REPORT" ACTION {|oReport| PrintReport(oReport)}  
  
        // DEFINIÇÃO DA SEÇÃO OSA1  
        DEFINE SECTION oSA1 OF oReport TITLE "Cliente" TABLES "SA1"  
            DEFINE CELL NAME "A1_COD"  OF oSA1 ALIAS "SA1"  
            DEFINE CELL NAME "A1_NOME" OF oSA1 ALIAS "SA1"  
            DEFINE CELL NAME "A1_VEND" OF oSA1 ALIAS "SA1"  
        DEFINE BREAK oBreak OF oSA1 WHEN oSA1:Cell("A1_VEND")  
  
        DEFINE FUNCTION FROM oSA1:Cell("A1_COD") FUNCTION COUNT BREAK oBreak  
  
        oReport:nRemoteType   := NO_REMOTE  
        oReport:lExcelByEmail := .T.  
        oReport:cEmail        := "guilherme.bigois@totvs.com.br"  
        oReport:cFile         := "RELATORIO"  
  
        oReport:SetDevice(IMP_EXCEL)  
        oReport:SetPreview(.F.)  
        oReport:Print(.F.)  
    RPCClearEnv() // ENCERRRA AMBIENTE (COMENTAR SE VIA GUI)  
Return (NIL)  
  
// DADOS DE EXIBIÇÃO  
Static Function PrintReport(oReport)  
    Local cAlias := Space(0) // ALIAS TEMPORÁRIO  
  
    // SE AMBIENTE IGUAL A TOPCONNECT  
    #IFDEF TOP  
        cAlias := GetNextAlias() // RECUPERA O PRÓXIMO ALIAS TEMPORÁRIO DO SISTEMA  
        MakeSQLExp("REPORT")  
  
        // INICIA QUERY PARA RETORNO DE DADOS  
        BEGIN REPORT QUERY oReport:Section(1)  
            BEGINSQL ALIAS cAlias  
                SELECT A1_COD, A1_NOME, A1_VEND  
                FROM %Table:SA1% SA1  
                WHERE A1_FILIAL = %XFilial:SA1% AND SA1.%NotDel%  
                ORDER BY A1_FILIAL, A1_VEND  
            ENDSQL  
        END REPORT QUERY oReport:Section(1)  
  
        oReport:Section(1):Print(.F.)  
    #ENDIF  
Return (NIL)
```

**Saiba mais**  
[TReport](https://tdn.totvs.com/display/public/PROT/TReport)
