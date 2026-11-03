---
article_id: 360051138234
category: ADVPL - Ponto de Entrada
content_hash: f4282c9383c18b6aa2983f5a7ef116e30f776521666f689e58e379d0d5b1924d
fetched_at: '2026-06-28T22:40:11.745281+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Manutenção de Contratos:Ponto
  de entrada MVC
type: support-article
updated_at: '2021-12-29T13:05:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051138234-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Manuten%C3%A7%C3%A3o-de-Contratos-Ponto-de-entrada-MVC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Tem um exemplo do ponto de entrada MVC para o CNTA300?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – Todas versões  
  
**Solução**

```
#include 'protheus.ch'  
#include 'parmtype.ch'  
  
User Function CNTA300()  
  
Local aParam     := PARAMIXB  
Local xRet       := .T.  
Local oObj       := ''  
Local cIdPonto   := ''  
Local cIdModel   := ''  
Local lIsGrid    := .F.  
Local cClasse := ""  
Local nLinha     := 0  
Local nQtdLinhas := 0  
Local cMsg       := ''  
  
If aParam <> NIL  
           
       oObj       := aParam[1]  
       cIdPonto   := aParam[2]  
       cIdModel   := aParam[3]  
       lIsGrid    := ( Len( aParam ) > 3 )  
  
       If     cIdPonto == 'MODELPOS'  
  
             cMsg := 'Chamada na validação total do modelo (MODELPOS).' + CRLF  
             cMsg += 'ID ' + cIdModel + CRLF              
  
             If !( xRet := ApMsgYesNo( cMsg + 'Continua ?' ) )  
                    Help( ,, 'Help',, 'O MODELPOS retornou .F.', 1, 0 )  
             EndIf  
  
              
  
       ElseIf cIdPonto == 'FORMPOS'  
  
             cMsg := 'Chamada na validação total do formulário (FORMPOS).' + CRLF  
             cMsg += 'ID ' + cIdModel + CRLF              
  
             If      cClasse == 'FWFORMGRID'  
                    cMsg += 'É um FORMGRID com ' + Alltrim( Str( nQtdLinhas ) ) + ;  
'     linha(s).' + CRLF  
cMsg += 'Posicionado na linha ' + Alltrim( Str( nLinha     ) ) + CRLF  
  
             ElseIf cClasse == 'FWFORMFIELD'  
                    cMsg += 'É um FORMFIELD' + CRLF  
             EndIf  
           
             If !( xRet := ApMsgYesNo( cMsg + 'Continua ?' ) )  
                    Help( ,, 'Help',, 'O FORMPOS retornou .F.', 1, 0 )  
             EndIf         
  
       ElseIf cIdPonto == 'FORMLINEPRE'  
  
             If aParam[5] == 'DELETE'  
cMsg := 'Chamada na pre validação da linha do formulário (FORMLINEPRE).' + CRLF  
                    cMsg += 'Onde esta se tentando deletar uma linha' + CRLF  
                    cMsg += 'É um FORMGRID com ' + Alltrim( Str( nQtdLinhas ) ) +;  
' linha(s).' + CRLF  
cMsg += 'Posicionado na linha ' + Alltrim( Str( nLinha     ) ) + CRLF  
                    cMsg += 'ID ' + cIdModel + CRLF  
                   
                    If !( xRet := ApMsgYesNo( cMsg + 'Continua ?' ) )  
                           Help( ,, 'Help',, 'O FORMLINEPRE retornou .F.', 1, 0 )  
                    EndIf  
             EndIf  
            
       ElseIf cIdPonto == 'FORMLINEPOS'  
  
cMsg := 'Chamada na validação da linha do formulário (FORMLINEPOS).' + CRLF  
             cMsg += 'ID ' + cIdModel + CRLF  
             cMsg += 'É um FORMGRID com ' + Alltrim( Str( nQtdLinhas ) ) + ;  
' linha(s).' + CRLF  
             cMsg += 'Posicionado na linha ' + Alltrim( Str( nLinha     ) ) + CRLF              
  
             If !( xRet := ApMsgYesNo( cMsg + 'Continua ?' ) )  
                    Help( ,, 'Help',, 'O FORMLINEPOS retornou .F.', 1, 0 )  
             EndIf  
            
       ElseIf cIdPonto == 'MODELCOMMITTTS'  
ApMsgInfo('Chamada apos a gravação total do modelo e dentro da transação (MODELCOMMITTTS).' + CRLF + 'ID ' + cIdModel )  
         
       ElseIf cIdPonto == 'MODELCOMMITNTTS'  
ApMsgInfo('Chamada apos a gravação total do modelo e fora da transação (MODELCOMMITNTTS).' + CRLF + 'ID ' + cIdModel)  
       
             //ElseIf cIdPonto == 'FORMCOMMITTTSPRE'           
  
       ElseIf cIdPonto == 'FORMCOMMITTTSPOS'  
  
ApMsgInfo('Chamada apos a gravação da tabela do formulário (FORMCOMMITTTSPOS).' + CRLF + 'ID ' + cIdModel)  
           
       ElseIf cIdPonto == 'MODELCANCEL'  
  
cMsg := 'Chamada no Botão Cancelar (MODELCANCEL).' + CRLF + 'Deseja Realmente Sair ?'  
           
             If !( xRet := ApMsgYesNo( cMsg ) )  
                    Help( ,, 'Help',, 'O MODELCANCEL retornou .F.', 1, 0 )  
             EndIf  
            
       ElseIf cIdPonto == 'BUTTONBAR'  
  
ApMsgInfo('Adicionando Botao na Barra de Botoes (BUTTONBAR).' + CRLF + 'ID ' + cIdModel )  
  
xRet := { {'Salvar', 'SALVAR', { || Alert( 'Salvou' ) }, 'Este botao Salva' } }  
             
       EndIf  
  
EndIf  
  
Return xRet
```

**Saiba Mais**  
[Ponto de Entrada Padrão do MVC](https://tdn.totvs.com/pages/releaseview.action?pageId=208345968)  
[Boas práticas MVC](https://tdn.totvs.com/pages/viewpage.action?pageId=28574107)
