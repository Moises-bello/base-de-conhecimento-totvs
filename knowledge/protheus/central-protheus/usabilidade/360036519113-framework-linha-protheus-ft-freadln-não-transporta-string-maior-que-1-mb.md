---
article_id: 360036519113
category: Usabilidade
content_hash: ba21be35f2bb896bc91b01b59074fe4b3e3256d6d9dd784e6c410999e427d335
fetched_at: '2026-06-28T22:42:17.236697+00:00'
product: protheus
section_id: 360000076807
source: central-protheus
title: Framework - Linha Protheus - FT_FREADLN() NÃO TRANSPORTA STRING MAIOR QUE 1
  MB
type: support-article
updated_at: '2026-01-26T19:41:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036519113-Framework-Linha-Protheus-FT-FREADLN-N%C3%83O-TRANSPORTA-STRING-MAIOR-QUE-1-MB
---

**OCORRÊNCIA**  
Ao utilizar a função `FT_FReadLn()` para realizar a leitura das linhas de um arquivo .CSV, caso o conteúdo tenha mais que 1 MB, o mesmo está sendo sendo cortado no caractere 1.024.  
  
**AMBIENTE**  
Protheus – ADVPL – A partir da versão 11.8  
  
**CAUSA**  
Devido a uma limitação de memória da função, o transporte de variáveis só ocorre até o 1.024º caractere.  
  
**SOLUÇÃO**  
Utilizar a classe `FwFileReader()` com o método `GetAllLines()`.  
  
**EXEMPLO**

```
// BIBLIOTECAS NESSÁRIAS
#Include "TOTVS.ch"

// BARRA DE SEPARAÇÃO DE DIRETÓRIOS
#Define BAR IIf(IsSrvUnix(), "/", "\")

//------------------------------------------------------
// ABRE UM ARQUIVO .CSV E ORGANIZA POR LINHA
//------------------------------------------------------
User Function T235CSV()
    Local cPath := BAR + "dirdoc" + BAR + "NFSE.csv"
    Local oFile := FwFileReader():New(cPath)
    Local aAux  := {}
    Local aLine := {}
    Local aHead := {}

     // SE FOR POSSÍVEL ABRIR O ARQUIVO, LEIA-O
    // SE NÃO, EXIBA O ERRO DE ABERTURA
    If (oFile:Open())
        aAux := oFile:GetAllLines() // ACESSA TODAS AS LINHAS

        // CRIA O CABEÇALHO E DELETA DO CONJUNTO DE LINHAS
        aHead := StrTokArr2(aAux[1], ";")
        ADel(aAux, 1)
        ASize(aAux, Len(aAux) - 1)

        // SEPARA O VETOR EM NÍVEL CONFORME TOKEN
        AEval(aAux, {|x| AAdd(aLine, StrTokArr2(x, ";", .T.))})
    Else
        Final("Couldn't find/open file: " + cPath)
    EndIf
Return (NIL)
```

**SAIBA MAIS**  
[FRAMEWORK - FWFILEREADER](https://tdn.totvs.com/display/framework/FWFileReader)
