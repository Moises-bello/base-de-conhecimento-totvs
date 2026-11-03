---
article_id: 360021360291
category: ADVPL - Ponto de Entrada
content_hash: f40d1c6835fce4f348bfa02f90d5cb2994aaa4d629054ece958ee62932a9356d
fetched_at: '2026-06-28T22:40:12.853885+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - QNCPABXP
type: support-article
updated_at: '2022-06-21T17:49:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021360291-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-QNCPABXP
---

**Dúvida**Estou utilizando o ponto de entrada QNCPABXP, existe algum campo ou algo que me informe qual o item do registro que estou selecionado?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**O ponto [**QNCPABXP**](http://tdn.totvs.com/pages/releaseview.action?pageId=6801057) não traz essa informação por paramixb mas é possível utilizar uma variável private "nItem".  
Exemplo : npositem:= M->nItem

```
#INCLUDE "PROTHEUS.CH"  
   
USER FUNCTION QNCPABXP ()  
 Local aArray := Paramixb[1]  
 Local lReturn := .F.  
 Local nCont := 0  
 Local npositem:= M->nItem  
  
 Alert("QNCPABXP" + cvaltochar(npositem))  
  
For nCont:= 1 to 11  
 MessageDlg(aArray[1][nCont])  
 Next  
Return
```

**Observação: esse ponto não tem retorno Lógico não é possível utilizar para validação sugerimos utilizar os pontos abaixo****Saiba Mais**[QNCAEACO - Baixa das Etapas](http://tdn.totvs.com/display/public/PROT/QNCAEACO+-+Baixa+das+Etapas)  
[QNCVALIF - Validação de Campos](http://tdn.totvs.com/pages/releaseview.action?pageId=6801035)
