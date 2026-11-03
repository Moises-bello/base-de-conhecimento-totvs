---
article_id: 360021106391
category: Ativo Fixo - Ponto de entrada, Customizações, Funções, Execauto
content_hash: 6bed184a4a2a006fbc88486fcde4f6d322ad62bd666f1ee40b3519d459aba5e1
fetched_at: '2026-06-28T22:41:39.066516+00:00'
product: protheus
section_id: 1500001536601
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAATF - Ponto de entrada
  MVC ATFA036
type: support-article
updated_at: '2024-03-22T19:57:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021106391-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAATF-Ponto-de-entrada-MVC-ATFA036
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**O ponto entrada **AF030VLBX** não está funcionando na versão P12.1.17

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**Conforme documentação o ponto ATFA036L substitui o ponto de entrada AF030VLBX da rotina ATFA030 e o ponto de entrada AF035BLBX da rotina ATFA035.   
Ponto de entrada **[ATFA036L](http://tdn.totvs.com/pages/releaseview.action?pageId=143656357)** Este ponto só é acionado na opção "*Baixa em Lote*" para opção "Baixa" utilize o modelo de exemplo.  
Como a rotina já está em MVC é necessário utilizar o Ponto de entrada Padrão MVC.  
O id do modelo da dados da rotina ATFA036 é ATFA036, assim sendo, a assinatura da função de usuário deve ser **User Function ATFA036()**.

**Observação:** O nome do arquivo.prw não poderá ser o mesmo da user function.

**Saiba Mais**Todos os pontos de entrada terão seu legado mantido, salvo os pontos que consideramos como pontos padrões (ex: validação após a gravação e botões que serão substituídos), os pontos que trazem conteúdo do sistema por PARAMIXB, esses serão mantidos com suas particularidades

**Exemplo**

```
#include "parmtype.ch"  
  
User Function ATFA036()  
    Local aParam := PARAMIXB  
    Local xRet := .T.  
    Local oObj := ""  
    Local cIdPonto := ""  
    Local cIdModel := ""  
    Local lIsGrid := .F.  
    Local nLinha := 0  
    Local nQtdLinhas := 0  
    Local cMsg := ""  
  
    If aParam <> NIL  
        oObj := aParam[1]  
        cIdPonto := aParam[2]  
        cIdModel := aParam[3]  
        lIsGrid := (Len(aParam) > 3)  
  
        If cIdPonto == "MODELPOS"  
            cMsg := "Chamada na validação total do modelo." + CRLF  
            cMsg += "ID " + cIdModel + CRLF  
            xRet := ApMsgYesNo(cMsg + "Continua?")  
        ElseIf cIdPonto == "FORMPOS"  
            cMsg := "Chamada na validação total do formulário." + CRLF  
            cMsg += "ID " + cIdModel + CRLF  
  
            If lIsGrid  
                cMsg += "É um FORMGRID com " + Alltrim(Str(nQtdLinhas)) + " linha(s)." + CRLF  
                cMsg += "Posicionado na linha " + Alltrim(Str(nLinha)) + CRLF  
            Else  
                cMsg += "É um FORMFIELD" + CRLF  
            EndIf  
            xRet := ApMsgYesNo(cMsg + "Continua?")  
        ElseIf cIdPonto == "FORMLINEPRE"  
            If aParam[5] == "DELETE"  
                cMsg := "Chamada na pré validação da linha do formulário. " + CRLF  
                cMsg += "Onde esta se tentando deletar a linha" + CRLF  
                cMsg += "ID " + cIdModel + CRLF  
                cMsg += "É um FORMGRID com " + Alltrim(Str(nQtdLinhas)) + " linha(s)." + CRLF  
                cMsg += "Posicionado na linha " + Alltrim(Str(nLinha)) + CRLF  
                xRet := ApMsgYesNo(cMsg + " Continua?")  
            EndIf  
  
        ElseIf cIdPonto == "FORMLINEPOS"  
            cMsg := "Chamada na validação da linha do formulário." + CRLF  
            cMsg += "ID " + cIdModel + CRLF  
            cMsg += "É um FORMGRID com " + Alltrim(Str(nQtdLinhas)) + " linha(s)." + CRLF  
            cMsg += "Posicionado na linha " + Alltrim(Str(nLinha)) + CRLF  
            xRet := ApMsgYesNo(cMsg + " Continua?")  
        ElseIf cIdPonto == "FORMCOMMITTTSPRE"  
            ApMsgInfo("Chamada após a gravação da tabela do formulário.")  
        ElseIf cIdPonto == "FORMCOMMITTTSPOS"  
            ApMsgInfo("Chamada após a gravação da tabela do formulário.")  
        ElseIf cIdPonto == "MODELCANCEL"  
            cMsg := "Deseja realmente sair?"  
            xRet := ApMsgYesNo(cMsg)  
        ElseIf cIdPonto == "BUTTONBAR"  
            xRet := {{"Salvar", "SALVAR", {||u_TSMT020()}}}  
        EndIf  
    EndIf  
Return xRet  
  
User Function TSMT020()  
    Alert("Buttonbar")  
Return NIL
```
