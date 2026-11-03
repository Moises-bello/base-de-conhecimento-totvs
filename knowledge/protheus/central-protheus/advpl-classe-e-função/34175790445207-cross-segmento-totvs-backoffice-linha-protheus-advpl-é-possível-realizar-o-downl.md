---
article_id: 34175790445207
category: ADVPL - Classe e Função
content_hash: b4ebcb79359a0920f354bf2ffdb54ba68f37331965c92a8132b72203dad005ca
fetched_at: '2026-06-28T22:40:20.701646+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - É possível realizar
  o download em chunks de um arquivo grande?
type: support-article
updated_at: '2025-08-20T17:21:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34175790445207-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-%C3%89-poss%C3%ADvel-realizar-o-download-em-chunks-de-um-arquivo-grande
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34175790432023) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
É possível realizar um download em partes (*chunks*) de um arquivo grande?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – Todas as versões  
  
**Solução**

Um download em partes (*chunks)* é uma técnica onde um arquivo grande é dividido em partes para formar o arquivo completo. Atualmente o Protheus possui uma limitação em requisições definida pela chave [MAXSTRINGSIZE](https://tdn.totvs.com/pages/viewpage.action?pageId=161349793); entretanto é possível dividir o download em partes usando headers `Range` (se o servidor suportar).

**Exemplo:**

```
#include "protheus.ch"

/*/{Protheus.doc} DRange
Função para download de grandes arquivos em chunks com limite de tamanho
@author Evandro Narciso
@since data
@version 1.2
@param nMaxSizeMB Numérico - Tamanho máximo em MB (opcional)
@return logical .T. se sucesso, .F. se erro
/*/

User Function DRange(nMaxSizeMB)

Default nMaxSizeMB:=45

Local cLocalFile := ""
Local cUrl := "http://arquivos.receitafederal.gov.br/dados/cnpj/dados_abertos_cnpj/2025-07/Empresas0.zip"
Local nChunkSize := 1024 * 1024 // 1 MB
Local nStart := 0, nEnd := nChunkSize - 1
Local cBuffer := "", nHandle := 0, lConcluido := .F.
Local aHeaders := {"User-Agent: Mozilla/5.0 (Protheus)"}
Local cHeaderRet := "", nAttempt := 1, nMaxAttempts := 3
Local nFileSize := 0, nTotalRead := 0
Local nMaxBytes

nMaxBytes := If(nMaxSizeMB == Nil, Nil, nMaxSizeMB * 1024 * 1024)

// Nome do arquivo com timestamp
cLocalFile := "\dirdoc\" + StrTran(DToS(Date()) + "_" + StrTran(Time(), ":") + "_DOCUMENT.zip", " ", "_")

nHandle := FCreate(cLocalFile)
If nHandle == -1
    ConOut("Erro ao criar arquivo: " + cLocalFile + " - " + ErrorMsg())
    Return .F.
EndIf

// Loop principal de download
While !lConcluido .and. nAttempt <= nMaxAttempts
    // Verifica limite máximo (se definido)
    If nMaxBytes != Nil .and. nTotalRead >= nMaxBytes
        ConOut("Limite de " + cValToChar(nMaxSizeMB) + " MB atingido")
        lConcluido := .T.
        Exit
    EndIf
    
    // Ajusta o final do chunk para não ultrapassar o limite
    If nMaxBytes != Nil .and. (nEnd - nStart + 1) > (nMaxBytes - nTotalRead)
        nEnd := nStart + (nMaxBytes - nTotalRead) - 1
    EndIf
    
    // Configura Range
    aAdd(aHeaders, "Range:bytes=" + AllTrim(Str(nStart)) + "-" + AllTrim(Str(nEnd)))
    
    // Tentativa com tratamento de timeout
    Begin Sequence
        cBuffer := HTTPGet(cUrl, "", 60, aHeaders, @cHeaderRet)
    Recover
        cBuffer := ""
        ConOut("Timeout na tentativa " + cValToChar(nAttempt))
    End Sequence
    
    // Verifica condições de término
    If Empty(cBuffer)
        If nAttempt < nMaxAttempts
            nAttempt++
            ConOut("Tentando novamente (" + cValToChar(nAttempt) + "/" + cValToChar(nMaxAttempts) + ")")
            Loop
        Else
            ConOut("Falha após " + cValToChar(nMaxAttempts) + " tentativas")
            lConcluido := .T.
        EndIf
    ElseIf "416 Range Not Satisfiable" $ cHeaderRet .or. Len(cBuffer) < nChunkSize
        lConcluido := .T.
        FWrite(nHandle, cBuffer) // Grava último chunk
        nTotalRead += Len(cBuffer)
    Else
        If FWrite(nHandle, cBuffer) != Len(cBuffer)
            ConOut("Erro ao gravar chunk no arquivo")
            lConcluido := .T.
        Else
            nTotalRead += Len(cBuffer)
            nStart := nEnd + 1
            nEnd += nChunkSize
            
            // Progresso em MB com limite (se aplicável)
            ConOut("Baixados: " + Str(nTotalRead/1024/1024, 10, 2) + " MB" + ;
                  If(nMaxBytes != Nil, " de " + cValToChar(nMaxSizeMB) + " MB máximo", ""))
        EndIf
    EndIf
    
    // Remove header Range para próxima iteração
    If Len(aHeaders) > 1
        aSize(aHeaders, Len(aHeaders)-1)
    EndIf
EndDo

FClose(nHandle)

If nTotalRead == 0
    FErase(cLocalFile)
    Return .F.
EndIf

ConOut("Download concluído: " + cLocalFile + " - Tamanho: " + Str(nTotalRead/1024/1024, 10, 2) + " MB" + ;
      If(nMaxBytes != Nil, " (Limite: " + cValToChar(nMaxSizeMB) + " MB)", ""))

Return .T.
```

**Saiba mais**  
[**MAXSTRINGSIZE**](https://tdn.totvs.com/pages/viewpage.action?pageId=161349793)  
[**HttpGet**](https://tdn.totvs.com/display/tec/HTTPGet)
