---
article_id: 4412372676503
category: ADVPL - Classe e Função
content_hash: a349fd016b51c3503d57a4b9639479ef506a7fe792b43d5c850dbfbc000aa6af
fetched_at: '2026-06-28T22:40:20.574350+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Classe FwPrinterXlsx
  com uso de fórmula
type: support-article
updated_at: '2021-11-05T18:36:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412372676503-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Classe-FwPrinterXlsx-com-uso-de-f%C3%B3rmula
---

**Dúvida**Como usar fórmula excel com a classe **FwPrinterXlsx** ?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL- Todas as versões  
  
**Solução**Para gerar fórmulas no Excel é possível através do método **setFormula** da classe **FwPrinterXlsx,**segue exemplo de utilização:

```
User function xlsx()  
  
    local oPrtXlsx as object  
    local cFilename as character  
    local lRet as logical  
  
    cFilename := '/system/'+cValToChar(ThreadId())+'_teste.rel'  
    ferase(cFilename)  
  
    oPrtXlsx := FwPrinterXlsx():New()  
  
    lRet := oPrtXlsx:Activate(cFilename)  
    lRet := oPrtXlsx:AddSheet("1 - Plan")  
  
    oPrtXlsx:SetValue(1, 1, 2)  
    oPrtXlsx:SetValue(2, 1, 3)  
  
    oPrtXlsx:SetFormula(4, 1,"=Average(A1:A2)")  
  
    lRet := oPrtXlsx:toXlsx()  
  
    oPrtXlsx:DeActivate()  
  
Return
```

Verifique que no exemplo a Fórmula é passada em inglês, pois para uso do **SetFormula** no **FwPrinterXlsx** a mesma deve ser escrita em inglês.

No caso da média deverá ser**oPrtXlsx:SetFormula(4, 1,"=AVERAGE(A1:A2)")**

**Saiba mais**  
<https://tdn.totvs.com/display/framework/FwPrinterXlsx>
