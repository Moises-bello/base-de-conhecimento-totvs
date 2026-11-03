---
article_id: 360024038172
category: ADVPL - Classe e Função
content_hash: 79531e72c927d0fc58a727d499e8a26440bf5a01ac51b32d05f5221f1c841aee
fetched_at: '2026-06-28T22:40:15.699984+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Converter um texto
  para binário
type: support-article
updated_at: '2022-01-05T12:57:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024038172-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Converter-um-texto-para-bin%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**É possível converter um texto para binário incluindo o retorno do carro (*carriage return* | CR | Chr(13)), o salto de linha (*line feed* | LF | Chr(10)) e outros caracteres presentes na tabela ASCII?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Sim, porém será necessário o uso das funções abaixo:

|  |  |
| --- | --- |
| Chr() | Converte um código ASCII para caractere |
| Bin2Str() | Converte uma string com caracteres para uma string com o valor binário |
| StrTran() | Pesquisa e substitui um conjunto de caracteres de uma string |

**Fonte**

```
// BIBLIOTECAS NECESSÁRIAS  
#Include "TOTVS.ch"  
  
// CONSTANTES NECESSÁRIAS  
#Define ENTER  Chr(10) + Chr (13) // SALTO DE LINHA (CARRIAGE RETURN + LINE FEED)  
#Define TAB    Chr(9)             // TABULAÇÃO (TAB)  
#Define BULLET Chr(7)             // TÓPICO (BULLET POINT)  
  
// CENÁRIO PARA CONVERSÃO  
User Function MainFunct()  
    Local cMessage := "LINGUAGENS" + ENTER  
  
    // MONTAGEM DA MENSAGEM  
    cMessage += TAB + BULLET + " ADVPL" + ENTER  
    cMessage += TAB + BULLET + " TL++"  + ENTER  
    cMessage += TAB + BULLET + " 4GL"  
  
    MsgInfo(cMessage)           // VIDE ÁREA "MENSAGEM 01"  
    MsgInfo(Text2Bin(cMessage)) // VIDE ÁREA "MENSAGEM 02"  
Return (NIL)  
  
// CONVERTE UM TEXTO PARA BINÁRIO COM ZERO E UM  
Static Function Text2Bin(cText)  
    Default cText :=""  
  
    // VALIDA O CONTEÚDO ENVIADO  
    If (ValType(cText) == "C" .And. !Empty(cText))  
        cText := StrTran(Bin2Str(cText), Space(1), "0")  
        cText := StrTran(cText, "x", "1")  
    EndIf  
Return (cText)
```

Mensagem 01

```
LINGUAGENS  
     ADVPL   
     TL++   
     4GL
```

Mensagem 02

```
01001100010010010100111001000111010101010100000101000111010001010100111001010011000010100000110100001001000001110010000001000001010001000101011001010000010011000000101000001101000010010000011100100000010101000100110000101011001010110000101000001101000010010000011100100000001101000100011101001100
```

**Saiba mais**[CHR - ASCII para caractere](http://tdn.totvs.com/display/tec/Chr)  
[BIN2STR - String para binário](http://tdn.totvs.com/display/tec/Bin2Str)  
[STRTRAN - Pesquisa e substitui uma string em outra](http://tdn.totvs.com/display/tec/StrTran)
