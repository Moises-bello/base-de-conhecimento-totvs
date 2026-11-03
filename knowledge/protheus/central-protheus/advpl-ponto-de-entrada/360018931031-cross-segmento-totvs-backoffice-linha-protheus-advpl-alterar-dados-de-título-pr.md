---
article_id: 360018931031
category: ADVPL - Ponto de Entrada
content_hash: 285f53ae9a0c6c9b394d976f19ccee5509ce629b3e58ebc185936b83c4266057
fetched_at: '2026-06-28T22:40:11.625096+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Alterar dados de
  título pr ou pre na purchase order (EICPO400)
type: support-article
updated_at: '2023-10-11T12:34:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018931031-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Alterar-dados-de-t%C3%ADtulo-pr-ou-pre-na-purchase-order-EICPO400
---

**Dúvida**Como alterar dados (exemplo: a data do título) de um título gerado pela rotina *Purchase Order* (ordem de compra) no módulo SIGAEIC?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**Utilizar o ponto de entrada EICDUP.  
  
**Exemplo**

```
// BIBLIOTECAS NECESSÁRIAS  
#Include "TOTVS.ch  
  
// PONTO DE ENTRADA  
User Function EICDUPL()  
    // SE TIPO DO TÍTULO IGUAL A "PR",  
    // ALTERE A DATA DE EMISSÃO PARA 27/11/2018  
    // SE TIPO DO TÍTULO NÃO FOR IGUAL A "PR" E FOR IGUAL A "PRE",  
    // ALTERE A DATA DE EMISSÃO PARA 28/11/2018  
    If (cTipo =="PR")  
        dEmissao := CTod("27/11/2018")  
    ElseIf (cTipo =="PRE")  
        dEmissao := CTod("28/11/2018")  
    EndIf  
Return (NIL) // RETORNO
```

 **Observação**O ponto de entrada EICPO400 (*User Function* EICPO400) não servirá para alterações como a acima reportada. **Saiba mais**[EICDUPL - GRAVAÇÃO DOS TÍTULOS PR E PRE](https://tdn.totvs.com/pages/releaseview.action?pageId=510506592)

[EICPO400 - MANUTENÇÃO DO PURCHASE ORDER](https://tdn.totvs.com/pages/releaseview.action?pageId=699799390)
