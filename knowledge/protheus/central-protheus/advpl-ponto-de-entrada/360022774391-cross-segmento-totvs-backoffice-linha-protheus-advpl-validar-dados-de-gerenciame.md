---
article_id: 360022774391
category: ADVPL - Ponto de Entrada
content_hash: 0e470affb4e4a0ddd14ffc64debfcaf73d7332489851f8486e99b7a3240e34a1
fetched_at: '2026-06-28T22:40:11.588424+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) -  ADVPL - Validar dados
  de gerenciamento de projeto na solicitação de compra
type: support-article
updated_at: '2021-05-06T20:34:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022774391-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Validar-dados-de-gerenciamento-de-projeto-na-solicita%C3%A7%C3%A3o-de-compra
---

**Dúvida**É possível tornar o preenchimento dos campos da grid de Gerenciamento de Projetos (tabela AFG | Tecla F4) obrigatório na rotina de Solicitação de Compras (MATA110)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**Pode ser utilizado o ponto de entrada MTA110OK (valida a gravação de dados por meio de retorno lógico) em conjunto com as variáveis aRatAFG (linhas da grid) e aHdrAFG (campos da grid).  
  
**Fonte**

```
// BIBLIOTECAS NECESSÁRIAS  
#Include "TOTVS.ch"  
  
// PONTO PARA VALIDAÇÃO DE GRAVAÇÃO DE SOLICITAÇÃO DE COMPRA  
User Function MTA110OK()  
    Local nNumSol  := PARAMIXB[1] // NÚMERO DA SOLICITAÇÃO  
    Local cNomeSol := PARAMIXB[2] // NOME DO SOLICITANTE  
    Local dDataSol := PARAMIXB[3] // DATA DA SOLICITAÇÃO  
    Local lValid   := .F.         // CONTROLE DE PROCESSAMENTO DA ROTINA  
  
    // VERIFICA SE A GRID DE GERENCIAMENTO DE PROJETO FOI PREENCHIDA  
    If (Len(aRatAFG) > 0 .And. Len(aRatAFG[1]) > 1)  
        // VALIDA SE OS CAMPOS PROJETO (AFG_PROJET) E TAREFA (AFG_TAREFA) ESTÃO PREENCHIDOS  
        For nX := 1 To Len(aRatAFG[1][2])  
            If (Empty(aRatAFG[1][2][nX][AScan(aHdrAFG, {|x| AllTrim(x[2]) == "AFG_PROJET"})]) .Or.;  
                Empty(aRatAFG[1][2][nX][AScan(aHdrAFG, {|x| AllTrim(x[2]) == "AFG_TAREFA"})]))  
                lValid := .F. // RETORNO FALSO CASO OS CAMPOS ESTEJAM VAZIO  
  
                // MENSAGEM DE ERRO PARA O USUÁRIO  
                Help(NIL, NIL, "EMPTY_PROJECT", NIL, "Existem campos não preenchidos",;  
                    1, 0, NIL, NIL, NIL, NIL, NIL, {"Realize o preenchimento dos campos da " +;  
                    "grid de Gerenciamento de Gerenciamento de Projetos (AFG)"})  
            EndIf  
        Next nX  
    EndIf  
Return (lValid)
```

**Variáveis**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020132592/mceclip0.png)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019992051/mceclip1.png)

**Saiba mais**  
[MTA110OK - Valida inclusão da SC](http://tdn.totvs.com/pages/releaseview.action?pageId=6085567)
