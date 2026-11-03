---
article_id: 360016599112
category: ADVPL - Ponto de Entrada
content_hash: bc80a94cca98f0598028869c80532e3e5dcc3f1530f950c4f6eedfbe4abf5854
fetched_at: '2026-06-28T22:40:12.962271+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - MATA750: Pontos
  de entrada M750GRIM, M750LCSV e M750VIMP'
type: support-article
updated_at: '2021-12-30T18:28:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016599112-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-MATA750-Pontos-de-entrada-M750GRIM-M750LCSV-e-M750VIMP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como alterar e validar os valores da vindos do arquivo \*.CSV na opção "Importar CSV" da rotina MATA750?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.8  
  
**Solução**Para realizar a alteração dos dados importados pela rotina de Manutenção do Plano Mestre de Produção na opção "Importar CSV", deve-se utilizar os pontos M750LCSV e M750GRIM, contudo para validar os valores, pode ser utilizado o ponto de entrada M750VIMP.  
  
**Exemplo**

```
#Include "TOTVS.ch"  
  
// ALTERA O CONTEÚDO DO CAMPO POR MEIO DOS VALORES  
// FORNECIDOS NA SÉTIMA POSIÇÃO DO PE M750LCSV  
  
User Function M750GRIM()  
    Local aImport := PARAMIXB[1]  
  
    RecLock("SHC", .F.)  
        Replace HC_PRODUTO With aImport[1]  
        Replace HC_QUANT   With aImport[2]  
        Replace HC_DATA    With aImport[3]  
        Replace HC_DOC     With aImport[4]  
        Replace HC_OPC     With aImport[5]  
        Replace HC_MOPC    With aImport[6]  
          
        If (Len(aImport == 7 .And. aImport[7] <> NIL)  
            Replace HC_DOC With aImport[7]  
        EndIf  
    MsUnLock()  
Return (NIL)
```

```
#Include "TOTVS.ch"  
  
// INSERE VALORES QUE PODEM SER MANIPULADOS NA SÉTIMA  
// POSIÇÃO DO VETOR POR MEIO DO PONTO DE ENTRADA M750GRIM  
// CHAMADO UMA VEZ PARA CADA LINHA  
  
User Function M750LCSV()  
    Local cLine    := PARAMIXB[1] // O VALOR DE CCONTEND PODE SER RETIRADO DA LINHA  
    Local cContent := "PMP009"  
Return (cContent)
```

```
#Include "TOTVS.ch"  
  
#Define CRLF Chr(10) + Chr(13)  
  
// VALIDA AS INFORMAÇÕES ANTES DO  
// PONTO DE ENTRADA M750GRIM  
  
User Function M750VIMP()  
    Local aImport  := PARAMIXB[1]  
    Local nPos     := PARAMIXB[2]  
    Local cMessage := ""  
  
    cMessage += "PRODUTO: "    + aImport[nPos][1]             + CRLF  
    cMessage += "QUANTIDADE: " + CValToChar(aImport[nPos][2]) + CRLF  
    cMessage += "DATA: "       + CValToChar(aImport[nPos][3]) + CRLF  
    cMessage += "DOCUMENTO: "  + aImport[nPos][4]             + CRLF  
    cMessage += "OPCIONAL "    + aImport[nPos][5]  
  
    If (Len(aImport[nPos]) == 6 .And. aImport[nPos][6] <> NIL)  
        cMessage += "" + CRLF + "M750LCSV: " + aImport[nPos][6]  
    EndIf  
Return (MsgYesNo(cMessage, "Deseja importar o registro?"))
```

**Exemplo**[EVID\_MATA750.7Z](https://totvssuporte.zendesk.com/attachments/token/RlsbyCDQJODMC70lDrrDqnxeT/?name=VALIDA%C3%87%C3%83O+E+ALTERAR+DE+DADOS+NA+IMPORTA%C3%87%C3%83O+DE+CSV.7z) **Saiba mais**[M750LCSV - LEITURA DE COLUNAS](http://tdn.totvs.com/display/PROT/M750LCSV+-+Leitura+de+Colunas)  
[M750GRIM - GRAVAÇÃO DE CAMPOS](http://tdn.totvs.com/pages/viewpage.action?pageId=6089370)  
[M750VIMP - VALIDA GERAÇÃO DE PMP](http://tdn.totvs.com/pages/viewpage.action?pageId=321291675)
