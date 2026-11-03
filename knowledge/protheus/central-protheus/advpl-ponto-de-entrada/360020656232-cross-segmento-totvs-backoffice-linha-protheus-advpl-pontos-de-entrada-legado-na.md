---
article_id: 360020656232
category: ADVPL - Ponto de Entrada
content_hash: e40ac01f8b80ce8744dfc32a2a40070a1b493b60f51d316529504217edfb892b
fetched_at: '2026-06-28T22:40:12.794679+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Pontos de entrada
  legado na Fina460
type: support-article
updated_at: '2023-06-26T21:47:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020656232-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Pontos-de-entrada-legado-na-Fina460
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:05:00 min  
  
Ocorrência**Os pontos de entrada abaixo não estão funcionando na rotina FINA460.

* A460VALLIN: Executado na inclusão de linhas de parcelas da liquidação a receber;
* F460BOT: Executado para inclusão de botões no botão Ações Relacionadas da liquidação a receber;
* F460CAN: Executado no cancelamento da tela de geração de liquidação a receber;
* F460CON: Executado no cancelamento da tela de geração de liquidação a receber;
* F460GRV: Executado após a gravação de dados da geração de liquidação a receber;
* F460SAID: Executado no cancelamento da tela de geração de liquidação a receber;
* F460TOK: Executado na validação de toda tela de geração de liquidação a receber;
* FA460CON: Executado na confirmação da tela de geração de liquidação a receber;
* FA460LOK: Executado na validação da linha de parcelas da liquidação a receber.

**Obs**: O nome do fonte ( .prw) não pode ser o mesmo da rotina ( FINA460A.prw)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus – ADVPL – A partir da versão 12.1.17  
  
**Causa**  
Os pontos acima citados foram descontinuados da rotina FINA460 por motivo de que ponto de entrada FINA460A (padrão MVC) conter todos os momentos aos quais os pontos tratavam.  
  
**Solução**Utilizar o ponto de entrada MVC FINA460A.

```
User Function FINA460A()  
  
Local aParam := PARAMIXB  
Local xRet := .T.  
Local oObj := ''  
Local cIdPonto := ''  
Local cIdModel := ''  
Local nLinha := 0  
Local nQtdLinhas:= 0  
Local cMsg := ''  
Local cClasse := ""  
  
If aParam <> NIL  
    oObj := aParam[1]  
    cIdPonto := aParam[2]  
    cIdModel := aParam[3]  
  
    If cIdPonto == 'MODELPOS' // Bloco substitui o ponto de entrada F460TOK e FA460CON  
        cMsg := 'Chamada na validação total do formulário (MODELPOS).' + CRLF  
        cMsg += 'ID ' + cIdModel + CRLF  
        If cClasse == 'FWFORMGRID' // Bloco substitui o ponto de entrada FA460LOK, validação do Grid, utilizar o ID de Model 'TITGERFO2'  
            nQtdLinhas := oObj:Length()  
             nLinha := oObj:GetLine()  
  
            cMsg += 'É um FORMGRID com ' + Alltrim( Str( nQtdLinhas ) ) + ' linha(s).' + CRLF  
            cMsg += 'Posicionado na linha ' + Alltrim( Str( nLinha ) ) + CRLF  
  
        EndIf  
  
        If !( xRet := ApMsgYesNo( cMsg + 'Continua ?' ) )  
            Help( ,, 'Help',, 'O MODELPOS retornou .F.', 1, 0 )  
        EndIf  
    ElseIf cIdPonto == 'MODELCANCEL' // Bloco substitui os pontos de entrada F460CAN, F460CON e F460SAID no cancelamento da tela de geração de liquidação.  
        cMsg := 'Chamada no Botão Cancelar (MODELCANCEL).' + CRLF + 'Deseja Realmente Sair ?'  
        If !( xRet := ApMsgYesNo( cMsg ) )  
            Help( ,, 'Help',, 'O MODELCANCEL retornou .F.', 1, 0 )  
        EndIf  
    ElseIf cIdPonto == 'FORMLINEPRE' // Bloco substitui o ponto de entrada A460VALLIN.  
        If cIdModel == 'TITGERFO2'  
            nQtdLinhas := oObj:Length()  
            nLinha := oObj:GetLine()  
            If aParam[5] == 'DELETE' // Deleção de Linha do Grid  
                cMsg := 'Chamada na pre validação da linha do formulário (FORMLINEPRE).' + CRLF  
                cMsg += 'Onde esta se tentando deletar uma linha' + CRLF  
                cMsg += 'É um FORMGRID com ' + Alltrim( Str( nQtdLinhas ) ) + ' linha(s).' + CRLF  
                cMsg += 'Posicionado na linha ' + Alltrim( Str( nLinha ) ) + CRLF  
                cMsg += 'ID ' + cIdModel + CRLF  
  
                If !( xRet := ApMsgYesNo( cMsg + 'Continua ?' ) )  
                    Help( ,, 'Help',, 'O FORMLINEPRE retornou .F.', 1, 0 )  
                EndIf  
            EndIf  
        EndIf  
    ElseIf cIdPonto == 'FORMLINEPOS' // Substitui o ponto de entrada FA460LOK  
        If cIdModel == 'TITGERFO2'  
            nQtdLinhas := oObj:Length()  
            nLinha := oObj:GetLine()  
            cMsg := 'Chamada na validação da linha do formulário (FORMLINEPOS).' + CRLF  
            cMsg += 'ID ' + cIdModel + CRLF  
            cMsg += 'É um FORMGRID com ' + Alltrim( Str( nQtdLinhas ) ) + ' linha(s).' + CRLF  
            cMsg += 'Posicionado na linha ' + Alltrim( Str( nLinha ) ) + CRLF  
  
            If !( xRet := ApMsgYesNo( cMsg + 'Continua ?' ) )  
                Help( ,, 'Help',, 'O FORMLINEPOS retornou .F.', 1, 0 )  
            EndIf  
        EndIf  
    ElseIf cIdPonto == 'MODELCOMMITNTTS' // Bloco substitui o ponto de entrada F460GRV.  
        ApMsgInfo('Chamada apos a gravação total do modelo e fora da transação (MODELCOMMITNTTS).' + CRLF + 'ID ' + cIdModel)  
    ElseIf cIdPonto == 'BUTTONBAR' // Bloco substitui o ponto de entrada F460BOT.  
        ApMsgInfo('Adicionando Botao na Barra de Botoes (BUTTONBAR).' + CRLF + 'ID ' + cIdModel )  
        xRet := { {'Salvar', 'SALVAR', { || Alert( 'Salvou' ) }, 'Este botao Salva' } }  
    EndIf  
EndIf  
  
Return xRet
```

**Saiba mais**  
[Ponto de Entrada Padrão do MVC](http://tdn.totvs.com/pages/viewpage.action?pageId=208345968)
